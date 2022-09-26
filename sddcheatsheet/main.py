from response import Responder

responder = Responder()
responder.login()
for i in range(20):
    responder.code_run()
    responder.next_level()
#responder.driver.quit()
