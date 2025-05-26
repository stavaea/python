from collections import defaultdict
import spacy
from typing import List, Dict

class TestAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("zh_core_web_sm")
        self.rule_db = {
            'functions': {
                '登录': 'AUTH',
                '注册': 'REG',
                '支付': 'PAY',
                '搜索': 'SEARCH'
            },
            'dimensions': {
                '验证': '功能测试',
                '性能': '性能测试',
                '安全': '安全测试'
            }
        }

    def analyze(self, text: str) -> Dict:
        """主分析方法"""
        doc = self.nlp(text)
        results = {
            'functions': defaultdict(list),
            'test_items': []
        }

        # 识别功能点和测试维度
        for sent in doc.sents:
            func_tags = self._extract_functions(str(sent))
            dim_tags = self._extract_dimensions(str(sent))

            if func_tags or dim_tags:
                test_item = {
                    'source': str(sent),
                    'functions': func_tags,
                    'dimensions': dim_tags
                }
                results['test_items'].append(test_item)

                for func in func_tags:
                    results['functions'][func].append(str(sent))

        return results

    def _extract_functions(self, text: str) -> List[str]:
        """基于规则和NLP识别功能点"""
        found = set()
        for kw, code in self.rule_db['functions'].items():
            if kw in text:
                found.add(code)

        # 补充名词识别
        doc = self.nlp(text)
        for token in doc:
            if token.pos_ == 'NOUN' and token.text in self.rule_db['functions']:
                found.add(self.rule_db['functions'][token.text])

        return sorted(found)

    def _extract_dimensions(self, text: str) -> List[str]:
        """识别测试维度"""
        return list(set(
            dim for kw, dim in self.rule_db['dimensions'].items()
            if kw in text
        ))