# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import time
import os
import sys

load_dotenv()

try:
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    MAX = 2000000
except:
    print("please fill your credentials in .env file", file=sys.stderr)
    exit()


def run(name):
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    driver.get("https://politicsandwar.com/login/")
    time.sleep(2)
    try:
        elem = driver.find_element_by_id("consent_agree_btn")
        elem.click()
    except:
        pass
    elem = driver.find_element_by_name("email")
    elem.send_keys(EMAIL)
    elem = driver.find_element_by_name("password")
    elem.send_keys(PASSWORD)
    elem = driver.find_element_by_name("loginform")
    elem.click()
    print('logging...')
    time.sleep(5)
    try:
        elem = driver.find_elements_by_class_name("close")
        elem[0].click()
    except:
        pass
    ads = driver.find_element_by_css_selector("a[href='https://politicsandwar.com/rewarded-ads/']")
    ads.click()
    print('watching')
    time.sleep(3)
    spam(driver)
    driver.close()  # Press Ctrl+F8 to toggle the breakpoint.


def spam(driver):
    keep_running = stop(driver)
    while keep_running:
        try:
            elem = driver.find_element_by_id("btnAds")
            elem.click()
            time.sleep(2)
            print("waiting 120s...")
            time.sleep(120)
        except:
            print("waiting more 10s...")
            time.sleep(10)
        keep_running = stop(driver)
    print("exiting...")


def stop(driver):
    try:
        elem = driver.find_element_by_id("rewarded_ads_earnings_today")
        amount = int(elem.text.replace(',', ''))
        print(amount)
        if int(amount) >= MAX:
            print("Maximum amount of money reached")
            return False
        return True
    except:
        return True

def try_mute(driver: webdriver):
    try:
        driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        elem = driver.find_element_by_id("applixir_video_ima-mute-div")
        elem.click()
        print("muted")
        driver.switch_to_default_content()
    except:
        driver.switch_to_default_content()
        print("fail to mute")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
