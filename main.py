import time
import requests
from selenium import webdriver

time_url  = 'http://worldtimeapi.org/api/timezone/Asia/Tehran'
login_url = 'https://lms1.sbu.ac.ir/login/index.php'
class_url = 'https://lms1.sbu.ac.ir/mod/onlineclass/view.php?id=4601'

username = 'USERNAME'   # Put your own username.
password = 'PASSWORD'   # Put your own password.

start_hour = 10         # Class start hour (24-hour format).
start_minute = 30       # Class start minute.
sleep_duration = 60     # Sleep duration between tries (seconds).

# Xpath of components
username_input  =   '//*[@id="username"]'
password_input  =   '//*[@id="password"]'
login_submit    =   '//*[@id="loginbtn"]'
class_link      =   '//*[@id="id_submitbutton"]'
open_class      =   '//*[@id="launchOptionsDialog"]/div[2]/coral-dialog-content/div[1]/div[1]/div'

# chromedriver_path = '/home/parsa/Downloads/chromedriver_linux64/chromedriver'     # Linux
chromedriver_path = "D:\\chromedriver_win32\\chromedriver.exe"                      # Windows

while(True):  
    try:                                                                            # Try-except in case API call fails.
        print('Getting time.')
        response = requests.get(time_url).json()
        current_time = response['datetime'].split('T')[1].split('.')[0]
        hour = int(current_time.split(':')[0])
        minute = int(current_time.split(':')[1])
        print('Time: {}:{}'.format(hour, minute))
        if (hour == start_hour) and (minute >= start_minute):
            print('Connecting to class.')
            driver = webdriver.Chrome(executable_path=chromedriver_path)
            driver.get(login_url)
            driver.find_element_by_xpath(username_input).send_keys(username)
            driver.find_element_by_xpath(password_input).send_keys(password)
            driver.find_element_by_xpath(login_submit).click()
            driver.get(class_url)
            driver.find_element_by_xpath(class_link).click()
            driver.find_element_by_xpath(open_class).click()
            break
        else:
            print('Time incorrect. Waiting...')
            time.sleep(sleep_duration)
    except:
        print('Getting time failed. Re-trying...')
        time.sleep(sleep_duration)