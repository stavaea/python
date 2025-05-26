import re
import jieba
from typing import List, Dict

class TextPreprocessor:
    @staticmethod
    def clean_text(text: str) -> str:
        """基础文本清洗"""
        text = re.sub(r'[^\w\u4e00-\u9fff]+', ' ', text)  # 保留中英文和数字
        return text.strip()

    @staticmethod
    def segment_text(text: str) -> List[str]:
        """中文分词处理"""
        return [word for word in jieba.cut(text) if len(word) > 1]

    @staticmethod
    def detect_sentences(text: str) -> List[str]:
        """分句处理"""
        return [s.strip() for s in re.split(r'[。！？；\n]', text) if s.strip()]