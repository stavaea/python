# API 测试套件

## 环境要求
- Python 3.11+
- pytest
- requests
- allure-pytest

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行测试
```bash
pytest --alluredir=./allure-results
```

## 查看报告
```bash
allure serve ./allure-results
```

## 测试覆盖
- 用户认证（注册/登录）
- 产品管理
- 购物车管理
- 订单管理