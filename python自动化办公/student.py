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
实现一个简单的学生班级信息的管理系统
"""

import mysql.connector
from tabulate import tabulate


class StudentDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            self.connection.commit()
            return result
        except mysql.connector.Error as e:
            print(f"执行查询时发生错误: {e}")
            raise e

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS students (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255),
                   age INT,
                   grade VARCHAR(2)
                   )'''
        self.execute_query(query)

    def insert_student(self, name, age, grade):
        query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        values = (name, age, grade)
        self.execute_query(query, values)

    def update_student(self, student_id, name, age, grade):
        query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
        values = (name, age, grade, student_id)
        self.execute_query(query, values)

    def delete_student(self, student_id):
        query = "DELETE FROM students WHERE id = %s"
        values = (student_id,)
        self.execute_query(query, values)

    def get_all_students(self):
        query = "SELECT * FROM students"
        return self.execute_query(query)

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM students WHERE id = %s"
        values = (student_id,)
        return self.execute_query(query, values)


def main():
    db = StudentDB(host='127.0.0.1', user='root', password='12345678', database='ibai-tools')
    db.connect()

    db.create_table()

    while True:
        print("\n请选择操作:")
        print("1. 添加学生")
        print("2. 更新学生信息")
        print("3. 删除学生")
        print("4. 查看所有学生")
        print("5. 退出")

        choice = input("请输入您的选择 (1-5): ")

        if choice == '1':
            name = input("请输入学生姓名: ")
            age = int(input("请输入学生年龄: "))
            grade = input("请输入学生班级: ")
            db.insert_student(name, age, grade)
            print("学生添加成功！")

        elif choice == '2':
            student_id = int(input("请输入要更新的学生ID: "))
            name = input("请输入学生的新姓名: ")
            age = int(input("请输入学生的新年龄: "))
            grade = input("请输入学生的新班级: ")
            db.update_student(student_id, name, age, grade)
            print("学生信息更新成功！")

        elif choice == '3':
            student_id = int(input("请输入要删除的学生ID: "))
            db.delete_student(student_id)
            print("学生删除成功！")

        elif choice == '4':
            students = db.get_all_students()
            headers = ["ID", "姓名", "年龄", "班级"]
            print(tabulate(students, headers=headers))

        elif choice == '5':
            print("正在退出...")
            break

        else:
            print("无效的选择，请输入1到5之间的数字。")

    db.close()


if __name__ == "__main__":
    main()
