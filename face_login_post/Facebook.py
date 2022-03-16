from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com')



class FACEBOOK_GROUPS_POST:

    def sign_in(self,username,password):
        login_user = driver.find_element(By.CSS_SELECTOR, 'input.inputtext._55r1._6luy')
        login_password = driver.find_element(By.CSS_SELECTOR, 'input.inputtext._55r1._6luy._9npi')
        login_user.send_keys(username)
        login_password.send_keys(password)
        time.sleep(3)
        login_password.submit()
        time.sleep(3)


    def write_post(self,group_number,message):
        driver.get(f'https://www.facebook.com/groups/{group_number}')
        time.sleep(2)
        post_pad = driver.find_element(By.CSS_SELECTOR, 'div.m9osqain.a5q79mjw.gy2v8mqq.jm1wdb64.k4urcfbm.qv66sw1b')
        post_pad.click()
        time.sleep(5)
        writing_area = driver.find_element(By.CSS_SELECTOR, 'div._1mf._1mj')
        writing_area.send_keys(message)
        time.sleep(5)
        post = driver.find_element(By.CSS_SELECTOR, 'div._1mf._1mj')
        post.submit()
        time.sleep(7)

    def close_browser(self):
        driver.close()