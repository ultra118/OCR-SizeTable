# Selenium을 활용한 Crawling

## Setting

- selenium 설치

```bash
pip install selenium
```

- 사용할 브라우저별 Selenium 드라이버를 설치한다. 각 브라우저 버전을 확인해 거기에 맞는 드라이버를 설치(브라우저 옵션에서 도움말 탭 살펴보면 됨)
  - [Firefox ](<https://github.com/mozilla/geckodriver/releases>)
  - [Chrome](<https://sites.google.com/a/chromium.org/chromedriver/downloads>)

  ```python
  driver_path = './geckodriver.exe'
  browser = webdriver.Firefox(executable_path=driver_path)
  browser.get(__url__)
  
  webdriver_path = './chromedriver.exe'
  browser = webdriver.Chrome(executable_path=webdriver_path)
  browser.get(__url__)
  ```

## 전체화면 스크린샷

- 전체 페이지 길이를 가져옴

```python
js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

scrollheight = browser.execute_script(js)

```

- 페이지 zoom 조절

```python
zoom = 0.5
scrollheight = int(scrollheight * zoom)
```

- 스크롤하면서 list에 이미지 append

```python
browser.execute_script("window.scrollTo(0, %s);" % offset)
img = Image.open(BytesIO(browser.get_screenshot_as_png()))
offset += img.size[1]
```



- list의 이미지들 한줄로 붙여놓기

```python
screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
offset = 0
for img in slices:
    screenshot.paste(img, (0, offset))
    offset += img.size[1]
```

