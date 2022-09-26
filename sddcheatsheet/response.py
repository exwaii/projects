from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv
from time import sleep


load_dotenv()

# has_path_right has_path_left enemy_in_sight is_gap_ahead()
# 4 digit starting with 8 is a bush
# anything starting wtih 0 is empty
# 4 is grass
# 1 is path
dict = {
    8101: "bush",
    8112: "sticktree",
    31: "treasure",
}


class Responder:
    def __init__(self):
        self.user = os.environ.get("USER")
        self.password = os.environ.get("PASSWORD")
        self.driver = webdriver.Chrome(service=Service("/Users/xy/Downloads/chromedriver_win32/chromedriver.exe"))
        self.headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/97.0.4692.71 Safari/537.36", }

    def login(self):
        self.driver.get(url="https://www.tynker.com/#/login/student")
        sleep(2)
        self.driver.find_element(By.ID, "email-input").send_keys(self.user)
        self.driver.find_element(By.ID, "password-input").send_keys(self.password)
        self.driver.find_element(By.ID, "password-input").send_keys(Keys.ENTER)
        sleep(2)
        self.driver.get(url="https://www.tynker.com/nb/project/58225568af9231d0668b465a/?dir=director&chapterid"
                            "=57f69349af92317e458b458c&s=3")

    def code_run(self):
        code_ui = self.driver.find_elements(By.CSS_SELECTOR, ".CodeMirror-code")[3]
        self.driver.fullscreen_window()
        code_ui.click()
        sleep(2)
        code_ui = ActionChains(self.driver)
        code_ui.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        code_ui.key_down(Keys.DELETE).key_up(Keys.DELETE)
        code_ui.send_keys("while not reached_goal():")
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        code_ui.send_keys("forward()")
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        code_ui.send_keys("if is_gap_ahead():")
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        code_ui.send_keys("jump()")
        code_ui.perform()
        sleep(0.1)
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        sleep(0.1)
        for i in range(4):
            code_ui.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        sleep(0.1)
        #code_ui.key_down(Keys.TAB).key_up(Keys.TAB)
        code_ui.send_keys("if has_path_left():")
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        code_ui.send_keys("turn_left()")
        code_ui.perform()
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        sleep(0.1)
        for i in range(4):
            code_ui.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        sleep(0.1)
        #code_ui.key_down(Keys.TAB).key_up(Keys.TAB)
        code_ui.send_keys("if has_path_right():")
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        code_ui.send_keys("turn_right()").perform()
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        sleep(0.1)
        for i in range(4):
            code_ui.key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        sleep(0.1)
        # code_ui.key_down(Keys.TAB).key_up(Keys.TAB)
        code_ui.send_keys("if enemy_in_sight():")
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        code_ui.send_keys("fire()").perform()
        code_ui.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        play = self.driver.find_element(By.XPATH, '//*[@id="playstop"]/a[1]')
        play.click()
        #sleep(20)


    def next_level(self):
        sleep(45)
        next_button = self.driver.find_element(By.XPATH, '//*[@class="congrats-footer"]/a[2]') 
        next_button.click()
        sleep(5)