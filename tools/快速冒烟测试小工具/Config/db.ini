# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 11:06
# @Author : waxberry
# @File : db.py
# @Software : PyCharm

# 1. 在数据库（此处是oracle）拼接URL
# 1.1 创建存放url的表
# 查看后台存放主域名和路径的表
select t.*,t.rowid from eclp_A t orderby id desc;
select t.*,t.rowid from eclp_B t orderby id desc;

# 创建存放完整url的表
CREATETABLE eclp_uc_url (
ID NUMBER(20) DEFAULT0  NOTNULL ,
SUB_SYSTEM_ID  NUMBER(20) DEFAULT0  NOTNULL ,
SUB_SYSTEM_CODEVARCHAR2(100 BYTE) DEFAULT''  NULL ,
NAME  VARCHAR2(255 BYTE) DEFAULT''  NULL ,
DOMAINVARCHAR2(100 BYTE) DEFAULT''  NULL ,
PATH VARCHAR2(100 BYTE)DEFAULT''  NULL ,
URL  VARCHAR2(100 BYTE) DEFAULT''  NULL ,
ASSERT_WORD  VARCHAR2(255 BYTE) DEFAULT''  NULL
)

# 创建主键
ALTERTABLE eclp_uc_url ADDPRIMARYKEY (ID);


# 创建id自增序列
drop SEQUENCE SEQ_ECLP_UC_URL;
CREATE SEQUENCE SEQ_ECLP_UC_URL
INCREMENTBY1
START WITH1
MAXVALUE9999999999999
CYCLE
CACHE 20；


# 1.2 从两个表分别插入域名和路径到存放url的新表
# eclp的路径path插入表
INSERTINTO eclp_uc_url(id,SUB_SYSTEM_ID,NAME,PATH)
SELECT SEQ_ECLP_UC_URL.NEXTVAL,SUB_SYSTEM_ID,NAME,URL from eclp_A;

# eclp的域名domian插入表
updateeclp_uc_url set DOMAIN = (select DOMAIN from eclp_B whereeclp_uc_url.SUB_SYSTEM_ID = eclp_B.id)
whereexists (select 1 from eclp_B where eclp_uc_url.SUB_SYSTEM_ID =eclp_sub_system.id);

# 将domain和path拼接成url
MERGEINTO eclp_uc_url A
USING( select t.id, t.domain || '/' || t.path as urls from eclp_uc_url t) B ON (A.ID= B.ID)
WHENMATCHED THEN UPDATE SET A.URL = B.URLS;