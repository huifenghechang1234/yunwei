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
查询当天的天气，并打印在控制台
"""

import requests

def get_weather_info(city_code, user_key,extensions):
    """
    获取指定城市的天气信息

    Args:
    - city_code: 城市编码
    - user_key: 用户的 API 密钥

    Returns:
    - 天气信息的 JSON 数据
    """
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city_code}&key={user_key}&extensions={extensions}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve weather information.")
        return None


from colorama import Fore, Style

def print_weather_info_colorama(weather_info):
    """
    打印带有颜色的天气信息

    Args:
    - weather_info: 天气信息的 JSON 数据
    """
    if 'forecasts' in weather_info and len(weather_info['forecasts']) > 0:
        forecasts = weather_info['forecasts'][0]
        forecast = forecasts['casts'][0]
        print(Style.BRIGHT + "日期:" + Style.RESET_ALL, Fore.BLUE + forecast['date'] + Style.RESET_ALL)
        print(Style.BRIGHT + "星期:" + Style.RESET_ALL, Fore.BLUE + forecast['week'] + Style.RESET_ALL)
        print(Style.BRIGHT + "省份:" + Style.RESET_ALL, Fore.CYAN + forecasts['province'] + Style.RESET_ALL)
        print(Style.BRIGHT + "城市:" + Style.RESET_ALL, Fore.CYAN + forecasts['city'] + Style.RESET_ALL)
        print(Style.BRIGHT + "白天天气:" + Style.RESET_ALL, Fore.GREEN + forecast['dayweather'] + Style.RESET_ALL)
        print(Style.BRIGHT + "夜晚天气:" + Style.RESET_ALL, Fore.GREEN + forecast['nightweather'] + Style.RESET_ALL)
        print(Style.BRIGHT + "白天温度:" + Style.RESET_ALL, Fore.YELLOW + str(forecast['daytemp']) + "摄氏度" + Style.RESET_ALL)
        print(Style.BRIGHT + "夜晚温度:" + Style.RESET_ALL, Fore.YELLOW + str(forecast['nighttemp']) + "摄氏度" + Style.RESET_ALL)
        print(Style.BRIGHT + "白天风力:" + Style.RESET_ALL, Fore.LIGHTMAGENTA_EX + forecast['daypower'] + Style.RESET_ALL)
        print(Style.BRIGHT + "夜晚风力:" + Style.RESET_ALL, Fore.LIGHTMAGENTA_EX + forecast['nightpower'] + Style.RESET_ALL)
    else:
        print("未能获取到天气信息")


if __name__ == "__main__":
    # 用户的 API 密钥
    user_key = "xxxxxx"
    # 城市编码，例如广州天河区的编码为 440106
    city_code = "440106"
    # 详细信息
    extensions = 'all'
    # 调用函数获取天气信息
    weather_info = get_weather_info(city_code, user_key,extensions)
    print_weather_info_colorama(weather_info)