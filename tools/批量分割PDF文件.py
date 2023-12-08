# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/8 9:05
# @Author : waxberry
# @File : 批量分割PDF文件.py
# @Software : PyCharm


'''一、架构设计
在进行批量分割PDF文件之前，我们需要先设计一个合理的架构，以确保代码的可维护性和可扩展性。
以下是一个简单的架构设计示意图：
1. 输入模块：负责接收用户输入的PDF文件路径和分割规则（如每页分割、按页数分割等）。
2. 处理模块：负责读取PDF文件，并根据分割规则进行分割。
3. 输出模块：将分割后的PDF文件保存到指定路径。

二、代码实现
接下来，我们将逐步实现上述架构中的各个模块。
首先，我们需要安装一个用于处理PDF文件的Python库——PyPDF2。
可以使用以下命令进行安装：

pip install PyPDF2'''


# 输入模块
import os

def get_pdf_files(directory):
    pdf_files = []
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(directory, file))
    return pdf_files
def get_split_rule():
    # 根据具体需求，获取分割规则
    pass
def get_output_directory():
    # 根据具体需求，获取输出路径
    pass

# 处理模块
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(file_path, split_rule):
    pdf = PdfFileReader(file_path)
    output_files = []
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        output_pdf = PdfFileWriter()
        output_pdf.addPage(page)
        output_file_path = f"{file_path}_{i}.pdf"
        with open(output_file_path, "wb") as output_file:
            output_pdf.write(output_file)
        output_files.append(output_file_path)
    return output_files


# 输出模块
def save_output_files(output_files, output_directory):
    for file in output_files:
        file_name = os.path.basename(file)
        output_path = os.path.join(output_directory, file_name)
        os.rename(file, output_path)


# 三、批量分割PDF文件
# 现在，我们可以将上述模块组合起来，实现批量分割PDF文件的功能。

def main():
    directory = input("请输入PDF文件所在目录：")
    pdf_files = get_pdf_files(directory)
    split_rule = get_split_rule()
    output_directory = get_output_directory()

    for file in pdf_files:
        output_files = split_pdf(file, split_rule)
        save_output_files(output_files, output_directory)

    print("分割完成！")

if __name__ == "__main__":
    main()