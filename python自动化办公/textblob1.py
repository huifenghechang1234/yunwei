"""
title = ''
author = 'huifenghechang'
mtime = '2024/4/22'
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""
"""
实现一个简易的文本情感分析系统
"""

from textblob import TextBlob
import requests
import random
from hashlib import md5

# Set your own appid/appkey.
appid = 'xxxxx'
appkey = 'xxxxxxx'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = 'auto'
to_lang = 'en'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def translate_text(query):
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    translations = [translation["dst"] for translation in result["trans_result"]]
    return translations


def analyze_sentiment(text):
    """分析情感倾向"""
    translations = translate_text(text)
    en_text = translations[0]
    if en_text:
        blob = TextBlob(en_text)
        sentiment = blob.sentiment

        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity

        if polarity > 0:
            result = 'positive'
        elif polarity < 0:
            result = 'negative'
        else:
            result = 'neutral'

        return result, polarity, subjectivity
    else:
        return None


if __name__ == '__main__':
    while True:
        input_text = input("请输入要分析的文本 (输入 'exit' 退出)：")
        if input_text.lower() == 'exit':
            print("感谢使用，再见！")
            break
        result = analyze_sentiment(input_text)
        if result:
            sentiment, polarity, subjectivity = result
            print(f"情感倾向: {sentiment}, 极性: {polarity}, 主观性: {subjectivity}")
        else:
            print("翻译失败，请稍后重试。")
