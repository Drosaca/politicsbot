#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import time
import os
import sys

print('Welcome')
try:
    load_dotenv()
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    HEADLESS = os.getenv('HEADLESS')
    MAX = 2000000
    REWARD = 80000
    if not EMAIL or not PASSWORD:
        raise Exception
    print('environement loaded')
except:
    print("Please copy .env.example to .env and modify it", file=sys.stderr)
    exit()


def main():
    options = Options()
    options.headless = HEADLESS == 'true'
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
    elem = driver.find_element_by_id("loginbox")
    elem.click()
    elem = driver.find_element_by_name("loginform")
    elem.click()
    print('logging...')
    time.sleep(5)
    try:
        elem = driver.find_elements_by_class_name("close")
        elem[0].click()
    except:
        pass
    try:
        driver.get("https://politicsandwar.com/rewarded-ads/")
        time.sleep(2)
        #ads = driver.find_element_by_css_selector("a[href='https://politicsandwar.com/rewarded-ads/']")
        #ads.click()
    except Exception as e:
        print(e)
    print('watching')
    time.sleep(3)
    spam(driver)
    driver.close()  # Press Ctrl+F8 to toggle the breakpoint.


FIRST_AMOUNT = 0
HARVESTED = 1

def recaptcha(driver):
    pass

def spam(driver):
    wallet = [get_actual_amount(driver), 0]
    keep_running = should_continue(driver)
    while keep_running:
        try:
            elem = driver.find_element_by_id("btnAds")
            elem.click()
            time.sleep(2)
            wallet[HARVESTED] += REWARD
            print("waiting 120s...")
            time.sleep(120)
        except:
            print("waiting more 10s...")
            time.sleep(10)
        keep_running = should_continue(driver, wallet)
    print("exiting...")


def should_continue(driver, wallet=[0, 0]):
    try:
        elem = driver.find_element_by_id("rewarded_ads_earnings_today")
        amount = int(elem.text.replace(',', ''))
        print(amount, ' <---> ', wallet[FIRST_AMOUNT] + wallet[HARVESTED])
        if int(amount) >= MAX:
            print("Maximum amount of money reached")
            return False
        if int(wallet[FIRST_AMOUNT] + wallet[HARVESTED] > MAX):
            print("incoherent values refreshing...")
            refresh(driver)
            time.sleep(4)
            wallet[FIRST_AMOUNT] = get_actual_amount(driver)
            wallet[HARVESTED] = 0
            if wallet[FIRST_AMOUNT] >= MAX:
                return False
        return True
    except:
        return True


def refresh(driver):
    ads = driver.find_element_by_css_selector("a[href='https://politicsandwar.com/rewarded-ads/']")
    ads.click()


def get_actual_amount(driver):
    try:
        elem = driver.find_element_by_id("rewarded_ads_earnings_today")
        amount = int(elem.text.replace(',', ''))
        return amount
    except:
        return 0


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


if __name__ == '__main__':
    main()
