from django.shortcuts import render
from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .full_shot import image_scrapping
from .full_shot import browser_on
from .crop_img import crop_col_img
from .crop_img import split_img
from .crop_img import img_concat
from .crop_img import image_preprocessing
import sys

# Create your views here.
browser = browser_on()

def index(request):
    global browser
    # from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
    scrollheight = browser.execute_script(js)
    print(f'scrollheight : {scrollheight}')
    scale = 0.8
    browser.execute_script(f'document.body.style.MozTransform = "scale({scale})";')

    return render(request, 'pages/index.html')


def output(request):
    print('output...')
    url = request.GET.get('url')
    print(f'@@@@@@@@@@@@@url : {url} type : {type(url)}')
    global browser
    browser.get(url)
    browser.implicitly_wait(10)
    image_scrapping(browser, [url])
    working_path = r'C:\OCR-SizeTable\OCR_test\django-ocrpj\pages\static\pages\screen_shot'
    saving_path =  r'C:\OCR-SizeTable\OCR_test\crawling'
    image_preprocessing(working_path, saving_path)
    return render(request, 'pages/output.html')

