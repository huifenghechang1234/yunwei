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
实现一个简易的 AI 绘图工具，可以通过文本生成图片
"""
import os
from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import Path
from pathlib import PurePosixPath
import requests
import dashscope

# 阿里SD，500张，用完需再申请https://help.aliyun.com/zh/dashscope/developer-reference/getting-started-with-stable-diffusion-models?spm=5176.28197632.0.0.97d87e06OPIVDX&disableWebsiteRedirect=true

dashscope.api_key = 'xxxx'


# model = "dashscope.ImageSynthesis.Models.wanx_v1"

# 指定图片所在目录和保存目录
save_dir = './tmp/'
# 创建保存目录
os.makedirs(save_dir, exist_ok=True)

def generate_and_save_images(prompt, n, size, save_path):
    rsp = dashscope.ImageSynthesis.call(model=dashscope.ImageSynthesis.Models.wanx_v1,
                                        prompt=prompt,
                                        n=n,
                                        size=size)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
        for result in rsp.output.results:
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            save_file_path = Path(save_path) / file_name
            with open(save_file_path, 'wb+') as f:
                f.write(requests.get(result.url).content)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    prompt = "a dog and a cat"
    n = 4
    size = '1024*1024'
    save_path = os.path.join(save_dir)
    generate_and_save_images(prompt, n, size, save_path)
