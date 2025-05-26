# -*- coding: utf-8 -*-

from preprocessor import TextPreprocessor
from analyzer import TestAnalyzer
from generator import TestItemGenerator
from exporter import ResultExporter

with open('word.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def process_text(input_text: str, output_format: str = 'json'):
    # 文本预处理
    cleaned_text = TextPreprocessor.clean_text(input_text)

    # 智能分析
    analyzer = TestAnalyzer()
    analysis_result = analyzer.analyze(cleaned_text)

    # 生成测试项
    generator = TestItemGenerator()
    test_items = generator.generate(analysis_result)
    analysis_result['test_items'] = test_items

    # 结果输出
    if output_format == 'markdown':
        return ResultExporter.to_markdown(analysis_result)
    else:
        return ResultExporter.to_json(analysis_result)


if __name__ == "__main__":
    sample_text = text
    print(process_text(sample_text))