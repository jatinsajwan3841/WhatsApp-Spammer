from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Name=str(input("Enter name or phone no. of target."))
#make sure that in search it appears on first place, it's better to enter phone number for 100% success.

Message=str(input("Enter your target message"))
NumberOfMessages=int(input("No. of messages to send"))
Interval=int(input("Time interval in between subsequent messages"))


def whatsappspam():
    # for using the default chrome profile
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Jatin\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome( executable_path="C:\\Users\\Jatin\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe", options=options)

    #Opening WhatsappWeb
    driver.get('https://web.whatsapp.com')

    time.sleep(15)
    elem = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    elem.send_keys(Name)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for i in range(NumberOfMessages):
        elem.send_keys(Message)
        elem.send_keys(Keys.RETURN)
        time.sleep(int(Interval))

whatsappspam()
