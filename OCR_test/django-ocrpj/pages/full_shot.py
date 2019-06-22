from selenium import webdriver
from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import os
import time
import sys

def browser_on():
    driver_path = 'C:/OCR-SizeTable/OCR_test/django-ocrpj/pages/geckodriver.exe'
    sys.path.append(driver_path)
    options = webdriver.FirefoxOptions()

    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    # 사람처럼 보이게
    options.add_argument("disable-gpu")   # 가속 사용 x
    #options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko') # user-agent

    return webdriver.Firefox(executable_path=driver_path, options=options)

def image_scrapping(browser,href_list):
    over_weight = 0
    for idx, href in enumerate(href_list):
        print(f'{idx+1}/{len(href_list)} screent shot...')

        browser.get(href)
        browser.implicitly_wait(15)
        # 팝업창 닫기

        # from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
        js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
        scrollheight = browser.execute_script(js)
        if scrollheight > 40000:
            print(f'scrollheight over: {scrollheight} !!')
            over_weight +=1
            print(f'over_weight_count : {over_weight}')
            continue
        scale = 0.8
        browser.execute_script(f'document.body.style.MozTransform = "scale({scale})";')
        time.sleep(2)

        slices = []
        offset = 0
        while offset < scrollheight:
            browser.execute_script(f'window.scrollTo(0, {offset});')
            time.sleep(0.1)
            img = Image.open(BytesIO(browser.get_screenshot_as_png()))
            offset += img.size[1]

            slices.append(img)

            # print (f'{offset} / {scrollheight}')
        screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
        offset = 0
        for img in slices:
            screenshot.paste(img, (0, offset))
            offset += img.size[1]
        screenshot.save(f'C:/OCR-SizeTable/OCR_test/django-ocrpj/pages/static/pages/screen_shot/screen_shot_{idx}.png')
