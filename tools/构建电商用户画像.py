# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/20 9:31
# @Author : waxberry
# @File : 构建电商用户画像.py
# @Software : PyCharm

%matplotlab inline  #一个魔法函数，由于%matplotlib inline的存在，当输入plt.plot()后，不必再输入plt.show()，图像将自动显示出来。
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

# 02数据准备
# 导入数据集
df_orginal = pd.read_csv('./taobao_persona.csv')
# 抽取部分数据
df = df_orginal.sample(frac=0.2,random_state=None)

# 03数据预处理
# 查看其中是否有缺失值，统计各字段缺失值
df.isnull().any().sum()
# 发现只有user_geohash有缺失值，且缺失的比例很高，无统计分析的意义，将此列删除
df.drop('user_geohash',axis=1,inplace=True)
# 将time字段拆分为日期和时段
df['date'] = df['time'].str[0:10]
df['time'] = df['time'].str[11:]
df['time'] = df['time'].astype(int)
# date用str方法取0-9位的字符，time取11位到最后一位，将time转化成int类型。
# 将时段分为'凌晨','上午','中午','下午','晚上'
df['hour'] = pd.cut(df['time'],bins=[-1,5,10,13,18,24],labels=['凌晨','上午','中午','下午','晚上'])

# 生成用户标签表，制作好的标签都加入这个表中
users = df['user_id'].unique()
labels = pd.DataFrame(users,columns=['user_id'])


# 04数构建用户行为标签
# 1）对用户浏览时间段进行分析
# 对用户和时段分组，统计浏览次数
time_browse = df[df['behavior_type']==1].groupby(['user_id','hour']).item_id.count().reset_index()
time_browse.rename(columns={'item_id':'hour_counts'},inplace=True)
# 统计每个用户浏览次数最多的时段
time_browse_max = time_browse.groupby('user_id').hour_counts.max().reset_index()
time_browse_max.rename(columns={'hour_counts':'read_counts_max'},inplace=True)
time_browse = pd.merge(time_browse,time_browse_max,how='left',on='user_id')
# 之前已经按照user_id和hour进行了浏览物品次数的计数统计，现在借用浏览次数统计user_id在
# 哪个时间段浏览次数最多，并将其作为该用户的浏览时间标签的代表。
# 选取各用户浏览次数最多的时段，如有并列最多的时段，用逗号连接
time_browse_hour=time_browse.loc[time_browse['hour_counts']==time_browse['read_counts_max'],'hour'].groupby\
    (time_browse['user_id']).aggregate(lambda x:','.join(x)).reset_index()
time_browse_hour.head()
# 将用户浏览活跃时间段加入用户标签表中
labels = pd.merge(labels,time_browse_hour,how='left',on='user_id')
labels.rename(columns={'hour':'time_browse'},inplace=True)
# labels相当于一张考试卷纸，上面展示的都是最后处理好的结果

# 2）关于类目的用户行为
df_browse = df.loc[df['behavior_type']==1,['user_id','item_id','item_category']]
df_collect = df.loc[df['behavior_type']==2,['user_id','item_id','item_category']]
df_cart = df.loc[df['behavior_type']==3,['user_id','item_id','item_category']]
df_buy = df.loc[df['behavior_type']==4,['user_id','item_id','item_category']]

# 对用户与类目进行分组，统计浏览次数
df_cate_most_browse = df_browse.groupby(['user_id','item_category']).item_id.count().reset_index()
df_cate_most_browse.rename(columns={'item_id':'item_category_counts'},inplace=True)
# 统计每个用户浏览次数最多的类目
df_cate_most_browse_max=df_cate_most_browse.groupby('user_id').item_category_counts.max().reset_index()
df_cate_most_browse_max.rename(columns={'item_category_counts':'item_category_counts_max'},inplace=True)
df_cate_most_browse = pd.merge(df_cate_most_browse,df_cate_most_browse_max,how='left',on='user_id')
# 将item_category的数字类型改为字符串型
df_cate_most_browse['item_category'] = df_cate_most_browse['item_category'].astype(str)
# 选取各用户浏览次数最多的类目，如有并列最多的类目，用逗号连接
df_cate_browse=df_cate_most_browse.loc[df_cate_most_browse['item_category_counts']==df_cate_most_browse
['item_category_counts_max'],'item_category'].groupby(df_cate_most_browse['user_id']).aggregate(lambda x:','.join(x)).reset_index()
# 将用户浏览最多的类目加入用户标签表中
labels = pd.merge(labels,df_cate_browse,how='left',on='user_id')
labels.rename(columns={'item_category':'cate_most_browse'},inplace=True)
labels.head(5)

# 3）近30天用户行为分析。
# 将购买行为按用户进行分组，统计次数
df_counts_30_buy = df[df['behavior_type']==4].groupby('user_id').item_id.count().reset_index()
labels = pd.merge(labels,df_counts_30_buy,how='left',on='user_id')
labels.rename(columns={'item_id':'counts_30_buy'},inplace=True)

# 将加购行为按用户进行分组，统计次数
df_counts_30_cart = df[df['behavior_type']==3].groupby('user_id').item_id.count().reset_index()
labels = pd.merge(labels,df_counts_30_cart,how='left',on='user_id')
labels.rename(columns={'item_id':'counts_30_cart'},inplace=True)

# 对用户进行分组，统计活跃的天数，包括浏览、收藏、加购、购买
counts_30_active = df.groupby('user_id')['date'].nunique()
labels = pd.merge(labels,counts_30_active,how='left',on='user_id')
labels.rename(columns={'date':'counts_30_active'},inplace=True)
# 这里pd.nunique()是指返回的是唯一值的个数。

# 4）最后一次行为距今天数。
days_browse = df[df['behavior_type']==1].groupby('user_id')['date'].max().apply(lambda x:(datetime.strptime('2014-12-19','%Y-%m-%d')-x).days)
labels = pd.merge(labels,days_browse,how='left',on='user_id')
labels.rename(columns={'date':'days_browse'},inplace=True)

# 5）最近两次购买间隔天数。
df_interval_buy = df[df['behavior_type']==4].groupby(['user_id','date']).item_id.count().reset_index()
interval_buy = df_interval_buy.groupby('user_id')['date'].apply(lambda x:x.sort_values().diff(1).dropna().head(1)).reset_index()
interval_buy['date'] = interval_buy['date'].apply(lambda x:x.days)
interval_buy.drop('level_1', axis=1, inplace=True)
interval_buy.rename(columns={'date':'interval_buy'}, inplace=True)
labels = pd.merge(labels, interval_buy, how='left', on='user_id')

# 6）是否浏览未下单
df_browse_buy=df.loc[(df['behavior_type']==1)|(df['behavior_type']==4),
['user_id','item_id','behavior_type','time']]
browse_not_buy=pd.pivot_table(df_browse_buy,index=['user_id','item_id'],
columns=['behavior_type'],values=['time'],aggfunc=['count'])
browse_not_buy.columns = ['browse','buy']
browse_not_buy.fillna(0,inplace=True)
# 添加了一列browse_not_buy，初始值为0。
browse_not_buy['browse_not_buy'] = 0
# 浏览数>0,购买数=0的数据输出1.
browse_not_buy.loc[(browse_not_buy['browse']>0) & (browse_not_buy['buy']==0),'browse_not_buy'] = 1
browse_not_buy=browse_not_buy.groupby('user_id')['browse_not_buy'].sum().reset_index()
labels = pd.merge(labels,browse_not_buy,how='left',on='user_id')
labels['browse_not_buy'] = labels['browse_not_buy'].apply(lambda x: '是' if x>0else '否')

# 7）是否加购未下单
df_cart_buy=df.loc[(df['behavior_type']==3)|(df['behavior_type']==4),['user_id','item_id','behavior_type','time']]
cart_not_buy=pd.pivot_table(df_cart_buy,index=['user_id','item_id'],columns=['behavior_type'],values=['time'],aggfunc=['count'])
cart_not_buy.columns = ['cart','buy']
cart_not_buy.fillna(0,inplace=True)
cart_not_buy['cart_not_buy'] = 0
cart_not_buy.loc[(cart_not_buy['cart']>0) & (cart_not_buy['buy']==0),'cart_not_buy'] = 1
cart_not_buy = cart_not_buy.groupby('user_id')['cart_not_buy'].sum().reset_index()
labels = pd.merge(labels,cart_not_buy,how='left',on='user_id')
labels['cart_not_buy'] = labels['cart_not_buy'].apply(lambda x: '是' if x>0 else '否')


# 05构建用户属性标签
# 1）是否复购用户：
buy_again = df[df['behavior_type']==4].groupby('user_id')['item_id'].count().reset_index()
buy_again.rename(columns={'item_id':'buy_again'},inplace=True)
labels = pd.merge(labels,buy_again,how='left',on='user_id')
labels['buy_again'].fillna(-1,inplace=True)
# 未购买的用户标记为'未购买'，有购买未复购的用户标记为'否'，有复购的用户标记为'是'
labels['buy_again'] = labels['buy_again'].apply(lambda x: '是' if x>1 else  '否' if x==1 else '未购买')

# 2）访问活跃度：
user_active_level = labels['counts_30_active'].value_counts().sort_index(ascending=False)
plt.figure(figsize=(16,9))
user_active_level.plot(title='30天内访问次数与访问人数的关系',fontsize=18)
plt.ylabel('访问人数',fontsize=14)
plt.xlabel('访问次数',fontsize=14)
# 用于显示中文
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 先将user_active_level全部设置成高，再搜索数值<16的部分，设置成低
labels['user_active_level'] = '高'
labels.loc[labels['counts_30_active']<=16,'user_active_level'] = '低'

# 3）购买活跃度：
buy_active_level = labels['counts_30_buy'].value_counts().sort_index(ascending=False)
plt.figure(figsize=(16,9))
buy_active_level.plot(title='30天内购买次数与购买人数的关系',fontsize=18)
plt.ylabel('购买人数',fontsize=14)
plt.xlabel('购买次数',fontsize=14)
labels['buy_active_level'] = '高'
labels.loc[labels['counts_30_buy']<=14,'buy_active_level'] = '低'

# 4）购买的品类是否单一：
buy_single=df[df['behavior_type']==4].groupby('user_id').item_category.nunique().reset_index()
buy_single.rename(columns={'item_category':'buy_single'},inplace=True)
labels = pd.merge(labels,buy_single,how='left',on='user_id')
labels['buy_single'].fillna(-1,inplace=True)
labels['buy_single'] = labels['buy_single'].apply(lambda x: '是' if x>1 else  '否' if x==1 else '未购买' )

# 5）用户价值分组（RFM模型）：
last_buy_days = labels['days_buy'].value_counts().sort_index()
plt.figure(figsize=(16,9))
last_buy_days.plot(title='最后一次购买距今天数与购买人数的关系',fontsize=18)
plt.ylabel('购买人数',fontsize=14)
plt.xlabel('距今天数',fontsize=14)





# 使用RFM模型分析：
labels['buy_days_level'] = '高'
labels.loc[labels['days_buy']>8,'buy_days_level'] = '低'
labels['rfm_value'] = labels['buy_active_level'].str.cat(labels['buy_days_level'])
def trans_value(x):
    if x == '高高':
        return '重要价值客户'
    elif x == '低高':
        return '重要深耕客户'
    elif x == '高低':
        return '重要唤回客户'
    else:
        return '即将流失客户'
labels['rfm'] = labels['rfm_value'].apply(trans_value)
# 此处的apply()调用了一个自己定义（def）的函数
labels.drop(['buy_days_level','rfm_value'],axis=1,inplace=True)
labels['rfm'].value_counts()