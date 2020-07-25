# WhatsApp-Spammer
Spam someone's WhatsApp using python script

#Required Module:
Selenium for webdriver control.
 
 Install by either using
 
 ''' python
 pip install selenium
 '''
 
 or visit <a href="https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium" target="_blank">here</a> for other way around.
                        
 The browser interface driver is required, here in this I have tried and tested using ChromeDriver 85.0.4183.38.
 For downloading according to your preference visit <a href="https://selenium-python.readthedocs.io/installation.html#drivers" target="_blank">here</a>
 
 After setting up everything change the location of driver to the downloaded location in main.py
 
 The chrome profile used in this script is default chrome profile and the code will fail if chrome is already opened.
 For proper functioning keep chrome closed.
 The main reason I used default chrome profile is that many like me are used to keep logged in sessions of whatsapp in whatsapp web,
 so to skip scanning qr code again and again did this. 
 If you do not want to open the default chrome profile and rather have separate instance, remove chrome options from the code.
 
 Please note that while typing the target name make sure it appears on first place in search, it's better to enter phone number for 100% success.
 I'll try to provide comments wherever necessary in code.
 
 Change 
 
 '''python
 time.sleep()
 '''
 
 value according to your internet speed as if the page do not loads in that time the code will throw error of element not found. 
 Will try to find other way to solve this.
 
 And do not start spamming everyone unless you seriously want a tight hit 😅.
