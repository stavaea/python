import json
from datetime import datetime
from typing import List, Dict

class ResultExporter:
    @staticmethod
    def to_json(data: Dict, file_path: str = None):
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_functions': len(data['functions']),
                'total_test_items': len(data['test_items'])
            },
            'details': data
        }
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
        return json.dumps(report, ensure_ascii=False)

    @staticmethod
    def to_markdown(data: Dict) -> str:
        md = ["# 测试项分析报告", f"**生成时间**: {datetime.now()}\n"]

        md.append("## 识别功能点")
        for func, examples in data['functions'].items():
            md.append(f"- {func} (示例: {examples[0][:30]}...)")

        md.append("\n## 生成的测试项")
        for item in data['test_items'][:10]:  # 显示前10条
            md.append(f"1. [{item['type']}] {item['name']}")

        return "\n".join(md)