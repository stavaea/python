import re
from typing import List, Dict


def analyze_requirements(text: str) -> Dict[str, List[str]]:
    """
    分析需求文本并拆分成功能测试项

    参数:
        text: 需求文本

    返回:
        字典，包含模块和对应的测试项列表
    """
    # 初始化结果字典
    results = {
        "核心功能": [],
        "用户界面": [],
        "数据处理": [],
        "性能要求": [],
        "安全要求": [],
        "其他功能": []
    }

    # 预处理文本：移除多余空格和换行
    cleaned_text = ' '.join(text.split())

    # 识别核心功能测试项
    core_patterns = [
        r'应(基于|整合|为|从而|经过|包括|对|形成|利用|帮助|)([^。]+)',
        r'必须(实现|提供|具备|建立)([^。]+)',
        r'功能包括([^。]+)',
        r'实现([^。]+)功能'
    ]
    results["核心功能"] = _extract_items(cleaned_text, core_patterns)

    # 识别用户界面测试项
    ui_patterns = [
        r'界面应([^。]+)',
        r'显示([^。]+)',
        r'布局([^。]+)',
        r'用户交互([^。]+)'
    ]
    results["用户界面"] = _extract_items(cleaned_text, ui_patterns)

    # 识别数据处理测试项
    data_patterns = [
        r'数据(存储|处理|保存)([^。]+)',
        r'输入([^。]+)',
        r'输出([^。]+)',
        r'支持([^。]+)格式'
    ]
    results["数据处理"] = _extract_items(cleaned_text, data_patterns)

    # 识别性能要求测试项
    perf_patterns = [
        r'响应时间(不超过|少于)([^。]+)',
        r'支持([^。]+)并发',
        r'每秒处理([^。]+)',
        r'性能要求([^。]+)'
    ]
    results["性能要求"] = _extract_items(cleaned_text, perf_patterns)

    # 识别安全要求测试项
    security_patterns = [
        r'安全(要求|措施)([^。]+)',
        r'权限(控制|管理)([^。]+)',
        r'加密([^。]+)',
        r'防止([^。]+)'
    ]
    results["安全要求"] = _extract_items(cleaned_text, security_patterns)

    # 其他未分类的功能
    other_patterns = [
        r'当([^。]+)时，系统应([^。]+)',
        r'如果([^。]+)，则([^。]+)'
    ]
    results["其他功能"] = _extract_items(cleaned_text, other_patterns)

    # 过滤空项
    return {k: v for k, v in results.items() if v}


def _extract_items(text: str, patterns: List[str]) -> List[str]:
    """
    使用正则表达式从文本中提取测试项

    参数:
        text: 需求文本
        patterns: 正则表达式模式列表

    返回:
        提取的测试项列表
    """
    items = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            # 处理匹配结果为元组的情况
            if isinstance(match, tuple):
                item = ' '.join([m for m in match if m])
            else:
                item = match

            # 清理结果并添加到列表
            cleaned_item = item.strip(' ,;:、')
            if cleaned_item and len(cleaned_item) > 2:  # 过滤过短的项
                items.append(cleaned_item)

    return list(set(items))  # 去重


def print_test_items(test_items: Dict[str, List[str]]):
    """
    打印整理后的测试项

    参数:
        test_items: 测试项字典
    """
    for category, items in test_items.items():
        print(f"\n=== {category} ===")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")


if __name__ == "__main__":
    print("需求分析脚本 - 功能测试项拆分工具")
    print("请输入需求文本(输入'END'结束):\n")

    # 读取多行输入
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)

    # 合并文本并分析
    requirement_text = '\n'.join(lines)
    if requirement_text.strip():
        test_items = analyze_requirements(requirement_text)
        print("\n分析结果：")
        print_test_items(test_items)
    else:
        print("未输入有效需求文本")