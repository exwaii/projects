# Molly Bolly
from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar

def main():
    window = Tk()
    window.title("Molly Bolly Settings")
    window.minsize(width=600, height=300)
    window.config(padx=20, pady=20)


    time = Frame(window)
    time.grid(column=0, row=0, sticky=W, ipadx=20, ipady=20)
    dayson = Combobox(time, width = 27, values = ("Days on", "Days off"))
    dayson.current(0)
    dayson.pack(pady=20)
    cal = Calendar(time, width=12, height=250, font="Arial 8", selectmode='day', locale='en_US', year=2002, month=4, day=17, showweeknumbers=False, showothermonthdays=False)
    cal.pack()


    appearance = Frame(window)
    appearance.grid(column=1, row=0, ipadx=20, ipady=20, columnspan=2)

    ground = StringVar(appearance)
    ground.set("back")
    bg = Radiobutton(appearance, text="Background", variable=ground, value="back")
    bg.grid(column=0, row=0, columnspan=3)
    fg = Radiobutton(appearance, text="Foreground", variable=ground, value="fore")
    fg.grid(column=0, row=1, columnspan=3, pady=20)
    
    r = IntVar()
    r.set(255)
    b = IntVar()
    b.set(255)
    g = IntVar()
    g.set(255)
    color_display = Label(appearance, bg=f'#{r.get():02x}{g.get():02x}{b.get():02x}', height=6, width=10    , relief=SUNKEN)
    color_display.grid(column=3, row=2, columnspan=2, padx=(5,0), sticky=E)
    def update_color(x):
        color_display.config(bg=f'#{r.get():02x}{g.get():02x}{b.get():02x}')
    rslider = Scale(appearance, from_=0, to=255, orient=VERTICAL, variable=r, command=update_color)
    rslider.grid(column=0, row=2, sticky=W)
    gslider = Scale(appearance, from_=0, to=255, orient=VERTICAL, variable=g, command=update_color)
    gslider.grid(column=1, row=2, sticky=W)
    bslider = Scale(appearance, from_=0, to=255, orient=VERTICAL, variable=b, command=update_color)
    bslider.grid(column=2, row=2, sticky=W)
    


    red = Label(appearance, text="Red")
    red.grid(column=0, row=3, sticky=E)
    green = Label(appearance, text="Green")
    green.grid(column=1, row=3, sticky=E)
    blue = Label(appearance, text="Blue")
    blue.grid(column=2, row=3, sticky=E)


    settings = Frame(window)
    settings.grid(column=3, row=0, sticky=E, ipadx=20, ipady=20)

    alwayson = BooleanVar()
    always = Checkbutton(settings, text="Always use these settings", variable=alwayson, onvalue=True, offvalue=False)
    always.grid(column=0, row=0, sticky=W, pady=10)

    startupon = BooleanVar()
    startup = Checkbutton(settings, text="Run on startup", variable=startupon, onvalue=True, offvalue=False)
    startup.grid(column=0, row=1, sticky=W, pady=10)
    
    soundson = BooleanVar()
    sounds = Checkbutton(settings, text="Activate sounds", variable=soundson, onvalue=True, offvalue=False)
    sounds.grid(column=0, row=2, sticky=W, pady=10)

    daytimeon = BooleanVar()
    daytime = Checkbutton(settings, text="Daytime only",  variable=daytimeon, onvalue=True, offvalue=False)
    daytime.grid(column=0, row=3, sticky=W, pady=10)

    ok = Button(settings, text="OK", command=exit)
    ok.grid(column=0, row=4, sticky=W)
    cancel = Button(settings, text="Cancel", command=exit)
    cancel.grid(column=0, row=5, sticky=W)

    window.mainloop()

if __name__ == "__main__":
    main()