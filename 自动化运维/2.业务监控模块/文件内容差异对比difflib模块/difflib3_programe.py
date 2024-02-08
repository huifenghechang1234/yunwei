"""
title = ''
author = 'huifenghechang'
mtime = '2023/12/10'
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
文件比较
通过open()函数直接把给定的文件路径，所有内容读取出来，保存到列表中，然后传递给difflib中的make_file进行比较即可

注意：读的时候使用二进制rb模式，可以防止各种乱码的问题，读完之后通过decode转换为utf-8再进行比较
"""
import difflib

class DiffFile:
    """文件比较类"""

    @classmethod
    def _read_file(cls, file):
        """
        读取文件内容，以列表形式返回
        :param file: 文件路径
        :return:
        """
        try:
            with open(file, "rb") as fp:
                # 二进制方式读取文件内容，并转换为str类型
                lines = fp.read().decode('utf-8')
                # 按行进行分割
                text = lines.splitlines()
                # print text
                return text
        except Exception as e:
            print("ERROR: %s" % str(e))

    @classmethod
    def compare_file(cls, file1, file2, out_file):
        """
        比较文件，生成html格式
        :param file1: 第1个文件路径
        :param file2: 第2个文件路径
        :param out_file: 比较结果文件路径
        :return:
        """
        file1_content = cls._read_file(file1)
        file2_content = cls._read_file(file2)
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(file1_content, file2_content)
        with open(out_file, 'w') as fp:
            fp.writelines(compare_result)

    @classmethod
    def compare_text(cls, src_text, target_text):
        """
        比较给定的2个字符串
        :param src_text:
        :param target_text:
        :return:
        """
        d = difflib.Differ()
        return "".join(list(d.compare(src_text, target_text)))

    @classmethod
    def compare_text_to_file(cls, src_text, target_text, out_file):
        """
        比较给定的2个字符串，生成html格式
        :param src_text:
        :param target_text:
        :param out_file:
        :return:
        """
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(src_text, target_text)
        with open(out_file, 'w') as fp:
            fp.writelines(compare_result)


if __name__ == '__main__':

    DiffFile.compare_file('Demo.py', "Demo2.py", 'diff2.html')

    text1 = '''  1. Beautiful is better than ugly.
           2. Explicit is better than implicit.
           3. Simple is better than complex.
           4. Complex is better than complicated.
         '''.splitlines(keepends=True)

    text2 = '''  1. Beautiful is better than ugly.
           3.   Simple is better than complex.
           4. Complicated is better than complex.
           5. Flat is better than nested.
         '''.splitlines(keepends=True)
    print(DiffFile.compare_text_to_file(text1, text2, 'text_diff.html'))
