# 匯入模組
from datetime import date
from flask import Flask, request, abort
import json
import def_Netflix as d

# 匯入模組(LINE Bot)
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

# 記得修改env.json(要套用的LINE Bot API)
with open("env.json") as f:
    env = json.load(f)

# 取得資訊(LINE Bot)
line_bot_api = LineBotApi(env["YOUR_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(env["YOUR_CHANNEL_SECRET"])

# ------------------------------------------------------------------

app = Flask(__name__)

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    except Exception as e:
        print("Error occurred while handling webhook: ", e)
        abort(500)

    return "OK"

# 訊息傳遞區塊(根據訊息內容，做處理)

# 告訴LINE Bot，當使用者輸入訊息，且訊息是文字時，我們就執行以下的程式碼
@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    message = event.message.text

    if event.message.text == "Netflix 台灣 新片":

        # 製作【Netflix_New】Bubble
        flex_message = d.Netflix_New()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )

    elif event.message.text == "Netflix 台灣 新片(含簡介) --- 1-20":

        # 確認是否有今日的【Netflix_New_info_txt】檔案
        d.check_file_Netflix_New_info_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_New_info_{now_date}_1_20.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        flex_message = d.Netflix_New_info_page_2_3()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, flex_message]
        )

    elif event.message.text == "Netflix 台灣 新片(含簡介) --- 21-40":

        # 確認是否有今日的【Netflix_New_info_txt】檔案
        d.check_file_Netflix_New_info_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_New_info_{now_date}_21_40.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        flex_message = d.Netflix_New_info_page_1_3()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, flex_message]
        )

    elif event.message.text == "Netflix 台灣 新片(含簡介) --- 41-60":

        # 確認是否有今日的【Netflix_New_info_txt】檔案
        d.check_file_Netflix_New_info_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_New_info_{now_date}_41_60.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        flex_message = d.Netflix_New_info_page_1_2()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, flex_message]
        )

    elif event.message.text == "Netflix 台灣 新片(不含簡介) --- 1-20":

        # 確認是否有今日的【Netflix_New_txt】檔案
        d.check_file_Netflix_New_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_New_{now_date}_1_20.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        flex_message = d.Netflix_New_page_2_3()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, flex_message]
        )

    elif event.message.text == "Netflix 台灣 新片(不含簡介) --- 21-40":

        # 確認是否有今日的【Netflix_New_txt】檔案
        d.check_file_Netflix_New_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_New_{now_date}_21_40.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        flex_message = d.Netflix_New_page_1_3()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, flex_message]
        )

    elif event.message.text == "Netflix 台灣 新片(不含簡介) --- 41-60":

        # 確認是否有今日的【Netflix_New_txt】檔案
        d.check_file_Netflix_New_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_New_{now_date}_41_60.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        flex_message = d.Netflix_New_page_1_2()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, flex_message]
        )

    elif event.message.text == "Netflix 台灣 Top 10 電影":

        # 製作【Netflix_TW_Top10_film】Bubble
        flex_message = d.Netflix_TW_Top10_film()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )

    elif event.message.text == "Netflix 台灣 Top 10 電影 (含簡介)":

        # 確認是否有今日的【Netflix_TW_Top10_film_info_txt】檔案
        d.check_file_Netflix_TW_Top10_film_info_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_TW_Top10_film_info_{now_date}.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            text_message
        )

    elif event.message.text == "Netflix 台灣 Top 10 電影 (不含簡介)":

        # 確認是否有今日的【Netflix_TW_Top10_film_txt】檔案
        d.check_file_Netflix_TW_Top10_film_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_TW_Top10_film_{now_date}.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            text_message
        )

    elif event.message.text == "Netflix 台灣 Top 10 節目":

        # 製作【Netflix_TW_Top10_TV】Bubble
        flex_message = d.Netflix_TW_Top10_TV()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )

    elif event.message.text == "Netflix 台灣 Top 10 節目 (含簡介)":

        # 確認是否有今日的【Netflix_TW_Top10_TV_info_txt】檔案
        d.check_file_Netflix_TW_Top10_TV_info_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_TW_Top10_TV_info_{now_date}.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            text_message
        )

    elif event.message.text == "Netflix 台灣 Top 10 節目 (不含簡介)":

        # 確認是否有今日的【Netflix_TW_Top10_TV_txt】檔案
        d.check_file_Netflix_TW_Top10_TV_txt()

        # 取得今日日期
        now_date = date.today().strftime("%Y%m%d")

        # 設定讀取檔案路徑
        file_path = f"Netflix_TW_Top10_TV_{now_date}.txt"

        # 讀取檔案
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            stored_message = f.read()

        text_message = TextSendMessage(stored_message)

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            text_message
        )

    elif event.message.text == "查詢":

        # 製作【指令】Bubble
        flex_message = d.code_list()

        # 使用LINE API
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )

    # 輸入內容，機器人就會原封不動的回傳給一模一樣的內容
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(message))

if __name__ == "__main__":
    app.run()
