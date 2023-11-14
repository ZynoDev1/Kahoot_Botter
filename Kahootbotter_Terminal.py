from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FireFoxOptions
#made by zyno remove this if ur gay as shit 
def main():
    options = FireFoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    title = ("""
 _  __    _    _   _  ___   ___ _____   ____   ___ _____ _____ _____ ____  
| |/ /   / \  | | | |/ _ \ / _ \_   _| | __ ) / _ \_   _|_   _| ____|  _ \ 
| ' /   / _ \ | |_| | | | | | | || |   |  _ \| | | || |   | | |  _| | |_) |
| . \  / ___ \|  _  | |_| | |_| || |   | |_) | |_| || |   | | | |___|  _ < 
|_|\_\/_/   \_\_|_|_|\___/_\___/_|_|_  |____/ \___/_|_|   |_| |_____|_| \_\
                 
                | __ ) \  /  |__  /\ \ / / \ | |/ _ \                      
                |  _ \ \ /    / /  \ V /|  \| | | | |                     
                | |_) || |    / /_   | | | |\  | |_| |                     
                |____/ |_|   /____|  |_| |_| \_|\___/        
""")
    prefix='Console >> '
    print(title)
    pin = int(input(prefix+'Input kahoot pin » '))
    amount = int(input(prefix+'Bots » '))  
    cnames = str(input(prefix+'Type custom name, Press enter to use default setting » '))
    global cnter
    cnter = 0
    def bot():
        print("LOADING BOT  BOTNUMBER| "+ str(amount))
 
        driver.get("https://kahoot.it")
        pinloc = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/input")
        pinloc.click()
        pinloc.send_keys(pin)
        startbutton = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[3]/div[2]/main/div/form/button")
        startbutton.click()
        time.sleep(0.65)
        try:
            userfield = driver.find_element(By.ID, "nickname")    
        except NoSuchElementException:
             print("""Element with ID 'nickname' not found.
                      Most likely invalid pin returning to main program""")
             main()
        userfield.click()
        if not cnames:
         userfield.send_keys('stfu fuck you ')
        elif cnames != None:
            userfield.send_keys(cnames+str(cnter))
        start = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div/div[2]/main/div/form/button")
        start.click()
        print(' BOT SUCCESFULLY JOINED BOTNUMBER| ' + str(amount))
        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
    while amount > 0:
        cnter = cnter+1
        bot()  
        amount = amount - 1  
    if amount == 0:
        cnter = 0
        print("""Botting done 
              Returning back to main program in 5 seconds""")
        time.sleep(5)
        main()
main()
