from typing import List, Dict

class TestItemGenerator:
    TEMPLATES = {
        'AUTH': {
            '正向': "验证{function}功能正常流程",
            '异常': "验证{function}异常情况处理"
        },
        'PAY': {
            '功能测试': "测试{function}流程完整性",
            '性能测试': "测量{function}响应时间"
        }
    }

    def generate(self, analysis_result: Dict) -> List[Dict]:
        test_cases = []
        for item in analysis_result['test_items']:
            for func in item['functions']:
                for dim in item['dimensions']:
                    template = self.TEMPLATES.get(func, {}).get(dim, "测试{function}的{dimension}要求")
                    test_case = {
                        'name': template.format(
                            function=func,
                            dimension=dim
                        ),
                        'type': dim,
                        'source': item['source'],
                        'tags': [func, dim]
                    }
                    test_cases.append(test_case)
        return test_cases