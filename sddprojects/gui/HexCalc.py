# coded without following an online tutorial
# step 4, final version of Hex calculator

import operator
import re
from tkinter import *

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "//": operator.floordiv,
    "**": operator.pow,
    "%": operator.mod,
}
BUTTON_WIDTH = 4
BUTTON_HEIGHT = 5
BUTTON_PADX = 1
BUTTON_PADY = 3
FONT = "Helvetica 20 bold"
BG_COLOR = "blue violet"
DISPLAY_COLOR = "SlateBlue1"
INPUT_WIDTH = 19

# takes in 2 numbers in hex and an operator and returns a hex number


def hexCalc(firstHexOperand, oper, secondHexOperand):
    return hex(OPERATORS[oper](int(firstHexOperand, 16), int(secondHexOperand, 16)))


def calculate(string):
    oper_indices = [(match.start(), match.end())
                    for match in re.finditer(r"[*]+|//|[-+%]", string)]
    if len(oper_indices) > 1 or "ERROR" in string:
        return "ERROR"
    if len(oper_indices) == 0:
        return string
    if len(string) == oper_indices[0][1] + 2 or string[oper_indices[0][0] - 1] == "x":
        return "ERROR"
    try:
        result = hexCalc(string[:oper_indices[0][0]], string[oper_indices[0][0]:oper_indices[0][1]], string[oper_indices[0][1]:])
    except ZeroDivisionError:
        return "ERROR"
    if len(result) > INPUT_WIDTH or result[0] == "-":
        return "ERROR"
    return result


def main():
    window = Tk()
    window.title("XY's hex calculator w(°ｏ°)w")
    window.config(bg=BG_COLOR)

    # display
    display = StringVar()
    display.set("0x")
    output = Label(window, height=1, width=INPUT_WIDTH, textvariable=display,
                   bd=4, relief="solid", font=FONT, anchor=E, bg=DISPLAY_COLOR)
    output.grid(column=0, row=0, sticky=W+E)

    # buttonsz
    buttons = Frame(window)
    buttons.config(padx=2, pady=2, bg=BG_COLOR)
    buttons.grid(column=0, row=1)

    # operators
    for i, op in enumerate(OPERATORS):
        Button(buttons, text=op, width=BUTTON_WIDTH,
               font=FONT, command=lambda o=op: display.set(display.get() + o + "0x")).grid(row=i // 2, column=(i % 2) * 3, padx=BUTTON_PADX, pady=BUTTON_PADY)

    # numbers
    for i in range(16):
        Button(buttons, text=hex(i)[2:], width=BUTTON_WIDTH, font=FONT, command=lambda n=hex(i)[2:]: display.set(display.get() + n)).grid(
            column=i % 4, row=4 + i // 4, padx=BUTTON_PADX, pady=BUTTON_PADY)

    # misc
    Button(buttons, text="Clear", width=int(BUTTON_WIDTH * 1.5),
           font=FONT, command=lambda: display.set("0x")).grid(column=0, row=8, columnspan=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky=W)
    Button(buttons, text="=", width=BUTTON_WIDTH,
           font=FONT, command=lambda: display.set(calculate(display.get()))).grid(column=3, row=8, padx=BUTTON_PADX, pady=BUTTON_PADY)
    window.mainloop()


if __name__ == "__main__":
    main()
