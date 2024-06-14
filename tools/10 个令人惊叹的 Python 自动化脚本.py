#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/6/14 15:04
@Author  : waxberry
@File    : 10 个令人惊叹的 Python 自动化脚本.py
@Software: PyCharm
"""



# /01/ 剪贴板管理器
import tkinter as tk
from tkinter import ttk
import pyperclip

def update_listbox():
    new_item = pyperclip.paste()
    if new_item not in X:
        X.append(new_item)
        listbox.insert(tk.END, new_item)
        listbox.insert(tk.END, "----------------------")
    listbox.yview(tk.END)
    root.after(1000, update_listbox)

def copy_to_clipboard(event):
    selected_item = listbox.get(listbox.curselection())
    if selected_item:
        pyperclip.copy(selected_item)

X = []

root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Clipboard Contents:", bg="#f0f0f0")
label.grid(row=0, column=0)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, width=150, height=150, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)

update_listbox()

listbox.bind("<Double-Button-1>", copy_to_clipboard)

root.mainloop()
# 应用
# 捕捉从各种来源复制的研究笔记并进行分类。
# 扩展脚本可以捕捉重要的日历事件、提醒事项、密码等。




# /02/ 代码质量检查器
import os
import subprocess

def analyze_code(directory):
    # List Python files in the directory
    python_files = [file for file in os.listdir(directory) if file.endswith('.py')]

    if not python_files:
        print("No Python files found in the specified directory.")
        return

    # Analyze each Python file using pylint and flake8
    for file in python_files:
        print(f"Analyzing file: {file}")
        file_path = os.path.join(directory, file)

        # Run pylint
        print("\nRunning pylint...")
        pylint_command = f"pylint {file_path}"
        subprocess.run(pylint_command, shell=True)

        # Run flake8
        print("\nRunning flake8...")
        flake8_command = f"flake8 {file_path}"
        subprocess.run(flake8_command, shell=True)

if __name__ == "__main__":
    directory = r"C:\Users\abhay\OneDrive\Desktop\Part7"
    analyze_code(directory)

# 应用
# 自动代码增强器 - 对该脚本稍作扩展，可用于创建一个 Python 脚本，用于识别代码中的问题并作出相应修改。
# 自动代码审查。




# /03/ 不篡改文件
import hashlib
import os

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_integrity(file_path, expected_checksum):
    actual_checksum = calculate_sha256(file_path)
    return actual_checksum == expected_checksum

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    expected_checksum = input("Enter the expected SHA-256 checksum: ")

    if os.path.isfile(file_path):
        if check_integrity(file_path, expected_checksum):
            print("File integrity verified: The file has not been tampered with.")
        else:
            print("File integrity check failed: The file may have been tampered with.")
    else:
        print("Error: File not found.")




# /04/ 智能交易
import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('MSFT', "TSLA", 'GOOG', 'AAPL', "NVDA")
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())

st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)
# 要运行此程序，首先需要使用 pip 安装 Streamlit、yfinance、prophet 和 plotly python 库。
# 然后使用命令streamlit run smart_trade.py 运行它
# 应用
# 算法交易
# 股票价格比较仪表板




# /05/ 自动图像下载器
# Importing the necessary module and function
from simple_image_download import simple_image_download as simp

# Creating a response object
response = simp.simple_image_download

## Keyword
keyword = "Dog"

# Downloading images
try:
    response().download(keyword, 20)
    print("Images downloaded successfully.")
except Exception as e:
    print("An error occurred:", e)



# /06/ 端口扫描程序
import socket
from prettytable import PrettyTable
import sys

# Dictionary mapping common ports to vulnerabilities (Top 15)
vulnerabilities = {
    80: "HTTP (Hypertext Transfer Protocol) - Used for unencrypted web traffic",
    443: "HTTPS (HTTP Secure) - Used for encrypted web traffic",
    22: "SSH (Secure Shell) - Used for secure remote access",
    21: "FTP (File Transfer Protocol) - Used for file transfers",
    25: "SMTP (Simple Mail Transfer Protocol) - Used for email transmission",
    23: "Telnet - Used for remote terminal access",
    53: "DNS (Domain Name System) - Used for domain name resolution",
    110: "POP3 (Post Office Protocol version 3) - Used for email retrieval",
    143: "IMAP (Internet Message Access Protocol) - Used for email retrieval",
    3306: "MySQL - Used for MySQL database access",
    3389: "RDP (Remote Desktop Protocol) - Used for remote desktop connections (Windows)",
    8080: "HTTP Alternate - Commonly used as a secondary HTTP port",
    8000: "HTTP Alternate - Commonly used as a secondary HTTP port",
    8443: "HTTPS Alternate - Commonly used as a secondary HTTPS port",
    5900: "VNC (Virtual Network Computing) - Used for remote desktop access",
    # Add more ports and vulnerabilities as needed
}

def display_table(open_ports):
    table = PrettyTable(["Open Port", "Vulnerability"])
    for port in open_ports:
        vulnerability = vulnerabilities.get(port, "No known vulnerabilities associated with common services")
        table.add_row([port, vulnerability])
    print(table)

def scan_top_ports(target):
    open_ports = []
    top_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 5900, 8000, 8080, 8443]  # Top 15 ports
    for port in top_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust timeout as needed
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            sys.exit()
        except socket.error:
            pass
    return open_ports

def main():
    target = input("Enter the website URL or IP address to scan for open ports: ")
    open_ports = scan_top_ports(target)
    if not open_ports:
        print("No open ports found on the target.")
    else:
        print("Open ports and associated vulnerabilities:")
        display_table(open_ports)

if __name__ == "__main__":
    main()




# /07/ 密码管理器
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




# /08/ 邮件群发器
import smtplib
import ssl

# SMTP server details
smtp_server = 'data.STUDIO.com'
smtp_port = 465

# Sender and recipient details
from_address = 'Winzo Shop'
to_address = ['','']     ## Recepients List

# Authentication details
username = ''       ## Sender Email
password = ''       ## Sender Password


# Email message details
subject = '🎉 Exclusive Offer Inside! Get 10% Off Your Next Purchase'
body = '''
'''

# Create an SSL/TLS context
context = ssl.create_default_context()

# Connect to the SMTP server using SSL/TLS
with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    # Enable debugging to print the server's responses
    server.set_debuglevel(1)

    # Login to the SMTP server
    server.login(username, password)

    # Create the email message
    message = f'From: {from_address}\r\nSubject: {subject}\r\nTo: {to_address}\r\n\r\n{body}'
    message = message.encode()  # Convert the message to bytes

    # Send the email
    server.sendmail(from_address, to_address, message)




# /09/ Readme.md 生成器
def generate_markdown_file():
    # Prompting user for inputs
    repository_name = input("\n Enter the name of your GitHub repository: ")
    project_description = input("Enter a short description of your project: ")
    installation_instructions = input("Enter installation instructions for your project: ")
    usage_instructions = input("Enter usage instructions for your project: ")
    contributors = input("Enter the contributors to your project (separated by commas): ")
    license = select_license()

    # Generating badges
    stars_badge = "[![GitHub stars](https://img.shields.io/github/stars/{})](https://github.com/{}/stargazers)".format(repository_name, repository_name)
    forks_badge = "[![GitHub forks](https://img.shields.io/github/forks/{})](https://github.com/{}/network/members)".format(repository_name, repository_name)
    issues_badge = "[![GitHub issues](https://img.shields.io/github/issues/{})](https://github.com/{}/issues)".format(repository_name, repository_name)
    license_badge = "[![GitHub license](https://img.shields.io/github/license/{})](https://github.com/{}/blob/master/LICENSE)".format(repository_name, repository_name)

    # Generating Markdown content
    markdown_content = f"""
    # {repository_name}

    {project_description}

    ## Table of Contents
    - [Installation](#installation)
    - [Usage](#usage)
    - [Contributors](#contributors)
    - [License](#license)
    - [Badges](#badges)
    - [GitHub Repository](#github-repository)

    ## Installation
    ```
    {installation_instructions}
    ```
    ## Usage
    ```
    {usage_instructions}
    ```
    ## Contributors
    {contributors}
    ## License
    This project is licensed under the {license} License - see the [LICENSE](LICENSE) file for details.
    ## Badges
    {stars_badge} {forks_badge} {issues_badge} {license_badge}
    ## GitHub Repository
    [Link to GitHub repository](https://github.com/{repository_name})
    """
    # Writing content to Markdown file
    markdown_file_name = f"{repository_name}_README.md"
    with open(markdown_file_name, "w") as markdown_file:
        markdown_file.write(markdown_content)
    print(f"Markdown file '{markdown_file_name}' generated successfully!")

def select_license():
    licenses = {
        "MIT": "MIT License",
        "Apache": "Apache License 2.0",
        "GPL": "GNU General Public License v3.0",
        # Add more licenses as needed
    }
    print("Select a license for your project:")
    for key, value in licenses.items():
        print(f"{key}: {value}")
    while True:
        selected_license = input("Enter the number corresponding to your selected license: ")
        if selected_license in licenses:
            return licenses[selected_license]
        else:
            print("Invalid input. Please enter a valid license number.")

if __name__ == "__main__":
    generate_markdown_file()




# /10/ OrganizeIT 2.0
import os
import hashlib
import shutil

def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def organize_and_move_duplicates(folder_path):
    # Create a dictionary to store destination folders based on file extensions
    extension_folders = {}

    # Create the "Duplicates" folder if it doesn't exist
    duplicates_folder = os.path.join(folder_path, 'Duplicates')
    os.makedirs(duplicates_folder, exist_ok=True)

    # Create a dictionary to store file hashes
    file_hashes = {}

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()  # Convert extension to lowercase

            # Determine the destination folder
            if extension in extension_folders:
                destination_folder = extension_folders[extension]
            else:
                destination_folder = os.path.join(folder_path,
                                                  extension[1:])  # Remove the leading dot from the extension
                os.makedirs(destination_folder, exist_ok=True)
                extension_folders[extension] = destination_folder

            # Calculate the file hash
            file_hash = get_file_hash(file_path)

            # Check for duplicates
            if file_hash in file_hashes:
                # File is a duplicate, move it to the "Duplicates" folder
                shutil.move(file_path, os.path.join(duplicates_folder, filename))
                print(f"Moved duplicate file {filename} to Duplicates folder.")
            else:
                # Store the file hash
                file_hashes[file_hash] = filename
                # Move the file to the destination folder
                shutil.move(file_path, destination_folder)
                print(f"Moved {filename} to {destination_folder}")


if __name__ == "__main__":
    folder_path = input("Enter the path to the folder to organize: ")
    organize_and_move_duplicates(folder_path)