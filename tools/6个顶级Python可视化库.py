# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2024/1/19 9:41
# @Author : waxberry
# @File : 6个顶级Python可视化库.py
# @Software : PyCharm


# 为了探索每幅图表，将使用GitHub用户的数据：
import pandas as pd
import sns

# 强烈推荐关注@公众号：数据STUDIO，更多优质内容等你～
new_profile = pd.read_csv('https://gist.githubusercontent.com/khuyentran1401/98658198f0ef0cb12abb34b4f2361fd8/raw/ece16eb32e1b41f5f20c894fb72a4c198e86a5ea/github_users.csv')
new_profile



# Matplotlib
# 检查拥有最多粉丝的前100名用户的分布情况
import matplotlib.pyplot as plt

top_followers = new_profile.sort_values(by="followers", axis=0, ascending=False)[:100]
fig = plt.figure()
plt.bar(top_followers.user_name, top_followers.followers)
plt.show()

# 生成各种类型的图形。Matplotlib的网站[2]提供了全面的文档和各种图形的图库
fig = plt.figure()
plt.text(
    0.6,
    0.7,
    "learning",
    size=40,
    rotation=20.0,
    ha="center",
    va="center",
    bbox=dict(
        boxstyle="round",
        ec=(1.0, 0.5, 0.5),
        fc=(1.0, 0.8, 0.8),
    ),
)
plt.text(
    0.55,
    0.6,
    "machine",
    size=40,
    rotation=-25.0,
    ha="right",
    va="top",
    bbox=dict(
        boxstyle="square",
        ec=(1.0, 0.5, 0.5),
        fc=(1.0, 0.8, 0.8),
    ),
)
plt.show()

# 向他人展示数据，定制X轴、Y轴和其他绘图元素可能需要大量的努力。这是由于Matplotlib的低级接口造成的。
num_features = new_profile.select_dtypes("int64")
correlation = num_features.corr()
fig, ax = plt.subplots()
im = plt.imshow(correlation)
ax.set_xticklabels(correlation.columns)
ax.set_yticklabels(correlation.columns)
plt.setp(ax.get_xticklabels(),
        rotation=45,
        ha="right",
        rotation_mode="anchor")
plt.show()





# Seaborn
# 创建一个热图，而无需明确设置x和y标签：
correlation = new_profile.corr()
sns.heatmap(correlation, annot=True)

# Seaborn的默认设置，计数图在视觉上显得更加吸引人：
sns.set(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=titanic)




# Plotly
# 用一行Python代码就能创建令人印象深刻的图表。比如说：
import plotly.express as px
# 强烈推荐关注@公众号：数据STUDIO，更多优质内容等你～
fig = px.scatter(
    new_profile[:100],
    x="followers",
    y="total_stars",
    color="forks",
    size="contribution",
)
fig.show()

# 用Plotly实现的前面的用Matplotlib创建的条形图例子
top_followers = new_profile.sort_values(by="followers", axis=0, ascending=False)[:100]
fig = px.bar(
    top_followers,
    x="user_name",
    y="followers",
)
fig.show()

# 在地图上可视化GitHub用户的位置，我们可以获得他们的经纬度，并据此绘制：
location_df = pd.read_csv(
    "https://gist.githubusercontent.com/khuyentran1401/ce61bbad3bc636bf2548d70d197a0e3f/raw/ab1b1a832c6f3e01590a16231ba25ca5a3d761f3/location_df.csv",
    index_col=0,
)
m = px.scatter_geo(
    location_df,
    lat="latitude",
    lon="longitude",
    color="total_stars",
    size="forks",
    hover_data=["user_name", "followers"],
    title="Locations of Top Users",
)
m.show()




# Altair
# 使用泰坦尼克号的数据集来计算每个班级的人数：
import seaborn as sns
import altair as alt
titanic = sns.load_dataset("titanic")
alt.Chart(titanic).mark_bar().encode(alt.X("class"), y="count()")

# 在泰坦尼克号数据集中找到每个性别的平均年龄，你可以在代码本身中进行转换：
hireable = (
    alt.Chart(titanic)
    .mark_bar()
    .encode(x="sex:N", y="mean_age:Q")
    .transform_aggregate(mean_age="mean(age)", groupby=["sex"])
)
hireable

# 在散点图上直观地显示所选区间内每个阶层的人数：
brush = alt.selection(type="interval")
points = (
    alt.Chart(titanic)
    .mark_point()
    .encode(
        x="age:Q",
        y="fare:Q",
        color=alt.condition(brush, "class:N", alt.value("lightgray")),
    )
    .add_selection(brush)
)
bars = (
    alt.Chart(titanic)
    .mark_bar()
    .encode(y="class:N", color="class:N", x="count(class):Q")
    .transform_filter(brush)
)
points & bars





# Bokeh
# Matplotlib的圆形图...
import matplotlib.pyplot as plt
# 强烈推荐关注@公众号：数据STUDIO，更多优质内容等你～
fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5]
y = [2, 5, 8, 2, 7]
for x, y in zip(x, y):
    ax.add_patch(
        plt.Circle((x, y), 0.5, edgecolor="#f03b20", facecolor="#9ebcda", alpha=0.8)
    )
# Use adjustable='box-forced' to make the plot area square-shaped as well.
ax.set_aspect("equal", adjustable="datalim")
ax.set_xbound(3, 4)
ax.plot()  # Causes an autoscale update.
plt.show()

# 通过使用虚化技术实现更好的分辨率和更大的效用：
from bokeh.io import show, output_notebook
from bokeh.models import Circle
from bokeh.plotting import figure

output_notebook()
plot = figure(tools="tap", title="Select a circle")
renderer = plot.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=50)
selected_circle = Circle(fill_alpha=1, fill_color="firebrick", line_color=None)
nonselected_circle = Circle(fill_alpha=0.2, fill_color="blue", line_color="firebrick")
renderer.selection_glyph = selected_circle
renderer.nonselection_glyph = nonselected_circle
show(plot)

# 如果创建了三个并排的图形，并想观察它们的关系，你可以利用链接刷：
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource

source = ColumnDataSource(new_profile)
TOOLS = "box_select,lasso_select,help"
TOOLTIPS = [
    ("user", "@user_name"),
    ("followers", "@followers"),
    ("following", "@following"),
    ("forks", "@forks"),
    ("contribution", "@contribution"),
]
s1 = figure(tooltips=TOOLTIPS, title=None, tools=TOOLS)
s1.circle(x="followers", y="following", source=source)

s2 = figure(tooltips=TOOLTIPS, title=None, tools=TOOLS)
s2.circle(x="followers", y="forks", source=source)

s3 = figure(tooltips=TOOLTIPS, title=None, tools=TOOLS)
s3.circle(x="followers", y="contribution", source=source)
p = gridplot([[s1, s2, s3]])
show(p)

# 如果不为条形图增加宽度，图表会是这样的：
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

titanic_groupby = titanic.groupby("class")["survived"].sum().reset_index()
p = figure(x_range=list(titanic_groupby["class"]))
p.vbar(
    x="class",
    top="survived",
    source=titanic_groupby,
    fill_color=factor_cmap(
        "class", palette=Spectral6, factors=list(titanic_groupby["class"])
    ),
)
show(p)

from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
titanic_groupby = titanic.groupby("class")["survived"].sum().reset_index()
p = figure(x_range=list(titanic_groupby["class"]))
p.vbar(
    x="class",
    top="survived",
    source=titanic_groupby,
    fill_color=factor_cmap(
        "class", palette=Spectral6, factors=list(titanic_groupby["class"])
    ),
)
show(p)

# 因此，需要手动调整尺寸以使绘图更美观：
p = figure(x_range=list(titanic_groupby["class"]))
p.vbar(
    x="class",
    top="survived",
    width=0.9,
    source=titanic_groupby,
    fill_color=factor_cmap(
        "class", palette=Spectral6, factors=list(titanic_groupby["class"])
    ),
)
show(p)





# Folium
# 用Plotly创建的可视化Github用户位置的地图,有了Folium，可以进一步增强地图的外观。
import folium

# 在一个列表中保存纬度、经度和地点的名称*
lats = location_df["纬度"]
lons = location_df["经度"]
names = location_df["location"]
# 用一个初始位置创建一个地图*
m = folium.Map(location=[lats[0], lons[0]] )
for lat, lon, name in zip(lats, lons, names):
  # 用其他位置创建标记*
  folium.Marker(
    location=[lat, lon], popup=name, icon=folium.Icon(color="green")
  ).add_to(m)
m

# 添加地点
# Folium通过允许加入标记，可以很容易地添加其他用户的潜在位置。
# 启用在地图中添加更多的位置
m = m.add_child(folium.ClickForMarker(popup="Potential Location"))

# 将全球Github用户的总星数热图可视化，并识别出拥有大量顶级用户和星数的地区，Folium热图插件就可以实现这一目的。
# heatmap
# 强烈推荐关注@公众号：数据STUDIO，更多优质内容等你～
from folium.plugins import HeatMap

m = folium.Map(location=[lats[0], lons[0]])
HeatMap(data=location_df[["latitude", "longitude", "total_stars"]]).add_to(m)
m

