# 匯入模組
from bs4 import BeautifulSoup
from datetime import date
import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 匯入模組(LINE Bot)
from linebot.models import *

# 換頁(位在無簡介1-20)
def Netflix_New_page_2_3():
    flex_message = FlexSendMessage(
        alt_text='檢視更多 Netflix 台灣 新片資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "檢視更多 Netflix 台灣 新片資訊",
                        "size": "lg",
                        "weight": "bold"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "21 - 40",
                            "text": "Netflix 台灣 新片(不含簡介) --- 21-40"
                        },
                        "color": "#E50914"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "41 - 60",
                            "text": "Netflix 台灣 新片(不含簡介) --- 41-60"
                        },
                        "color": "#E50914"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_message

# 換頁(位在無簡介21-40)
def Netflix_New_page_1_3():
    flex_message = FlexSendMessage(
        alt_text='檢視更多 Netflix 台灣 新片資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "檢視更多 Netflix 台灣 新片資訊",
                        "size": "lg",
                        "weight": "bold"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "1 - 20",
                            "text": "Netflix 台灣 新片(不含簡介) --- 1-20"
                        },
                        "color": "#E50914"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "41 - 60",
                            "text": "Netflix 台灣 新片(不含簡介) --- 41-60"
                        },
                        "color": "#E50914"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_message

# 換頁(位在無簡介41-60)
def Netflix_New_page_1_2():
    flex_message = FlexSendMessage(
        alt_text='檢視更多 Netflix 台灣 新片資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "檢視更多 Netflix 台灣 新片資訊",
                        "size": "lg",
                        "weight": "bold"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "1 - 20",
                            "text": "Netflix 台灣 新片(不含簡介) --- 1-20"
                        },
                        "color": "#E50914"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "21 - 40",
                            "text": "Netflix 台灣 新片(不含簡介) --- 21-40"
                        },
                        "color": "#E50914"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_message

# ----------------------------------------------------------------

# 換頁(位在有簡介1-20)
def Netflix_New_info_page_2_3():
    flex_message = FlexSendMessage(
        alt_text='檢視更多 Netflix 台灣 新片資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "檢視更多 Netflix 台灣 新片資訊",
                        "size": "lg",
                        "weight": "bold"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "21 - 40",
                            "text": "Netflix 台灣 新片(含簡介) --- 21-40"
                        },
                        "color": "#E50914"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "41 - 60",
                            "text": "Netflix 台灣 新片(含簡介) --- 41-60"
                        },
                        "color": "#E50914"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_message

# 換頁(位在有簡介21-40)
def Netflix_New_info_page_1_3():
    flex_message = FlexSendMessage(
        alt_text='檢視更多 Netflix 台灣 新片資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "檢視更多 Netflix 台灣 新片資訊",
                        "size": "lg",
                        "weight": "bold"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "1 - 20",
                            "text": "Netflix 台灣 新片(含簡介) --- 1-20"
                        },
                        "color": "#E50914"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "41 - 60",
                            "text": "Netflix 台灣 新片(含簡介) --- 41-60"
                        },
                        "color": "#E50914"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_message

# 換頁(位在有簡介41-60)
def Netflix_New_info_page_1_2():
    flex_message = FlexSendMessage(
        alt_text='檢視更多 Netflix 台灣 新片資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "檢視更多 Netflix 台灣 新片資訊",
                        "size": "lg",
                        "weight": "bold"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "1 - 20",
                            "text": "Netflix 台灣 新片(含簡介) --- 1-20"
                        },
                        "color": "#E50914"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "21 - 40",
                            "text": "Netflix 台灣 新片(含簡介) --- 21-40"
                        },
                        "color": "#E50914"
                    }
                ],
                "flex": 0
            }
        }
    )
    return flex_message

# ----------------------------------------------------------------

# 製作【Netflix_New】bubble
def Netflix_New():
    flex_message = FlexSendMessage(
        alt_text = 'Netflix 台灣 新片清單',
        contents = {
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/Uw0Pd54.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "新片清單",
                        "weight": "bold",
                        "size": "xxl",
                        "align": "center"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "含影片簡介",
                            "text": "Netflix 台灣 新片(含簡介) --- 1-20"
                        },
                        "color": "#e50914",
                        "height": "sm",
                        "offsetBottom": "md"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "不含影片簡介",
                            "text": "Netflix 台灣 新片(不含簡介) --- 1-20"
                        },
                        "color": "#e50914",
                        "margin": "md",
                        "height": "sm",
                        "offsetBottom": "md"
                    },
                    {
                        "type": "text",
                        "text": "以上資訊之帳戶所在國家/地區為【台灣】",
                        "align": "center",
                        "size": "xs",
                        "color": "#8a8f96",
                        "margin": "lg"
                    }
                ]
            }
        }
    )
    return flex_message

# ----------------------------------------------------------------

# 確認是否有今日的【Netflix_New_txt】檔案
def check_file_Netflix_New_txt():

    # 取得今日時間
    today = date.today()

    # 指定檔名
    filename = f"Netflix_New_{today.strftime('%Y%m%d')}.txt"

    # 如果指定檔不存在
    if not os.path.isfile(filename):
        # 製作檔案
        Netflix_New_txt()

    # 如果指定檔存在
    else:
        # 印出確認文字
        text = f'無須更新 Netflix_New_{today.strftime("%Y%m%d")}.txt'
        print(text)

# 製作【Netflix_New_txt】檔案
def Netflix_New_txt():

    # 設定Chrome Driver的執行檔路徑
    options = Options()
    options.chrome_executable_path = 'chromedriver.exe'

    # 建立Driver物件實體，用程式操作瀏覽器運作
    driver = webdriver.Chrome(options=options)

    url = "https://about.netflix.com/zh_tw/new-to-watch"
    driver.get(url)

    # 等待後取得第一頁html
    time.sleep(2)
    page1 = driver.page_source

    # 捲動視窗到下一頁按鈕
    driver.execute_script('window.scrollTo(0, 4000);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 6000);')
    time.sleep(2)

    # 找到指定元素(下一頁按鈕)
    turn_page = driver.find_element(By.CSS_SELECTOR,
                                    '#main-content > div.paginationstyles__PaginationWrapper-sc-1ma3op1-0.eapWyF > nav > ul > li:nth-child(2) > button')
    # 模擬使用者點擊下一頁標籤
    turn_page.click()

    # 等待後取得第二頁html
    time.sleep(2)
    page2 = driver.page_source

    # 捲動視窗到下一頁按鈕
    driver.execute_script('window.scrollTo(0, 4000);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 6000);')
    time.sleep(2)

    # 找到指定元素(下一頁按鈕)
    turn_page = driver.find_element(By.CSS_SELECTOR,
                                    '#main-content > div.paginationstyles__PaginationWrapper-sc-1ma3op1-0.eapWyF > nav > ul > li:nth-child(3) > button')
    # 模擬使用者點擊下一頁標籤
    turn_page.click()

    # 等待後取得第三頁html
    time.sleep(2)
    page3 = driver.page_source

    # 合併三頁html
    page_all = page1 + page2 + page3

    # 關閉瀏覽器視窗
    driver.close()

    # 進行解析
    soup = BeautifulSoup(page_all, 'html.parser')

    # ---------------取得【網址】---------------

    links = soup.find_all('a', class_='link__StyledAnchor-sc-1gds0w3-0 cGrGmh')

    link_list = []

    for t in links:
        link = t.get('href')
        link = link.replace("watch", "tw/title")  # 需特別調整網址
        link_list.append(link)

    # 保留的目標內容
    target_text = 'https://www.netflix.com/tw/title/'

    # 取得清單中符合條件的元素索引值
    indices_to_keep = find_indices_with_text(link_list, target_text)

    # 保留清單中指定索引值的元素
    link_list = keep_elements_at_indices(link_list, indices_to_keep)

    # ---------------取得【片名】---------------

    title_list = []
    for t in links:
        title = t.get('aria-label')
        title_list.append(title)

    # 保留清單中指定索引值的元素
    title_list = keep_elements_at_indices(title_list, indices_to_keep)

    # ---------------取得【上線日期】---------------

    online_date_list = []

    online_dates = soup.find_all('p', class_='release-schedule-grid-cardstyles__DateText-sc-15f8nyv-2 dJFmAg')

    for o in online_dates:
        online_date = o.text
        online_date_list.append(online_date)

    # ---------------取得【更細節資訊】---------------

    Netflix_New = []

    for i in range(len(link_list)):

        # 建立請求的URL(=欲爬取網站)
        url = link_list[i]

        # 設定請求標頭(模擬正常的瀏覽器行為)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

        # 發送請求並獲取回應
        res = requests.get(url, headers=headers)

        # 設定編碼(防止中文亂碼)
        res.encoding = "utf-8"

        # 對獲取到的HTML內容進行解析
        soup = BeautifulSoup(res.content, "html.parser")

        # -------------------------------------------------------------------------------

        # 年分
        year = soup.find('span', class_='title-info-metadata-item item-year')
        if year is None:
            # 取得今日時間
            today = date.today()
            year = today.year
        else:
            year = year.text

        # 年齡限制
        maturity_number = soup.find('span', class_='maturity-number')
        if maturity_number is None:
            maturity_number = ''
        else:
            maturity_number = maturity_number.text

        # 片長
        duration = soup.find('span', class_='duration')
        if duration is None:
            duration = ''
        else:
            duration = duration.text

        # 類別
        genre = soup.find_all('span', class_='more-details-item item-genres')  # 從html取出
        genre = [g.text for g in genre]  # 逐一取出
        genre = ''.join(genre)  # 合併多個
        if genre is None:
            genre = ''

        # 簡介
        info = soup.find('div', class_='title-info-synopsis')
        if info is None:
            info = ''
        else:
            info = info.text

        # 主演
        info_starring = soup.find('span', class_='title-data-info-item-list')
        # 如果有資料
        if info_starring is None:
            info_starring = ''
        else:
            info_starring = info_starring.text

        # 性質
        mood = soup.find_all('span', class_='more-details-item item-mood-tag')
        mood = [m.text for m in mood]  # 逐一取出
        mood = ''.join(mood)  # 合併多個

        Netflix_New_ele = {
            '片名': title_list[i],
            '網址': link_list[i],
            '年份': year,
            '片長': duration,
            '年齡層': maturity_number,
            '類別': genre,
            '簡介': info,
            '主演': info_starring,
            '性質': mood,
            '上線日期': online_date_list[i]
        }

        Netflix_New.append(Netflix_New_ele)

    # -----------------------整理資料合併-----------------------

    message_all = f'☆☆☆ Netflix 新片 ☆☆☆\n\n'

    for i in range(len(link_list)):
        # 無簡介
        message = f"======== {i + 1} ======== \n\n({Netflix_New[i]['年份']}) {Netflix_New[i]['片名']} \n{Netflix_New[i]['網址']} \n上線：{Netflix_New[i]['上線日期']} \n類型：{Netflix_New[i]['類別']} \n\n"
        message_all += message

    # -----------------------儲存為txt-----------------------

    # 取得今日日期
    now_date = date.today().strftime("%Y%m%d")

    # 設定另存檔案路徑
    file_path = f"Netflix_New_{now_date}.txt"

    # 將訊息存入txt
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(message_all)

    text = f"已完成 Netflix_New_{now_date}.txt"
    print(text)

    # -----------------------拆分txt-----------------------

    # 設定讀取檔案路徑
    file_path = f"Netflix_New_{now_date}.txt"

    # 讀取檔案
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()

    # --------------------進行拆分txt--------------------

    parts = data.split('======== 21 ========')
    part_1_20 = parts[0]
    data = '☆☆☆ Netflix 新片 ☆☆☆\n\n======== 21 ========' + parts[1]

    parts = data.split('======== 41 ========')
    part_21_40 = parts[0]
    part_41_60 = '☆☆☆ Netflix 新片 ☆☆☆\n\n======== 41 ========' + parts[1]

    # --------------------拆分後儲存txt--------------------

    for start, end in [(1, 20), (21, 40), (41, 60)]:

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定另存檔案路徑
        file_path = f"Netflix_New_{now_date}_{start}_{end}.txt"

        # 取得對應的 part 變數
        part_var_name = f"part_{start}_{end}"
        part = locals()[part_var_name]

        # 將訊息存入txt
        with open(file_path, 'w', encoding='utf-8-sig') as f:
            f.write(part)

        text = f"已完成 Netflix_New_{now_date}_{start}_{end}.txt"
        print(text)

# ----------------------------------------------------------------

# 確認是否有今日的【Netflix_New_info_txt】檔案
def check_file_Netflix_New_info_txt():

    # 取得今日時間
    today = date.today()

    # 指定檔名
    filename = f"Netflix_New_info_{today.strftime('%Y%m%d')}.txt"

    # 如果指定檔不存在
    if not os.path.isfile(filename):
        # 製作檔案
        Netflix_New_info_txt()

    # 如果指定檔存在
    else:
        # 印出確認文字
        text = f"無須更新 Netflix_New_info_{today.strftime('%Y%m%d')}.txt"
        print(text)

# 製作【Netflix_New_info_txt】檔案
def Netflix_New_info_txt():

    # 設定Chrome Driver的執行檔路徑
    options = Options()
    options.chrome_executable_path = 'chromedriver.exe'

    # 建立Driver物件實體，用程式操作瀏覽器運作
    driver = webdriver.Chrome(options=options)

    url = "http://about.netflix.com/zh_tw/new-to-watch"
    driver.get(url)

    # 等待後取得第一頁html
    time.sleep(2)
    page1 = driver.page_source

    # 捲動視窗到下一頁按鈕
    driver.execute_script('window.scrollTo(0, 4000);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 6000);')
    time.sleep(2)

    # 找到指定元素(下一頁按鈕)
    turn_page = driver.find_element(By.CSS_SELECTOR,
                                    '#main-content > div.paginationstyles__PaginationWrapper-sc-1ma3op1-0.eapWyF > nav > ul > li:nth-child(2) > button')
    # 模擬使用者點擊下一頁標籤
    turn_page.click()

    # 等待後取得第二頁html
    time.sleep(2)
    page2 = driver.page_source

    # 捲動視窗到下一頁按鈕
    driver.execute_script('window.scrollTo(0, 4000);')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 6000);')
    time.sleep(2)

    # 找到指定元素(下一頁按鈕)
    turn_page = driver.find_element(By.CSS_SELECTOR,
                                    '#main-content > div.paginationstyles__PaginationWrapper-sc-1ma3op1-0.eapWyF > nav > ul > li:nth-child(3) > button')
    # 模擬使用者點擊下一頁標籤
    turn_page.click()

    # 等待後取得第三頁html
    time.sleep(2)
    page3 = driver.page_source

    # 合併三頁html
    page_all = page1 + page2 + page3

    # 關閉瀏覽器視窗
    driver.close()

    # 進行解析
    soup = BeautifulSoup(page_all, 'html.parser')

    # ---------------取得【網址】---------------

    links = soup.find_all('a', class_='link__StyledAnchor-sc-1gds0w3-0 cGrGmh')

    link_list = []

    for t in links:
        link = t.get('href')
        link = link.replace("watch", "tw/title")  # 需特別調整網址
        link_list.append(link)

    # 保留的目標內容
    target_text = 'https://www.netflix.com/tw/title/'

    # 取得清單中符合條件的元素索引值
    indices_to_keep = find_indices_with_text(link_list, target_text)

    # 保留清單中指定索引值的元素
    link_list = keep_elements_at_indices(link_list, indices_to_keep)

    # ---------------取得【片名】---------------

    title_list = []
    for t in links:
        title = t.get('aria-label')
        title_list.append(title)

    # 保留清單中指定索引值的元素
    title_list = keep_elements_at_indices(title_list, indices_to_keep)

    # ---------------取得【上線日期】---------------

    online_date_list = []

    online_dates = soup.find_all('p', class_='release-schedule-grid-cardstyles__DateText-sc-15f8nyv-2 dJFmAg')

    for o in online_dates:
        online_date = o.text
        online_date_list.append(online_date)

    # ---------------取得【更細節資訊】---------------

    Netflix_New = []

    for i in range(len(link_list)):

        # 建立請求的URL(=欲爬取網站)
        url = link_list[i]

        # 設定請求標頭(模擬正常的瀏覽器行為)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

        # 發送請求並獲取回應
        res = requests.get(url, headers=headers)

        # 設定編碼(防止中文亂碼)
        res.encoding = "utf-8"

        # 對獲取到的HTML內容進行解析
        soup = BeautifulSoup(res.content, "html.parser")

        # -------------------------------------------------------------------------------

        # 年分
        year = soup.find('span', class_='title-info-metadata-item item-year')
        if year is None:
            # 取得今日時間
            today = date.today()
            year = today.year
        else:
            year = year.text

        # 年齡限制
        maturity_number = soup.find('span', class_='maturity-number')
        if maturity_number is None:
            maturity_number = ''
        else:
            maturity_number = maturity_number.text

        # 片長
        duration = soup.find('span', class_='duration')
        if duration is None:
            duration = ''
        else:
            duration = duration.text

        # 類別
        genre = soup.find_all('span', class_='more-details-item item-genres')  # 從html取出
        genre = [g.text for g in genre]  # 逐一取出
        genre = ''.join(genre)  # 合併多個
        if genre is None:
            genre = ''

        # 簡介
        info = soup.find('div', class_='title-info-synopsis')
        if info is None:
            info = ''
        else:
            info = info.text

        # 主演
        info_starring = soup.find('span', class_='title-data-info-item-list')
        # 如果有資料
        if info_starring is None:
            info_starring = ''
        else:
            info_starring = info_starring.text

        # 性質
        mood = soup.find_all('span', class_='more-details-item item-mood-tag')
        mood = [m.text for m in mood]  # 逐一取出
        mood = ''.join(mood)  # 合併多個

        Netflix_New_ele = {

            '片名': title_list[i],
            '網址': link_list[i],
            '年份': year,
            '片長': duration,
            '年齡層': maturity_number,
            '類別': genre,
            '簡介': info,
            '主演': info_starring,
            '性質': mood,
            '上線日期': online_date_list[i]
        }

        Netflix_New.append(Netflix_New_ele)

    # -----------------------整理資料合併-----------------------

    message_all = f'☆☆☆ Netflix 新片 ☆☆☆\n\n'

    for i in range(len(link_list)):
        # 有簡介
        message = f"======== {i + 1} ======== \n\n({Netflix_New[i]['年份']}) {Netflix_New[i]['片名']} \n{Netflix_New[i]['網址']} \n上線：{Netflix_New[i]['上線日期']} \n類型：{Netflix_New[i]['類別']} \n簡介：{Netflix_New[i]['簡介']} \n\n"
        message_all += message

    # -----------------------儲存為txt-----------------------

    # 取得今日日期
    now_date = date.today().strftime("%Y%m%d")

    # 設定另存檔案路徑
    file_path = f"Netflix_New_info_{now_date}.txt"

    # 將訊息存入txt
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(message_all)

    text = f"已完成 Netflix_New_info_{now_date}.txt"
    print(text)

    # -----------------------拆分txt-----------------------

    # 設定讀取檔案路徑
    file_path = f"Netflix_New_info_{now_date}.txt"

    # 讀取檔案
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()

    # -----------------------進行拆分-----------------------

    parts = data.split('======== 21 ========')
    part_1_20 = parts[0]
    data = '☆☆☆ Netflix 新片 ☆☆☆\n\n======== 21 ========' + parts[1]

    parts = data.split('======== 41 ========')
    part_21_40 = parts[0]
    part_41_60 = '☆☆☆ Netflix 新片 ☆☆☆\n\n======== 41 ========' + parts[1]

    # --------------------拆分後儲存txt--------------------

    for start, end in [(1, 20), (21, 40), (41, 60)]:
        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定另存檔案路徑
        file_path = f"Netflix_New_info_{now_date}_{start}_{end}.txt"

        # 取得對應的 part 變數
        part_var_name = f"part_{start}_{end}"
        part = locals()[part_var_name]

        # 將訊息存入txt
        with open(file_path, 'w', encoding='utf-8-sig') as f:
            f.write(part)

        text = f"已完成 Netflix_New_info_{now_date}_{start}_{end}.txt"
        print(text)

# ----------------------------------------------------------------

# 取得清單中符合條件的元素索引值
def find_indices_with_text(list, target_text):

    indices = []
    for index, item in enumerate(list):
        if target_text in item:
            indices.append(index)
    return indices

# 保留清單中指定索引值的元素
def keep_elements_at_indices(list, indices_to_keep):

    list = [list[index] for index in indices_to_keep]
    return list

# ----------------------------------------------------------------

# 製作【Netflix_TW_Top10_film】bubble
def Netflix_TW_Top10_film():

    flex_message = FlexSendMessage(
        alt_text = 'Netflix 台灣 Top 10 電影',
        contents = {
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/Uw0Pd54.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Top 10 電影",
                        "weight": "bold",
                        "size": "xxl",
                        "align": "center"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "含影片簡介",
                            "text": "Netflix 台灣 Top 10 電影 (含簡介)"
                        },
                        "color": "#e50914",
                        "height": "sm",
                        "offsetBottom": "md"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "不含影片簡介",
                            "text": "Netflix 台灣 Top 10 電影 (不含簡介)"
                        },
                        "color": "#e50914",
                        "margin": "md",
                        "height": "sm",
                        "offsetBottom": "md"
                    },
                    {
                        "type": "text",
                        "text": "以上資訊之帳戶所在國家/地區為【台灣】",
                        "align": "center",
                        "size": "xs",
                        "color": "#8a8f96",
                        "margin": "lg"
                    }
                ]
            }
        }
    )
    return flex_message

# ----------------------------------------------------------------

# 確認是否有今日的【Netflix_TW_Top10_film_txt】檔案
def check_file_Netflix_TW_Top10_film_txt():

    # 取得今日時間
    today = date.today()

    # 指定檔名
    filename = f"Netflix_TW_Top10_film_{today.strftime('%Y%m%d')}.txt"

    # 如果指定檔不存在
    if not os.path.isfile(filename):
        # 製作檔案
        Netflix_TW_Top10_film_txt()

    # 如果指定檔存在
    else:
        # 印出確認文字
        text = f"無須更新 Netflix_TW_Top10_film_{today.strftime('%Y%m%d')}.txt"
        print(text)

# 製作【Netflix_TW_Top10_film_txt】檔案
def Netflix_TW_Top10_film_txt():

    # 建立請求的URL(=欲爬取網站)
    url = 'https://www.netflix.com/tudum/top10/taiwan'

    # 設定請求標頭(模擬正常的瀏覽器行為)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }

    # 發送請求並獲取回應
    res = requests.get(url, headers=headers)

    # 對獲取到的HTML內容進行解析
    soup = BeautifulSoup(res.text, 'html.parser')

    # --------------取得【網址】--------------

    links = soup.find_all('a', class_='block text-13px md:text-18px whitespace-nowrap hover:text-white')

    link_list = []

    for l in links:
        link = l.get('href')
        link = link.replace('title', 'tw/title')
        link_list.append(link)

    # --------------取得【各項資訊】--------------

    Netflix_New = []

    for link in link_list:

        # 建立請求的URL(=欲爬取網站)
        url = link

        # 設定請求標頭(模擬正常的瀏覽器行為)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

        # 發送請求並獲取回應
        res = requests.get(url, headers=headers)

        # 對獲取到的HTML內容進行解析
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.find('h1', class_='title-title')
        if title is None:
            title = ''
        else:
            title = title.text

        # 年分
        year = soup.find('span', class_='title-info-metadata-item item-year')
        if year is None:
            # 取得今日時間
            today = date.today()
            year = today.year
        else:
            year = year.text

        # 年齡限制
        maturity_number = soup.find('span', class_='maturity-number')
        if maturity_number is None:
            maturity_number = ''
        else:
            maturity_number = maturity_number.text

        # 片長
        duration = soup.find('span', class_='duration')
        if duration is None:
            duration = ''
        else:
            duration = duration.text

        # 類別
        genre = soup.find_all('span', class_='more-details-item item-genres')  # 從html取出
        genre = [g.text for g in genre]  # 逐一取出
        genre = ''.join(genre)  # 合併多個
        if genre is None:
            genre = ''

        # 簡介
        info = soup.find('div', class_='title-info-synopsis')
        if info is None:
            info = ''
        else:
            info = info.text

        # 主演
        info_starring = soup.find('span', class_='title-data-info-item-list')
        # 如果有資料
        if info_starring is None:
            info_starring = ''
        else:
            info_starring = info_starring.text

        # 性質
        mood = soup.find_all('span', class_='more-details-item item-mood-tag')
        mood = [m.text for m in mood]  # 逐一取出
        mood = ''.join(mood)  # 合併多個

        Netflix_New_ele = {
            '片名': title,
            '網址': link,
            '年份': year,
            '片長': duration,
            '年齡層': maturity_number,
            '類別': genre,
            '簡介': info,
            '主演': info_starring,
            '性質': mood
        }

        Netflix_New.append(Netflix_New_ele)

    # -----------------------整理資料合併-----------------------

    message_all = f'☆☆☆ Netflix 台灣 Top 10 電影 ☆☆☆\n\n'

    for i in range(len(link_list)):
        # 沒有簡介
        message = f"======== 第 {i + 1} 名 ======== \n\n({Netflix_New[i]['年份']}) {Netflix_New[i]['片名']} \n{Netflix_New[i]['網址']} \n類型：{Netflix_New[i]['類別']} \n\n"
        message_all += message

    # -----------------------儲存為txt-----------------------

    # 取得今日日期
    now_date = date.today().strftime("%Y%m%d")

    # 設定另存檔案路徑
    file_path = f"Netflix_TW_Top10_film_{now_date}.txt"

    # 將訊息存入txt
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(message_all)

    text = f"已完成 Netflix_TW_Top10_film_{now_date}.txt"
    print(text)

# ----------------------------------------------------------------

# 確認是否有今日的【Netflix_TW_Top10_film_info_txt】檔案
def check_file_Netflix_TW_Top10_film_info_txt():

    # 取得今日時間
    today = date.today()

    # 指定檔名
    filename = f"Netflix_TW_Top10_film_info_{today.strftime('%Y%m%d')}.txt"

    # 如果指定檔不存在
    if not os.path.isfile(filename):
        # 製作檔案
        Netflix_TW_Top10_film_info_txt()

    # 如果指定檔存在
    else:
        # 印出確認文字
        text = f"無須更新 Netflix_TW_Top10_film_info_{today.strftime('%Y%m%d')}.txt"
        print(text)

# 製作【Netflix_TW_Top10_film_info_txt】檔案
def Netflix_TW_Top10_film_info_txt():

    # 建立請求的URL(=欲爬取網站)
    url = 'https://www.netflix.com/tudum/top10/taiwan'

    # 設定請求標頭(模擬正常的瀏覽器行為)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }

    # 發送請求並獲取回應
    res = requests.get(url, headers=headers)

    # 對獲取到的HTML內容進行解析
    soup = BeautifulSoup(res.text, 'html.parser')

    # --------------取得【網址】--------------
    links = soup.find_all('a', class_='block text-13px md:text-18px whitespace-nowrap hover:text-white')

    link_list = []

    for l in links:
        link = l.get('href')
        link = link.replace('title', 'tw/title')
        link_list.append(link)

    # --------------取得【各項資訊】--------------

    Netflix_New = []

    for link in link_list:

        # 建立請求的URL(=欲爬取網站)
        url = link

        # 設定請求標頭(模擬正常的瀏覽器行為)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

        # 發送請求並獲取回應
        res = requests.get(url, headers=headers)

        # 對獲取到的HTML內容進行解析
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.find('h1', class_='title-title')
        if title is None:
            title = ''
        else:
            title = title.text

        # 年分
        year = soup.find('span', class_='title-info-metadata-item item-year')
        if year is None:
            # 取得今日時間
            today = date.today()
            year = today.year
        else:
            year = year.text

        # 年齡限制
        maturity_number = soup.find('span', class_='maturity-number')
        if maturity_number is None:
            maturity_number = ''
        else:
            maturity_number = maturity_number.text

        # 片長
        duration = soup.find('span', class_='duration')
        if duration is None:
            duration = ''
        else:
            duration = duration.text

        # 類別
        genre = soup.find_all('span', class_='more-details-item item-genres')  # 從html取出
        genre = [g.text for g in genre]  # 逐一取出
        genre = ''.join(genre)  # 合併多個
        if genre is None:
            genre = ''

        # 簡介
        info = soup.find('div', class_='title-info-synopsis')
        if info is None:
            info = ''
        else:
            info = info.text

        # 主演
        info_starring = soup.find('span', class_='title-data-info-item-list')
        # 如果有資料
        if info_starring is None:
            info_starring = ''
        else:
            info_starring = info_starring.text

        # 性質
        mood = soup.find_all('span', class_='more-details-item item-mood-tag')
        mood = [m.text for m in mood]  # 逐一取出
        mood = ''.join(mood)  # 合併多個

        Netflix_New_ele = {
            '片名': title,
            '網址': link,
            '年份': year,
            '片長': duration,
            '年齡層': maturity_number,
            '類別': genre,
            '簡介': info,
            '主演': info_starring,
            '性質': mood
        }

        Netflix_New.append(Netflix_New_ele)

    # -----------------------整理資料合併-----------------------

    message_all = f'☆☆☆ Netflix 台灣 Top 10 電影 ☆☆☆\n\n'

    for i in range(len(link_list)):
        # 有簡介
        message = f"======== 第 {i + 1} 名 ======== \n\n({Netflix_New[i]['年份']}) {Netflix_New[i]['片名']} \n{Netflix_New[i]['網址']} \n類型：{Netflix_New[i]['類別']} \n簡介：{Netflix_New[i]['簡介']} \n\n"
        message_all += message

    # -----------------------儲存為txt-----------------------

    # 取得今日日期
    now_date = date.today().strftime("%Y%m%d")

    # 設定另存檔案路徑
    file_path = f"Netflix_TW_Top10_film_info_{now_date}.txt"

    # 將訊息存入txt
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(message_all)

    text = f"已完成 Netflix_TW_Top10_film_info_{now_date}.txt"
    print(text)

# ---------------------------------------------------------------

# 製作【Netflix_TW_Top10_TV】bubble
def Netflix_TW_Top10_TV():
    flex_message = FlexSendMessage(
        alt_text = 'Netflix 台灣 Top 10 節目',
        contents = {
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/Uw0Pd54.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "Top 10 節目",
                        "weight": "bold",
                        "size": "xxl",
                        "align": "center"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "含影片簡介",
                            "text": "Netflix 台灣 Top 10 節目 (含簡介)"
                        },
                        "color": "#e50914",
                        "height": "sm",
                        "offsetBottom": "md"
                    },
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                            "type": "message",
                            "label": "不含影片簡介",
                            "text": "Netflix 台灣 Top 10 節目 (不含簡介)"
                        },
                        "color": "#e50914",
                        "margin": "md",
                        "height": "sm",
                        "offsetBottom": "md"
                    },
                    {
                        "type": "text",
                        "text": "以上資訊之帳戶所在國家/地區為【台灣】",
                        "align": "center",
                        "size": "xs",
                        "color": "#8a8f96",
                        "margin": "lg"
                    }
                ]
            }
        }
    )
    return flex_message

# ---------------------------------------------------------------

# 確認是否有今日的【Netflix_TW_Top10_TV_txt】檔案
def check_file_Netflix_TW_Top10_TV_txt():

    # 取得今日時間
    today = date.today()

    # 指定檔名
    filename = f"Netflix_TW_Top10_TV_{today.strftime('%Y%m%d')}.txt"

    # 如果指定檔不存在
    if not os.path.isfile(filename):
        # 製作檔案
        Netflix_TW_Top10_TV_txt()

    # 如果指定檔存在
    else:
        # 印出確認文字
        text = f"無須更新 Netflix_TW_Top10_TV_{today.strftime('%Y%m%d')}.txt"
        print(text)

# 製作【Netflix_TW_Top10_TV_txt】檔案
def Netflix_TW_Top10_TV_txt():

    # 建立請求的URL(=欲爬取網站)
    url = 'https://www.netflix.com/tudum/top10/taiwan/tv'

    # 設定請求標頭(模擬正常的瀏覽器行為)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }

    # 發送請求並獲取回應
    res = requests.get(url, headers=headers)

    # 對獲取到的HTML內容進行解析
    soup = BeautifulSoup(res.text, 'html.parser')

    # --------------取得【網址】--------------

    links = soup.find_all('a', class_='block text-13px md:text-18px whitespace-nowrap hover:text-white')

    link_list = []

    for l in links:
        link = l.get('href')
        link = link.replace('title', 'tw/title')
        link_list.append(link)

    # --------------取得【各項資訊】--------------

    Netflix_New = []

    for link in link_list:

        # 建立請求的URL(=欲爬取網站)
        url = link

        # 設定請求標頭(模擬正常的瀏覽器行為)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

        # 發送請求並獲取回應
        res = requests.get(url, headers=headers)

        # 對獲取到的HTML內容進行解析
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.find('h1', class_='title-title')
        if title is None:
            title = ''
        else:
            title = title.text

        # 年分
        year = soup.find('span', class_='title-info-metadata-item item-year')
        if year is None:
            # 取得今日時間
            today = date.today()
            year = today.year
        else:
            year = year.text

        # 年齡限制
        maturity_number = soup.find('span', class_='maturity-number')
        if maturity_number is None:
            maturity_number = ''
        else:
            maturity_number = maturity_number.text

        # 片長
        duration = soup.find('span', class_='duration')
        if duration is None:
            duration = ''
        else:
            duration = duration.text

        # 類別
        genre = soup.find_all('span', class_='more-details-item item-genres')  # 從html取出
        genre = [g.text for g in genre]  # 逐一取出
        genre = ''.join(genre)  # 合併多個
        if genre is None:
            genre = ''

        # 簡介
        info = soup.find('div', class_='title-info-synopsis')
        if info is None:
            info = ''
        else:
            info = info.text

        # 主演
        info_starring = soup.find('span', class_='title-data-info-item-list')
        # 如果有資料
        if info_starring is None:
            info_starring = ''
        else:
            info_starring = info_starring.text

        # 性質
        mood = soup.find_all('span', class_='more-details-item item-mood-tag')
        mood = [m.text for m in mood]  # 逐一取出
        mood = ''.join(mood)  # 合併多個

        Netflix_New_ele = {
            '片名': title,
            '網址': link,
            '年份': year,
            '片長': duration,
            '年齡層': maturity_number,
            '類別': genre,
            '簡介': info,
            '主演': info_starring,
            '性質': mood
        }

        Netflix_New.append(Netflix_New_ele)

    # -----------------------整理資料合併-----------------------

    message_all = f'☆☆☆ Netflix 台灣 Top 10 節目 ☆☆☆\n\n'

    for i in range(len(link_list)):
        # 沒有簡介
        message = f"======== 第 {i + 1} 名 ======== \n\n({Netflix_New[i]['年份']}) {Netflix_New[i]['片名']} \n{Netflix_New[i]['網址']} \n類型：{Netflix_New[i]['類別']} \n\n"
        message_all += message

    # -----------------------儲存為txt-----------------------

    # 取得今日日期
    now_date = date.today().strftime("%Y%m%d")

    # 設定另存檔案路徑
    file_path = f"Netflix_TW_Top10_TV_{now_date}.txt"

    # 將訊息存入txt
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(message_all)

    text = f"已完成 Netflix_TW_Top10_TV_{now_date}.txt"
    print(text)

# ---------------------------------------------------------------

# 確認是否有今日的【Netflix_TW_Top10_TV_info_txt】檔案
def check_file_Netflix_TW_Top10_TV_info_txt():

    # 取得今日時間
    today = date.today()

    # 指定檔名
    filename = f"Netflix_TW_Top10_TV_info_{today.strftime('%Y%m%d')}.txt"

    # 如果指定檔不存在
    if not os.path.isfile(filename):
        # 製作檔案
        Netflix_TW_Top10_TV_info_txt()

    # 如果指定檔存在
    else:
        # 印出確認文字
        text = f"無須更新 Netflix_TW_Top10_TV_info_{today.strftime('%Y%m%d')}.txt"
        print(text)

# 製作【Netflix_TW_Top10_TV_info_txt】檔案
def Netflix_TW_Top10_TV_info_txt():

    # 建立請求的URL(=欲爬取網站)
    url = 'https://www.netflix.com/tudum/top10/taiwan/tv'

    # 設定請求標頭(模擬正常的瀏覽器行為)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
    }

    # 發送請求並獲取回應
    res = requests.get(url, headers=headers)

    # 對獲取到的HTML內容進行解析
    soup = BeautifulSoup(res.text, 'html.parser')

    # --------------取得【網址】--------------
    links = soup.find_all('a', class_='block text-13px md:text-18px whitespace-nowrap hover:text-white')

    link_list = []

    for l in links:
        link = l.get('href')
        link = link.replace('title', 'tw/title')
        link_list.append(link)

    # --------------取得【各項資訊】--------------

    Netflix_New = []

    for link in link_list:

        # 建立請求的URL(=欲爬取網站)
        url = link

        # 設定請求標頭(模擬正常的瀏覽器行為)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
        }

        # 發送請求並獲取回應
        res = requests.get(url, headers=headers)

        # 對獲取到的HTML內容進行解析
        soup = BeautifulSoup(res.text, 'html.parser')

        title = soup.find('h1', class_='title-title')
        if title is None:
            title = ''
        else:
            title = title.text

        # 年分
        year = soup.find('span', class_='title-info-metadata-item item-year')
        if year is None:
            # 取得今日時間
            today = date.today()
            year = today.year
        else:
            year = year.text

        # 年齡限制
        maturity_number = soup.find('span', class_='maturity-number')
        if maturity_number is None:
            maturity_number = ''
        else:
            maturity_number = maturity_number.text

        # 片長
        duration = soup.find('span', class_='duration')
        if duration is None:
            duration = ''
        else:
            duration = duration.text

        # 類別
        genre = soup.find_all('span', class_='more-details-item item-genres')  # 從html取出
        genre = [g.text for g in genre]  # 逐一取出
        genre = ''.join(genre)  # 合併多個
        if genre is None:
            genre = ''

        # 簡介
        info = soup.find('div', class_='title-info-synopsis')
        if info is None:
            info = ''
        else:
            info = info.text

        # 主演
        info_starring = soup.find('span', class_='title-data-info-item-list')
        # 如果有資料
        if info_starring is None:
            info_starring = ''
        else:
            info_starring = info_starring.text

        # 性質
        mood = soup.find_all('span', class_='more-details-item item-mood-tag')
        mood = [m.text for m in mood]  # 逐一取出
        mood = ''.join(mood)  # 合併多個

        Netflix_New_ele = {
            '片名': title,
            '網址': link,
            '年份': year,
            '片長': duration,
            '年齡層': maturity_number,
            '類別': genre,
            '簡介': info,
            '主演': info_starring,
            '性質': mood
        }

        Netflix_New.append(Netflix_New_ele)

    # -----------------------整理資料合併-----------------------

    message_all = f'☆☆☆ Netflix 台灣 Top 10 節目 ☆☆☆\n\n'

    for i in range(len(link_list)):
        # 有簡介
        message = f"======== 第 {i + 1} 名 ======== \n\n({Netflix_New[i]['年份']}) {Netflix_New[i]['片名']} \n{Netflix_New[i]['網址']} \n類型：{Netflix_New[i]['類別']} \n簡介：{Netflix_New[i]['簡介']} \n\n"
        message_all += message

    # -----------------------儲存為txt-----------------------

    # 取得今日日期
    now_date = date.today().strftime("%Y%m%d")

    # 設定另存檔案路徑
    file_path = f"Netflix_TW_Top10_TV_info_{now_date}.txt"

    # 將訊息存入txt
    with open(file_path, 'w', encoding='utf-8-sig') as f:
        f.write(message_all)

    text = f"已完成 Netflix_TW_Top10_TV_info_{now_date}.txt"
    print(text)

# ---------------------------------------------------------------

# 查詢
def code_list():
    message = FlexSendMessage(
        alt_text = "Netflix 查詢",
        contents = {
  "type": "bubble",
  "size": "mega",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/Uw0Pd54.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "查詢",
        "weight": "bold",
        "size": "xxl",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "新片",
          "text": "Netflix 台灣 新片"
        },
        "color": "#e50914",
        "height": "sm",
        "offsetBottom": "md"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "Top 10 電影",
          "text": "Netflix 台灣 Top 10 電影"
        },
        "color": "#e50914",
        "margin": "md",
        "height": "sm",
        "offsetBottom": "md"
      },
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "Top 10 節目",
          "text": "Netflix 台灣 Top 10 節目"
        },
        "color": "#e50914",
        "margin": "md",
        "height": "sm",
        "offsetBottom": "md"
      },
      {
        "type": "text",
        "text": "以上資訊之帳戶所在國家/地區為【台灣】",
        "align": "center",
        "size": "xs",
        "color": "#8a8f96",
        "margin": "lg"
      }
    ]
  }
}
    )
    return message