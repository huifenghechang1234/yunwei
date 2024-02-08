"""
title = ''
author = 'huifenghechang'
mtime = '2024/1/15'
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

import os
import pandas as pd
import random
import datetime
from delphivcl import *

Qfiles = 'Questions.xlsx'
Record = 'Record.txt'


class Form1(Form):

    def __init__(self, owner):
        for i in range(7):
            setattr(self, f'p_{i}', Panel(self))
        self.bt_ty_sept = Button(self)
        for i in range(1, 21):
            setattr(self, f'bt_ty_{i}', Button(self))
        self.gb_twty = GroupBox(self)
        self.lt_ty_A = LabeledEdit(self)
        for i in range(1, 13):
            setattr(self, f'bt_tw_{i}', Button(self))
        self.le_tw_A = LabeledEdit(self)
        self.gb_tw = GroupBox(self)
        self.le_Nine_A = LabeledEdit(self)
        for i in range(1, 10):
            setattr(self, f'bt_Nine_{i}', Button(self))

        self.gb_Nine = GroupBox(self)
        self.le_fm_A = LabeledEdit(self)
        self.le_fm_Q = LabeledEdit(self)
        self.le_fs_A = LabeledEdit(self)
        self.le_fs_Q = LabeledEdit(self)

        self.ed_m_D = Edit(self)
        self.ed_m_C = Edit(self)
        self.ed_m_B = Edit(self)
        self.ed_m_A = Edit(self)

        self.cb_m_D = CheckBox(self)
        self.cb_m_C = CheckBox(self)
        self.cb_m_B = CheckBox(self)
        self.cb_m_A = CheckBox(self)

        self.gb_m_A = GroupBox(self)
        self.le_m_Q = LabeledEdit(self)

        self.le_Ansewer = LabeledEdit(self)

        self.ed_s_d = Edit(self)
        self.ed_s_c = Edit(self)
        self.ed_s_b = Edit(self)
        self.ed_s_a = Edit(self)

        self.ed_s_a = Edit(self)
        self.le_s_q = LabeledEdit(self)
        self.rg_s = RadioGroup(self)

        self.ed_levelAndNumber = Edit(self)
        self.pc_Q = PageControl(self)
        self.ed_time = Edit(self)
        self.ed_rate = Edit(self)
        self.ed_ng = Edit(self)
        self.ed_ok = Edit(self)
        self.cb_level = ComboBox(self)
        self.lb_rate = Label(self)
        self.lb_ng = Label(self)
        self.lb_ok = Label(self)
        self.lb_selectQ = Label(self)
        self.bt_submit = Button(self)
        self.bt_clear = Button(self)
        self.bt_exit = Button(self)
        self.ed_ok = Edit(self)
        self.lb_title = Label(self)
        self.right = Splitter(self)
        self.left = Splitter(self)
        self.top = Splitter(self)

        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Unit1.pydfm"))

        self.bt_ty_20.OnClick = self.bt_ty_20Click
        self.bt_ty_19.OnClick = self.bt_ty_19Click
        self.bt_ty_18.OnClick = self.bt_ty_18Click
        self.bt_ty_17.OnClick = self.bt_ty_17Click
        self.bt_ty_16.OnClick = self.bt_ty_16Click
        self.bt_ty_15.OnClick = self.bt_ty_15Click
        self.bt_ty_14.OnClick = self.bt_ty_14Click
        self.bt_ty_13.OnClick = self.bt_ty_13Click
        self.bt_ty_12.OnClick = self.bt_ty_12Click
        self.bt_ty_11.OnClick = self.bt_ty_11Click
        self.bt_ty_10.OnClick = self.bt_ty_10Click
        self.bt_ty_9.OnClick = self.bt_ty_9Click
        self.bt_ty_8.OnClick = self.bt_ty_8Click
        self.bt_ty_7.OnClick = self.bt_ty_7Click
        self.bt_ty_6.OnClick = self.bt_ty_6Click
        self.bt_ty_5.OnClick = self.bt_ty_5Click
        self.bt_ty_4.OnClick = self.bt_ty_4Click
        self.bt_ty_3.OnClick = self.bt_ty_3Click
        self.bt_ty_2.OnClick = self.bt_ty_2Click
        self.bt_ty_1.OnClick = self.bt_ty_1Click
        self.bt_tw_12.OnClick = self.bt_tw_12Click
        self.bt_tw_11.OnClick = self.bt_tw_11Click
        self.bt_tw_10.OnClick = self.bt_tw_10Click
        self.bt_tw_9.OnClick = self.bt_tw_9Click
        self.bt_tw_8.OnClick = self.bt_tw_8Click
        self.bt_tw_7.OnClick = self.bt_tw_7Click
        self.bt_tw_6.OnClick = self.bt_tw_6Click
        self.bt_tw_5.OnClick = self.bt_tw_5Click
        self.bt_tw_4.OnClick = self.bt_tw_4Click
        self.bt_tw_3.OnClick = self.bt_tw_3Click
        self.bt_tw_2.OnClick = self.bt_tw_2Click
        self.bt_tw_1.OnClick = self.bt_tw_1Click
        self.bt_Nine_9.OnClick = self.bt_Nine_9Click
        self.bt_Nine_8.OnClick = self.bt_Nine_8Click
        self.bt_Nine_7.OnClick = self.bt_Nine_7Click
        self.bt_Nine_6.OnClick = self.bt_Nine_6Click
        self.bt_Nine_5.OnClick = self.bt_Nine_5Click
        self.bt_Nine_4.OnClick = self.bt_Nine_4Click
        self.bt_Nine_3.OnClick = self.bt_Nine_3Click
        self.bt_Nine_2.OnClick = self.bt_Nine_2Click
        self.bt_Nine_1.OnClick = self.bt_Nine_1Click
        self.bt_ty_sept.OnClick = self.bt_ty_septClick
        self.bt_submit.OnClick = self.bt_submitClick
        self.bt_next.OnClick = self.bt_nextClick
        self.cb_question.OnChange = self.cb_questionChange
        self.bt_exit.OnClick = self.bt_exitClick
        self.bt_clear.OnClick = self.bt_clearClick
        self.bt_next.Caption = "开始"

        self.df = pd.read_excel(Qfiles)  # 读取题库文件
        self.question_num = 0  # 当前题目编号
        self.level = 0  # 当前题目难度等级
        self.QType = 0  # 当前题目类型
        self.strWord = ""
        self.listWord = []
        self.A_Result = ""

    def clear_all_status(self):
        self.ed_s_a.Color = clWindow
        self.ed_s_b.Color = clWindow
        self.ed_s_c.Color = clWindow
        self.ed_s_d.Color = clWindow
        self.ed_m_A.Color = clWindow
        self.ed_m_B.Color = clWindow
        self.ed_m_C.Color = clWindow
        self.ed_m_D.Color = clWindow
        self.le_fs_A.Color = clWindow
        self.le_fm_A.Color = clWindow
        self.le_Nine_A.Color = clWindow
        self.le_tw_A.Color = clWindow
        self.lt_ty_A.Color = clWindow
        self.le_Ansewer.Text = ""
        self.le_fm_A.Text = ""
        self.le_fs_A.Text = ""
        self.le_Nine_A.Text = ""
        self.le_tw_A.Text = ""
        self.rg_s.ItemIndex = -1


def bt_clearClick(self, Sender):
    self.clear_all_status()


def bt_exitClick(self, Sender):
    pass


def cb_questionChange(self, Sender):
    self.pc_Q.ActivePageIndex = self.cb_question.ItemIndex - 1


def show_single_choice(self):
    # 单选题显示
    self.le_s_q.Text = self.df.iloc[self.question_num, 3]
    self.ed_s_a.Text = self.df.iloc[self.question_num, 5]
    self.ed_s_b.Text = self.df.iloc[self.question_num, 6]
    self.ed_s_c.Text = self.df.iloc[self.question_num, 7]
    self.ed_s_d.Text = self.df.iloc[self.question_num, 8]


def show_multiple_choice(self):
    # 多选题显示代码
    self.le_m_Q.Text = self.df.iloc[self.question_num, 3]
    self.ed_m_A.Text = self.df.iloc[self.question_num, 5]
    self.ed_m_B.Text = self.df.iloc[self.question_num, 6]
    self.ed_m_C.Text = self.df.iloc[self.question_num, 7]
    self.ed_m_D.Text = self.df.iloc[self.question_num, 8]


def show_fs_blank(self):
    # 填空题显示代码
    self.le_fs_Q.Text = self.df.iloc[self.question_num, 3]


def show_fm_blank(self):
    # 对句题显示代码
    self.le_fm_Q.Text = self.df.iloc[self.question_num, 3]


def show_nine_box(self):
    self.listWord = list(self.df.iloc[self.question_num, 3])
    bts = [getattr(self, f'bt_Nine_{i + 1}') for i in range(9)]
    for i in range(9):
        bts[i].Caption = self.listWord[i]


def show_twelve_box(self):
    # 12宫代码
    self.listWord = list(self.df.iloc[self.question_num, 3])
    bts = [getattr(self, f'bt_tw_{i + 1}') for i in range(12)]
    for i in range(12):
        bts[i].Caption = self.listWord[i]


def show_twenty_box(self):
    # 20宫代码
    self.listWord = list(self.df.iloc[self.question_num, 3])
    bts = [getattr(self, f'bt_ty_{i + 1}') for i in range(20)]
    for i in range(20):
        bts[i].Caption = self.listWord[i]


def show_static_info(self, result):
    """显示正确率统计信息"""
    if result == "True":
        self.ed_ok.Text = int(self.ed_ok.Text) + 1
    else:
        self.ed_ng.Text = int(self.ed_ng.Text) + 1
    self.ed_rate.Text = 100 * int(self.ed_ok.Text) / (int(self.ed_ok.Text) + int(self.ed_ng.Text))  # 直接算百分比


def check_s_answer(self):
    """检查单选题答案"""
    ra = ['A', 'B', 'C', 'D']
    selected = ra[self.rg_s.ItemIndex]
    answer = self.df.iloc[self.question_num, 4]

    if selected == answer:
        self.A_Result = "True"
    self.highlight(selected, clGreen)
    else:
    self.A_Result = "False"
    self.highlight(selected, clRed)


def highlight(self, choice, color):
    """选项高亮"""
    if choice == 'A':
        self.ed_s_a.Color = color
    elif choice == 'B':
        self.ed_s_b.Color = color
    elif choice == 'C':
        self.ed_s_c.Color = color
    elif choice == 'D':
        self.ed_s_d.Color = color


def check_m_answer(self):
    # 检查多选题代码
    ra = ['A', 'B', 'C', 'D']
    answer = list(self.df.iloc[self.question_num, 4])
    selected = []
    if self.cb_m_A.Checked == 1:
        selected.append(ra[0])
    if self.cb_m_B.Checked == 1:
        selected.append(ra[1])
    if self.cb_m_C.Checked == 1:
        selected.append(ra[2])
    if self.cb_m_D.Checked == 1:
        selected.append(ra[3])


selected.sort()
answer.sort()
self.A_Result = "True" if selected == answer else "False"


# Todo填充颜色

def check_fs_answer(self):
    # 检查填字题代码
    if self.le_fs_A.Text == self.df.iloc[self.question_num, 4]:
        self.A_Result = "True"
        self.le_fs_A.Color = clGreen
    else:
        self.A_Result = "False"
        self.le_fs_A.Color = clRed


def check_fm_answer(self):
    # 检查对句题代码
    if self.le_fm_A.Text == self.df.iloc[self.question_num, 4]:
        self.A_Result = "True"
        self.le_fm_A.Color = clGreen
    else:
        self.A_Result = "False"
        self.le_fm_A.Color = clRed


def check_nine_answer(self):
    # 检查九宫格答案
    if self.le_Nine_A == self.df.iloc[self.question_num, 4]:
        self.A_Result = "True"
        self.le_Nine_A.Color = clGreen
    else:
        self.A_Result = "False"
        self.le_Nine_A.Color = clRed


def check_tw_answer(self):
    # 检查十二宫
    if self.le_tw_A == self.df.iloc[self.question_num, 4]:
        self.A_Result = "True"
        self.le_tw_A.Color = clGreen
    else:
        self.A_Result = "False"
        self.le_tw_A.Color = clRed


def check_ty_answer(self):  # Todo:这里还需要调整，有可能只对一半，或者前后两句的顺序可能反过来
    # 检查二十宫
    if self.lt_ty_A == self.df.iloc[self.question_num, 4]:
        self.A_Result = "True"
        self.lt_ty_A.Color = clGreen
    else:
        self.A_Result = "False"
        self.lt_ty_A.Color = clRed


def show_correct_answer(self):
    # 显示正确答案
    self.le_Ansewer.Text = self.df.iloc[self.question_num, 4]
    self.le_Ansewer.Color = clGreen
    self.le_Ansewer.Font.Color = clWhite


def show_Question(self):
    """判断题目类型并显示"""
    if self.pc_Q.ActivePageIndex == 0:
        self.show_single_choice()
    elif self.pc_Q.ActivePageIndex == 1:
        self.show_multiple_choice()
    elif self.pc_Q.ActivePageIndex == 2:
        self.show_fs_blank()
    elif self.pc_Q.ActivePageIndex == 3:
        self.show_fm_blank()
    elif self.pc_Q.ActivePageIndex == 4:
        self.show_nine_box()
    elif self.pc_Q.ActivePageIndex == 5:  # 十二宫
        self.show_twelve_box()
    elif self.pc_Q.ActivePageIndex == 6:  # 二十宫
        self.show_twenty_box()


def bt_nextClick(self, Sender):
    """下一题的处理"""
    self.bt_next.Caption = "下一题"
    self.clear_all_status()
    self.question_num = random.randint(0, len(self.df) - 1)
    self.level = self.df.iloc[self.question_num, 2]
    self.ed_levelAndNumber.Text = f"难度：{str(self.level)}--题号:{self.question_num + 1}"
    self.QType = self.df.iloc[self.question_num, 1]
    self.pc_Q.ActivePageIndex = int(self.QType) - 1
    self.show_Question()


def bt_submitClick(self, Sender):
    """根据题目类型判断答题结果"""
    if self.pc_Q.ActivePageIndex == 0:
        self.check_s_answer()
    elif self.pc_Q.ActivePageIndex == 1:
        self.check_m_answer()
    elif self.pc_Q.ActivePageIndex == 2:
        self.check_fs_answer()
    elif self.pc_Q.ActivePageIndex == 3:
        self.check_fm_answer()
    elif self.pc_Q.ActivePageIndex == 4:
        self.check_nine_answer()
    elif self.pc_Q.ActivePageIndex == 5:  # 十二宫
        self.check_tw_answer()
    elif self.pc_Q.ActivePageIndex == 6:  # 二十宫
        self.check_ty_answer()
    self.show_correct_answer()
    self.show_static_info(self.A_Result)


def bt_ty_septClick(self, Sender):
    self.lt_ty_A.Text = self.lt_ty_A.Text + '|'
    # 九宫、十二宫，二十宫和处理,这段代码稀烂，不想优化了


def bt_Nine_1Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_1.Caption


def bt_Nine_2Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_2.Caption


def bt_Nine_3Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_3.Caption


def bt_Nine_4Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_4.Caption


def bt_Nine_5Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_5.Caption


def bt_Nine_6Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_6.Caption


def bt_Nine_7Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_7.Caption


def bt_Nine_8Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_8.Caption


def bt_Nine_9Click(self, Sender):
    self.le_Nine_A.Text += self.bt_Nine_9.Caption
    # 十二宫按钮


def bt_tw_1Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_1.Caption


def bt_tw_2Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_2.Caption


def bt_tw_3Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_3.Caption


def bt_tw_4Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_4.Caption


def bt_tw_5Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_5.Caption


def bt_tw_6Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_6.Caption


def bt_tw_7Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_7.Caption


def bt_tw_8Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_8.Caption


def bt_tw_9Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_9.Caption


def bt_tw_10Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_10.Caption


def bt_tw_11Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_11.Caption


def bt_tw_12Click(self, Sender):
    self.le_tw_A.Text += self.bt_tw_12.Caption
    # 二十宫格


def bt_ty_1Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_1.Caption


def bt_ty_2Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_2.Caption


def bt_ty_3Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_3.Caption


def bt_ty_4Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_4.Caption


def bt_ty_5Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_5.Caption


def bt_ty_6Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_6.Caption


def bt_ty_7Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_7.Caption


def bt_ty_8Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_8.Caption


def bt_ty_9Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_9.Caption


def bt_ty_10Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_10.Caption


def bt_ty_11Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_11.Caption


def bt_ty_12Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_12.Caption


def bt_ty_13Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_13.Caption


def bt_ty_14Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_14.Caption


def bt_ty_15Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_15.Caption


def bt_ty_16Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_16.Caption


def bt_ty_17Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_17.Caption


def bt_ty_18Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_18.Caption


def bt_ty_19Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_19.Caption


def bt_ty_20Click(self, Sender):
    self.lt_ty_A.Text += self.bt_ty_20.Caption

#    def bt_Nine_Click(self, Sender):
#        buttons = [self.bt_Nine_1, self.bt_Nine_2, self.bt_Nine_3, self.bt_Nine_4, self.bt_Nine_5, self.bt_Nine_6, self.bt_Nine_7, self.bt_Nine_8, self.bt_Nine_9]
#        for button in buttons:
#            self.le_Nine_A.Text += button.Caption

#    def bt_tw_Click(self, Sender):
#        buttons = [self.bt_tw_1, self.bt_tw_2, self.bt_tw_3, self.bt_tw_4, self.bt_tw_5, self.bt_tw_6, self.bt_tw_7, self.bt_tw_8, self.bt_tw_9, self.bt_tw_10, self.bt_tw_11, self.bt_tw_12]
#        for button in buttons:
#            self.le_tw_A.Text += button.Caption

#    def bt_ty_Click(self, Sender):
#        buttons = [self.bt_ty_1, self.bt_ty_2, self.bt_ty_3, self.bt_ty_4, self.bt_ty_5, self.bt_ty_6, self.bt_ty_7, self.bt_ty_8, self.bt_ty_9,
#        self.bt_ty_10, self.bt_ty_11, self.bt_ty_12, self.bt_ty_13, self.bt_ty_14, self.bt_ty_15, self.bt_ty_16, self.bt_ty_17, self.bt_ty_18,
#         self.bt_ty_19, self.bt_ty_20]
#        for button in buttons:
#            self.lt_ty_A.Text += button.Caption