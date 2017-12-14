import time
from datetime import datetime

class Library():
    
    def __init__(self, password, username):
        
        self.password = password
        self.username = username
        self.url = 'https://www.ucl.ac.uk/library/'
        
    def renew(self):

        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        chromedriver = 'Your path to the browser driver'
        browser = webdriver.Chrome(chromedriver)
        browser.get(self.url)

        button_login_page = browser.find_element_by_id('loginText')
        button_login_page.click()

        user_entry = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.ID, "bor_id")))
        pass_entry = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.ID, "bor_verification")))

        user_entry.send_keys(self.username)
        pass_entry.send_keys(self.password)

        login_button = browser.find_element_by_css_selector(".button[value='Login']")
        login_button.click()

        renew_button = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.ID, "renewAllButton")))
        renew_button.click()

        time.sleep(2)

        browser.close()
        browser.quit()
        
        return
    
    def record(self):
    
        text_file = open("Your path to the file to write", "a")
        text_file.write('Library books renewed on {0}/{1}/{2}\n'.format(datetime.today().day,\
                                                                        datetime.today().month,\
                                                                        datetime.today().year))
        text_file.close()
        
        return

class _check():

    def __init__(self):
        
        self.url = 'https://www.ucl.ac.uk/library/'
        self.period = 20
        
    def check(self):
        
        import urllib2
        
        while True:
            try:
                answ = urllib2.urlopen(self.url)
                
                if answ:
                    return True
                    break
                    
                else: pass
                
            except Exception, e:
                print e, '\n You have no internet connection!'
                time.sleep(self.period)

day = datetime.today().weekday()
connection = _check()

if day == 1:
    
    try:
    
        connection.check()

        while True:

            USERNAME = raw_input('Please enter your username: ')
            PASSWORD = raw_input('Guess the password: ')

            if len(PASSWORD) == 4 and len(USERNAME) == 11:
                library = Library(PASSWORD, USERNAME)
                library.renew()
                library.record()
                break

            else:
                print '\nPassword or username length does not match!\nTry again:'
            
    except Exception, e:
        print e
        
else: pass
