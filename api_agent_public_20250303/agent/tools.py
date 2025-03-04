import requests


async def save_script_to_file(filename:str, code: str):
    """
    将Python代码保存到指定的.py文件中。

    :param filename: 要保存的文件名（包括.py扩展名）
    :param code: 要保存的Python代码（字符串形式）
    """
    filename = "../tests/" + filename
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(code)
        print(f"代码已成功保存到 {filename}")
        return "FINISHED"
    except Exception as e:
        print(f"保存文件时出错: {e}")

async def load_api_doc():
    """加载API描述文档"""
    res = requests.get("http://localhost:8001/openapi.json")
    return res.json()
