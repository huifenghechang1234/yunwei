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
密码管理器

这个自动化脚本可以帮你管理所有密码，使用不同的加密技术确保密码安全，只有你自己才能访问
"""

import streamlit as st
import csv
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# Custom encryption key (hardcoded)
CUSTOM_ENCRYPTION_KEY = b'u7wGgNdDFefqpr_kGxb8wJf6XRVsRwvb3QgITsD5Ft4='                   ## 如果您打算在共享平台上使用此脚本，请确保将此密钥保存在一个单独的安全文件中。

# Function to encrypt password
def encrypt_password(password):
    cipher_suite = Fernet(CUSTOM_ENCRYPTION_KEY)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Function to decrypt password
def decrypt_password(encrypted_password):
    if isinstance(encrypted_password, bytes):
        try:
            cipher_suite = Fernet(CUSTOM_ENCRYPTION_KEY)
            decrypted_password = cipher_suite.decrypt(encrypted_password)
            return decrypted_password.decode()
        except InvalidToken:
            return "Invalid Token"
    else:
        return None

# Function to save website name and password to CSV file
def save_credentials(website_name, password):
    encrypted_password = encrypt_password(password)
    with open('credentials.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([website_name, encrypted_password.decode()])  # Ensure storing string representation

# Function to retrieve password from CSV file
def retrieve_password(website_name):
    with open('credentials.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == website_name:
                encrypted_password = row[1].encode()
                return encrypted_password
    return None

# Streamlit UI
st.title("Password Manager")

# Input fields for website name and password
website_name = st.text_input("Enter website name:")
password = st.text_input("Enter password:", type="password")

# Save button to save website name and password
if st.button("Save"):
    if website_name and password:
        save_credentials(website_name, password)
        st.success("Website name and password saved successfully.")
    else:
        st.error("Please fill in all fields.")

# Retrieve button to retrieve password
if st.checkbox("Retrieve Password"):
    website_name = st.selectbox("Select website name:", options=[""] + [row[0] for row in csv.reader(open('credentials.csv', 'r'))])
    key = st.text_input("Enter Your Encryption Key:", type="password")
    if st.button("Retrieve Password"):
        if key == str(CUSTOM_ENCRYPTION_KEY.decode()):
            if website_name:
                encrypted_password = retrieve_password(website_name)
                if encrypted_password:
                    decrypted_password = decrypt_password(encrypted_password)
                    st.success(f"Password for **{website_name}** -> **{decrypted_password}**")
                else:
                    st.error("Password not found in database.")
        elif key == "":
            pass
        else:
            st.error("Invalid Encryption Key!!!")
