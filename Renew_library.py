#!/Users/'your_user_name'/anaconda2/bin/python2.7
import time
import argparse
from datetime import datetime

##### TAKE ARGUMENTS #####

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-u", "--username", help="Your username/barcode, can be found on the back of UCL card", type=str)
parser.add_argument("-p", "--password", help="Your password or PIN, if not changed is set to date and month of you birthday", type=str)
args = parser.parse_args()


class Library(object):
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

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        #If you run this as a launchd, the full path to the chromedriver must be specified:
        # browser = webdriver.Chrome('/Users/'your user name'/anaconda2/bin/chromedriver', chrome_options=options)
        browser = webdriver.Chrome(chrome_options=options)
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
    
        text_file = open("Your path to the logout file", "a")
        text_file.write('Library books renewed on {0}/{1}/{2}\n'.format(datetime.today().day,\
                                                                        datetime.today().month,\
                                                                        datetime.today().year))
        text_file.close()
    
        return

    
##### TRY TO RUN THE CODE WITH THE ARGUMENTS FROM ARGPARSE #####

def internet_on():
    '''Check the internet connection'''

    import urllib2

    while True:
        try:
            response=urllib2.urlopen('http://google.com', timeout=20)
            return True
            break
        except urllib2.URLError, e: 
            time.sleep(20)
            pass

def mainloop():

    connection = internet_on()

    try:
        mylib = Library(args.password, args.username)
        mylib.renew()
        mylib.record()
    except Exception, e:
        with open("Your path to the logout file", "a") as file:
            file.write('Something went wrong on {0}/{1}/{2}\nThe error occured {3}'.format(datetime.today().day,\
                                                                            datetime.today().month,\
                                                                            datetime.today().year), e)

mainloop()
