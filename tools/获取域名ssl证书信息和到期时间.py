# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/9/19 10:19
# @Author : waxberry
# @File : 获取域名ssl证书信息和到期时间.py
# @Software : PyCharm


# 1、通过openssl证书获取
'''openssl x509 -in <cert>.pem -noout -dates'''

# 2、通过openssl域名获取
'''echo | openssl s_client -servername <doman> -connect <doman>:443 2>/dev/null | openssl x509 -noout -dates'''

# 3、通过脚本获取curl
# coding: utf-8
# 查询域名证书到期情况

import re
import subprocess
from datetime import datetime
def get_re_match_result(pattern, string):
    match = re.search(pattern, string)
    return match.group(1)

def parse_time(date_str):
    return datetime.strptime(date_str, "%b %d %H:%M:%S %Y GMT")

def format_time(date_time):
    return datetime.strftime(date_time, "%Y-%m-%d %H:%M:%S")

def get_cert_info(domain):
    """获取证书信息"""
    cmd = f"curl -Ivs https://{domain} --connect-timeout 10"

    exitcode, output = subprocess.getstatusoutput(cmd)

    # 正则匹配
    start_date = get_re_match_result('start date: (.*)', output)
    expire_date = get_re_match_result('expire date: (.*)', output)

    # 解析匹配结果
    start_date = parse_time(start_date)
    expire_date = parse_time(expire_date)

    return {
        'start_date': start_date,
        'expire_date': expire_date
    }


def get_cert_expire_date(domain):
    """获取证书剩余时间"""
    info = get_cert_info(domain)
    print(info)

    expire_date = info['expire_date']

    # 剩余天数
    return (expire_date - datetime.now()).days


if __name__ == "__main__":
    domain = 'www.baidu.com'
    expire_date = get_cert_expire_date(domain)
    print(expire_date)

# 4、通过socket 获取域名ssl 证书信息
# 核心代码
# -*- coding: utf-8 -*-

import socket
import ssl


def get_domain_cert(domain):
    """
    获取证书信息
    :param domain: str
    :return: dict
    """
    socket.setdefaulttimeout(5)

    cxt = ssl.create_default_context()
    skt = cxt.wrap_socket(socket.socket(), server_hostname=domain)

    skt.connect((domain, 443))
    cert = skt.getpeercert()

    skt.close()

    return cert


if __name__ == "__main__":
    print(get_domain_cert("www.baidu.com"))

# 还有一种方式也记录一下

import socket
import ssl


def get_domain_cert(host, port=443, timeout=3):
    """
    获取证书信息
    存在问题：没有指定主机ip，不一定能获取到正确的证书信息
    :param host: str
    :param port: int
    :param timeout: int
    :return: dict
    """
    context = ssl.create_default_context()

    with socket.create_connection(address=(host, port), timeout=timeout) as sock:
        with context.wrap_socket(sock, server_hostname=host) as wrap_socket:
            return wrap_socket.getpeercert()

# 结构化输出内容后的完整代码
# -*- coding: utf-8 -*-

import socket
import ssl

from dateutil import parser

# requests.packages.urllib3.disable_warnings()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

socket.setdefaulttimeout(5)


def get_domain_ip(domain):
    """
    获取ip地址
    :param domain: str
    :return: str
    """
    try:
        addrinfo = socket.getaddrinfo(domain, None)
        return addrinfo[0][-1][0]
    except Exception as e:
        pass

    return None


def get_domain_cert(domain):
    """
    获取证书信息
    :param domain: str
    :return: dict
    """
    cxt = ssl.create_default_context()
    skt = cxt.wrap_socket(socket.socket(), server_hostname=domain)

    skt.connect((domain, 443))
    cert = skt.getpeercert()
    skt.close()

    return cert


def get_cert_info(domain):
    """
    获取证书信息
    :param domain: str
    :return: dict
    """
    cert = get_domain_cert(domain)

    issuer = _tuple_to_dict(cert['issuer'])
    subject = _tuple_to_dict(cert['subject'])

    return {
        'domain': domain,
        'ip': get_domain_ip(domain),
        'subject': _name_convert(subject),
        'issuer': _name_convert(issuer),
        # 'version': cert['version'],
        # 'serial_number': cert['serialNumber'],
        'start_date': _parse_time(cert['notBefore']),
        'expire_date': _parse_time(cert['notAfter']),
    }


def _tuple_to_dict(cert_tuple):
    """
    cert证书 tuple转dict
    :param cert_tuple: tuple
    :return:
    """
    data = {}
    for item in cert_tuple:
        data[item[0][0]] = item[0][1]

    return data


def _name_convert(data):
    """
    名字转换
    :param data: dict
    :return: dict
    """
    name_map = {
        'C': 'countryName',
        'CN': 'commonName',
        'O': 'organizationName',
        'OU': 'organizationalUnitName',
        'L': 'localityName',
        'ST': 'stateOrProvinceName'
    }

    dct = {}
    for key, value in name_map.items():
        dct[key] = data.get(value, '')

    return dct


def _parse_time(time_str):
    """
    解析并格式化时间
    :param time_str: str
    :return: str
    """
    return parser.parse(time_str).astimezone().strftime(DATETIME_FORMAT)


if __name__ == "__main__":
    print(get_cert_info("www.baidu.com"))


# 5、通过pyOpenSSL获取证书信息
# 依赖
# pip install pyOpenSSL
# 示例
# -*- coding: utf-8 -*-

import ssl
import OpenSSL

def get_ssl_expire_date(host, port=443):
    cert = ssl.get_server_certificate((host, port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    return x509.get_notAfter().decode()


if __name__ == '__main__':
    print(get_ssl_expire_date('www.baidu.com'))
    # 20230806051601Z


# 6、Domain Admin可视化管理域名证书到期
'''
项目地址：https://github.com/mouday/domain-admin

运行环境：Python 3.7.0

$ pip install domain_admin

# 升级到最新版本，可选
$ pip3 install -U domain-admin -i https://pypi.org/simple

# 启动运行
$ gunicorn 'domain_admin.main:app'
访问地址：http://127.0.0.1:8000

默认的管理员账号：admin 密码：123456
'''