# -*- coding:utf-8 -*-
# ！/usr/bin/env python


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