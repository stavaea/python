# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/8/30 10:22
# @Author : waxberry
# @File : Matplotlib实操指南.py
# @Software : PyCharm

'''导读
Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。
通过 Matplotlib，开发者可以仅需要几行代码，便可以生成绘图，直方图，功率谱，条形图，错误图，散点图等。
以下内容来自「Github」，为《PythonDataScienceHandbook[1]》(Python 数据科学手册[2])第四章「Matplotlib」介绍部分。全部内容都在以下环境演示通过：
numpy:1.18.5
pandas:1.0.5
matplotlib:3.2.1'''

# 1.简单的折线图
# 对于图表来说，最简单的莫过于作出一个单一函数的图像。都会使用下面的代码将我们需要的包载入到 notebook 中：
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# 图形和维度可以使用下面代码进行最简形式的创建：
fig = plt.figure()
ax = plt.axes()

'''在 Matplotlib 中，图形（类plt.Figure的一个实例）可以被认为是一个包括所有维度、图像、文本和标签对象的容器。
维度（类plt.Axes的一个实例）就是你上面看到的图像，一个有边界的格子包括刻度和标签，最终还有我们画在上面的图表元素。
在本书中，我们会使用变量名fig来指代图形对象，以及变量名ax来指代维度变量。'''

# 下面是一个简单的正弦函数图形：
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))

# 同样的，使用 pylab 接口（MATLAB 风格的接口）在后台自动创建这两个对象：
plt.plot(x, np.sin(x))

# 如果需要在同一幅图形中绘制多根线条，只需要多次调用plot函数即可：
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
# 这就是在 Matplotlib 中绘制简单函数图像的所有接口了

# 调整折线图：线条颜色和风格
'''
plt.plot()函数接受额外的参数可以用来指定它们。
通过指定color关键字参数可以调整颜色，这个字符串类型参数基本上能用来代表任何能想到的颜色。
可以通过多种方式指定颜色参数：'''

# 所有 HTML 颜色名称可以在这里[3]找到。
plt.plot(x, np.sin(x - 0), color='blue')        # 通过颜色名称指定
plt.plot(x, np.sin(x - 1), color='g')           # 通过颜色简写名称指定(rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # 介于0-1之间的灰阶值
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # 16进制的RRGGBB值
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB元组的颜色值，每个值介于0-1
plt.plot(x, np.sin(x - 5), color='chartreuse') # 能支持所有HTML颜色名称值

# 如果没有指定颜色，Matplotlib 会在一组默认颜色值中循环使用来绘制每一条线条。
# 类似的，通过linestyle关键字参数可以指定线条的风格：
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')
# 还可以用形象的符号代表线条风格
plt.plot(x, x + 4, linestyle='-')  # 实线
plt.plot(x, x + 5, linestyle='--') # 虚线
plt.plot(x, x + 6, linestyle='-.') # 长短点虚线
plt.plot(x, x + 7, linestyle=':')  # 点线

# 如果喜欢更简洁的代码，这些linestyle和color参数能够合并成一个非关键字参数，传递给plt.plot()函数：
plt.plot(x, x + 0, '-g')  # 绿色实线
plt.plot(x, x + 1, '--c') # 天青色虚线
plt.plot(x, x + 2, '-.k') # 黑色长短点虚线
plt.plot(x, x + 3, ':r')  # 红色点线

# 上面的单字母颜色码是 RGB 颜色系统以及 CMYK 颜色系统的缩写，被广泛应用在数字化图像的颜色系统中。
# 还有很多其他的关键字参数可以对折线图的外观进行精细调整；可以通过在 IPython 中使用帮助工具查看plt.plot()函数的文档来获得更多细节内容。

# 调整折线图：坐标轴范围
'''Matplotlib 会自动选择非常合适的坐标轴范围来绘制你的图像，但是有些情况下你也需要自己进行相关调整。
使用plt.xlim()和plt.ylim()函数可以调整坐标轴的范围：'''

plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

# 如果某些情况下将坐标轴反向，可以通过上面的函数实现，将参数顺序颠倒即可：
plt.plot(x, np.sin(x))

plt.xlim(10, 0)
plt.ylim(1.2, -1.2)

# 相关的函数还有plt.axis()（注意：这不是plt.axes()函数，函数名称是 i 而不是 e）。
# 这个函数可以在一个函数调用中就完成 x 轴和 y 轴范围的设置，传递一个[xmin, xmax, ymin, ymax]的列表参数即可：
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5])

# 当然plt.axis()函数不仅能设置范围，还能像下面代码一样将坐标轴压缩到刚好足够绘制折线图像的大小：
plt.plot(x, np.sin(x))
plt.axis('tight')

# 还可以通过设置'equal'参数设置x轴与y轴使用相同的长度单位：
plt.plot(x, np.sin(x))
plt.axis('equal')
# 更多关于设置 axis 属性的内容请查阅plt.axis函数的文档字符串。

# 折线图标签
# 标题和坐标轴标签是最简单的这类标签，Matplotlib 提供了函数用来方便的设置它们：
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")

# 虽然有很多种正确的方法来指定图例，最简单的方法是通过在绘制每条线条时指定对应的label关键字参数来使用这个函数：
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend()

'''虽然大多数的plt函数都可以直接转换为ax的方法进行调用（例如plt.plot() → ax.plot()，plt.legend() → ax.legend()等），但是并不是所有的命令都能应用这种情况。
特别是用于设置极值、标签和标题的函数都有一定的改变。下表列出了将 MATLAB 风格的函数转换为面向对象的方法的区别：
plt.xlabel() → ax.set_xlabel()
plt.ylabel() → ax.set_ylabel()
plt.xlim() → ax.set_xlim()
plt.ylim() → ax.set_ylim()
plt.title() → ax.set_title()'''
# 在面向对象接口中，与其逐个调用上面的方法来设置属性，更常见的使用ax.set()方法来一次性设置所有的属性：
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot')

# 2.简单散点图

%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
# 使用 plt.plot 绘制散点图
# plt.plot/ax.plot方法绘制折线图。这两个方法也可以同样用来绘制散点图：
x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black')
# 下面的例子可以展示那些最通用的符号：
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

# 而且这些符号代码可以和线条、颜色代码一起使用，这会在折线图的基础上绘制出散点：
plt.plot(x, y, '-ok')
# plt.plot还有很多额外的关键字参数用来指定广泛的线条和点的属性：
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)

# 使用plt.scatter绘制散点图
# 第二种更强大的绘制散点图的方法是使用plt.scatter函数，它的使用方法和plt.plot类似：
plt.scatter(x, y, marker='o')

# plt.scatter和plt.plot的主要区别在于，plt.scatter可以针对每个点设置不同属性（大小、填充颜色、边缘颜色等），还可以通过数据集合对这些属性进行设置。
# 通过一个随机值数据集绘制不同颜色和大小的散点图来说明。为了更好的查看重叠的结果，使用alpha关键字参数对点的透明度进行了调整：
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()  # 显示颜色对比条

'''注意图表右边有一个颜色对比条（这里通过colormap()函数输出），图表中的点大小的单位是像素。
使用这种方法，散点的颜色和大小都能用来展示数据信息，在希望展示多个维度数据集合的情况下很直观。'''

# 例如，使用 Scikit-learn 中的鸢尾花数据集，里面的每个样本都是三种鸢尾花中的其中一种，并带有仔细测量的花瓣和花萼的尺寸数据：
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

'''从上图中看出，可以通过散点图同时展示该数据集的四个不同维度：图中的(x, y)位置代表每个样本的花萼的长度和宽度，
散点的大小代表每个样本的花瓣的宽度，而散点的颜色代表一种特定的鸢尾花类型。如上图的多种颜色和多种属性的散点图对于分析和展示数据集时都非常有帮助。'''

# plot 和 scatter 对比：性能提醒
'''除了上面说的plt.plot和plt.scatter对于每个散点不同属性的支持不同之外，还有别的因素影响对这两个函数的选择吗？
对于小的数据集来说，两者并无差别，当数据集增长到几千个点时，plt.plot会明显比plt.scatter的性能要高。

造成这个差异的原因是plt.scatter支持每个点使用不同的大小和颜色，因此渲染每个点时需要完成更多额外的工作。

而plt.plot来说，每个点都是简单的复制另一个点产生，因此对于整个数据集来说，确定每个点的展示属性的工作仅需要进行一次即可。
对于很大的数据集来说，这个差异会导致两者性能的巨大区别，因此，对于大数据集应该优先使用plt.plot函数。'''

# 3.误差可视化
# 基础误差条
# 调用一个 Matplotlib 函数就能创建一个基础的误差条：
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='.k')

# 这里的fmt参数是用来控制线条和点风格的代码，与plt.plot有着相同的语法，

'''除了上面的基本参数，errorbar函数还有很多参数可以用来精细调节图表输出。
使用这些参数你可以很容易的个性化调整误差条的样式。通常将误差线条颜色调整为浅色会更加清晰，特别是在数据点比较密集的情况下：'''

plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)
# 除了上面介绍的参数，还可以指定水平方向的误差条（xerr），单边误差条和其他很多的参数。

# 连续误差
'''在某些情况下可能需要对连续值展示误差条。虽然 Matplotlib 没有內建的函数能直接完成这个任务，但是可以通过简单将plt.plot和plt.fill_between函数结合起来达到目标。
这里会采用简单的高斯过程回归方法，Scikit-Learn 提供了 API。这个方法非常适合在非参数化的函数中获得连续误差。我们在这里不会详细介绍高斯过程回归，仅仅聚焦在如何绘制连续误差本身：
译者注：新版的 sklearn 修改了高斯过程回归实现方法，下面代码做了相应修改。'''
from sklearn.gaussian_process import GaussianProcessRegressor
# 定义模型和一些符合模型的点
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# 计算高斯过程回归，使其符合 fit 数据点
gp = GaussianProcessRegressor()
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, std = gp.predict(xfit[:, np.newaxis], return_std=True)
dyfit = 2 * std  # 两倍sigma ~ 95% 确定区域
# 使用plt.fill_between函数在误差限区域内填充一道浅色的误差带来展示连续误差：
# 可视化结果
plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')

plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
                 color='gray', alpha=0.2)
plt.xlim(0, 10)
# 在观测点的附近，模型会被限制在一个很小的区域内，反映了这些数据的误差比较小。在远离观测点的区域，模型开始发散，反映了这时的数据误差比较大。

# 4.密度和轮廓图
'''在二维图表中使用轮廓或颜色区域来展示三维的数据（可以设想等高线地图或温度分布图）。
Matplotlib 提供了三个有用的函数来处理这项任务：plt.contour绘制轮廓图，plt.contourf来绘制填充区域颜色的图表以及plt.imshow来展示图像。'''
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
# 三维可视化函数
# 首先使用一个简单的函数  绘制一个轮廓图来进行说明，用来作为数组广播运算的例子：
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
# 轮廓图可以使用plt.contour函数进行创建。
# 可以将两个一维的数组构造成一个二维的网格：
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 下面绘制标准的轮廓线图表：
plt.contour(X, Y, Z, colors='black')

'''值得注意的是，当使用单色绘制轮廓图时，虚线代表的是负数的数值，而实线代表的是正数。
下例中展示了使用色图且绘制了更多的轮廓线的例子，会在整个数据范围区域内等距分布有 20 条轮廓线：'''
plt.contour(X, Y, Z, 20, cmap='RdGy')
# Matplotlib 有大量的颜色图可供使用，你可以通过在 IPython 中对plt.cm模块使用 TAB 自动补全方法就可以看到：
plt.cm.<TAB>
# 改为填充轮廓图来解决这个问题，使用plt.contourf()函数（注意函数名最后有个 f，代表填充 fill），这个函数的语法基本上与plt.contour()保持一致。
# 并且加上了plt.colorbar()函数，这个函数会在图表边上创建一个颜色图例用以展示颜色所表示的数值区域：
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()

# 有了图例，很容易可以看出黑色区域代表着“峰”，而红色区域代表这“谷”。

# 通过设置很高的轮廓线数量来改善，但是这会导致绘制图表的性能降低：Matplotlib 必须在每个颜色阶梯上绘制一条新的轮廓多边形。
# 更好的办法是使用plt.imshow()函数，它会将一个二维的网格图表转换为一张图像。

# 下面的例子展示了该方法：

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image')

'''然而，在使用imshow()的时候也有一些坑：

plt.imshow()不接受 x 和 y 网格值作为参数，因此你需要手动指定extent参数[xmin, xmax, ymin, ymax]来设置图表的数据范围。
plt.imshow()使用的是默认的图像坐标，即左上角坐标点是原点，而不是通常图表的左下角坐标点。这可以通过设置origin参数来设置。
plt.imshow()会自动根据输入数据调整坐标轴的比例；这可以通过参数来设置，例如，plt.axis(aspect='image')能让 x 和 y 轴的单位一致。
最后，有时可能需要将轮廓图和图像结合起来。'''
# 例如，下例中使用了半透明的背景图像（通过alpha参数设置透明度），然后在背景图层之上绘制了轮廓图，并带有每个轮廓的数值标签（使用plt.clabel()函数绘制标签）：
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy', alpha=0.5)
plt.colorbar()

# 通过组合使用plt.contour、plt.contourf和plt.imshow这三个函数，基本可以满足绘制所有这种在二维图标上的三维数据的需求。

# 5.直方图，分桶和密度
# 前面看到了 Matplotlib 的直方图函数，我们可以用一行代码绘制基础的直方图，当然首先需要将需要用的包导入 notebook：
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data)

# hist()函数有很多的参数可以用来调整运算和展示；下面又一个更加个性化的直方图展示：
plt.hist(data, bins=30, density=True, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='none')

# 联合使用histtype='stepfilled'和alpha参数设置透明度在对不同分布的数据集进行比较展示时很有用：
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

# 如果只是需要计算直方图的数值（即每个桶的数据点数量）而不是展示图像，np.histogram()函数可以完成这个目标：

counts, bin_edges = np.histogram(data, bins=5)
print(counts)

# 二维直方图和分桶
# 也可以在二维上使用数据对应的点来划分桶。首先定义数据集，从多元高斯分布中获得x和y数组：
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T
# plt.hist2d：二维直方图
# 绘制二维直方图最直接的方法是使用 Matplotlib 的plt.hist2d函数：

plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

# 而且，plt.hist有np.histogram，plt.hist2d也有其对应的函数np.histogram2d。如下例：

counts, xedges, yedges = np.histogram2d(x, y, bins=30)

# plt.hexbin：六角形分桶
'''刚才的二维分桶是沿着坐标轴将每个桶分为正方形。
另一个很自然的分桶形状就是正六边形。对于这个需求，Matplotlib 提供了plt.hexbin函数，它也是在二维平面上分桶展示，不过每个桶（即图表上的每个数据格）将会是六边形：'''
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')

# 核密度估计
# 下面就一个简单的例子来说明如何使用 KDE 和绘制相应的二维直方图：
from scipy.stats import gaussian_kde

# 产生和处理数据，初始化KDE
data = np.vstack([x, y])
kde = gaussian_kde(data)

# 在通用的网格中计算得到Z的值
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# 将图表绘制成一张图像
plt.imshow(Z.reshape(Xgrid.shape),
           origin='lower', aspect='auto',
           extent=[-3.5, 3.5, -6, 6],
           cmap='Blues')
cb = plt.colorbar()
cb.set_label("density")

# 6.自定义图标图例
# 在 Matplotlib 中自定义图例的位置和进行美化的方法。
# 可以使用plt.legend()函数来创建最简单的图例，这个函数能自动创建任何带有标签属性的图表元素的图例：
import matplotlib.pyplot as plt
plt.style.use('classic')
%matplotlib inline
import numpy as np
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-b', label='Sine')
ax.plot(x, np.cos(x), '--r', label='Cosine')
ax.axis('equal')
leg = ax.legend()

# 例如，可以指定图例位置并且去除边框：
ax.legend(loc='upper left', frameon=False)
fig

# 可以使用ncol属性设置图例中每行的列数：
ax.legend(frameon=False, loc='lower center', ncol=2)
fig

# 还可以使用圆角方框（fancybox）或者增加阴影，设置方框的透明度（alpha 值）或修改文字的边距：
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
fig

# 选择设置图例的元素
# plt.plot函数能够同时产生多条折线，然后将这些线条的实例列表返回。将其中的部分实例传递到plt.legend()函数就能设置哪些线条会出现在图例中，再通过一个标签的列表指定图例的名称：
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)

# lines是一个线条实例的列表
plt.legend(lines[:2], ['first', 'second'])
# 通过将标签应用在图表元素上，然后绘制到图例中：
plt.plot(x, y[:, 0], label='first')
plt.plot(x, y[:, 1], label='second')
plt.plot(x, y[:, 2:])
plt.legend(framealpha=1, frameon=True)

# 散点大小的图例
# 在使用散点的大小来标记数据的某个特征，然后希望创建一个相应的图例。
'''下面的例子是加州城市人口的散点图，使用散点的大小表现该城市的面积，散点的颜色来表现城市的人口数量（自然对数值）。
使用一个图例来指明散点尺寸的比例，同时用一个颜色条来说明人口数量，可以通过自定义绘制一些标签数据来实现尺寸图例：'''
import pandas as pd
cities = pd.read_csv(r'D:\python\Github学习材料\Python数据科学手册\data\california_cities.csv')

# 提取我们感兴趣的数据
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# 绘制散点图，使用尺寸代表面积，颜色代表人口，不带标签
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis('scaled')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# 下面我们创建图例：
# 使用空列表绘制图例中的散点，使用不同面积和标签，带透明度
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area,
                label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')

plt.title('California Cities: Area and Population')

# 多重图例
# 有时候需要在同一个图表维度中设计多个图例。不幸的是，Matplotlib 并没有提供很简单的方式实现：通过标准的legend接口，只能在整张图表上创建一个图例。
'''如果试图使用plt.legend()或ax.legend()创建第二个图例，那么第二条语句创建的图例会覆盖第一条语句创建的。
只能通过从底层开始来创建一个新的图例 artist 这种方法来解决这个问题，然后使用ax.add_artist()的底层方法手动将第二个作者加到图表上：'''
fig, ax = plt.subplots()

lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                     styles[i], color='black')
ax.axis('equal')

# 指定第一个图例的线条和标签
ax.legend(lines[:2], ['line A', 'line B'],
          loc='upper right', frameon=False)

# 手动创建第二个图例，并将作者添加到图表中
from matplotlib.legend import Legend
leg = Legend(ax, lines[2:], ['line C', 'line D'],
             loc='lower right', frameon=False)
ax.add_artist(leg)

# 7.个性化颜色条
import matplotlib.pyplot as plt
plt.style.use('classic')
%matplotlib inline
import numpy as np
# 通过plt.colorbar函数可以创建最简单的颜色条：
x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

plt.imshow(I)
plt.colorbar()
# 自定义颜色条
# 颜色条可以通过cmap参数指定使用的色谱系统（或叫色图）：
plt.imshow(I, cmap='gray')
# 在 IPython 中使用 Tab 自动补全功能能列出所有的色图列表：
plt.cm.<TAB>

# 选择色图
# 通过将jet颜色条转换为黑白来看到这点：
from matplotlib.colors import LinearSegmentedColormap

def grayscale_cmap(cmap):
    """返回给定色图的灰度版本"""
    cmap = plt.cm.get_cmap(cmap) # 使用名称获取色图对象
    colors = cmap(np.arange(cmap.N)) # 将色图对象转为RGBA矩阵，形状为N×4

    # 将RGBA颜色转换为灰度
    # 参考 http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114] # RGB三色的权重值
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight)) # RGB平方值和权重的点积开平方根
    colors[:, :3] = luminance[:, np.newaxis] # 得到灰度值矩阵
    # 返回相应的灰度值色图
    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    """将色图对应的灰度版本绘制出来"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
view_colormap('jet')
# 无论是在彩色图中还是在灰度图中都有着同样的亮度变化：
view_colormap('viridis')

# 如果更喜欢彩虹方案，另一个好的选择是使用cubehelix色图：
view_colormap('cubehelix')

# 如果将双色颜色条转化为灰度的话，正负或两级的信息就会丢失：
view_colormap('RdBu')

# 颜色限制和扩展
# 颜色条也有着一些有趣的自定义行为：例如，可以缩小颜色的范围并且通过设置extend参数将超出范围之外的数值展示为顶部和底部的三角箭头形状：

# 在I数组中人为生成不超过1%的噪声
speckles = (np.random.random(I.shape) < 0.01)
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

plt.figure(figsize=(10, 3.5))
# 不考虑去除噪声时的颜色分布
plt.subplot(1, 2, 1)
plt.imshow(I, cmap='RdBu')
plt.colorbar()
# 设置去除噪声时的颜色分布
plt.subplot(1, 2, 2)
plt.imshow(I, cmap='RdBu')
plt.colorbar(extend='both')
plt.clim(-1, 1)

# 离散颜色条
# 最简单的方法是使用plt.cm.get_cmap()函数，在传递某个色图名称的同时，还额外传递一个颜色分桶的数量值参数给该函数：
plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(-1, 1)

# 例子：手写数字
# 首先，下载这个数据集，然后使用plt.imshow()将其中部分数据展示出来：

# 读取数字0-5的手写图像，然后使用Matplotlib展示头64张缩略图
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)

fig, ax = plt.subplots(8, 8, figsize=(6, 6))
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])
# 将这些手写数字图像数据映射到二维流形学习当中：

# 使用Isomap将手写数字图像映射到二维流形学习中
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)
# 使用离散颜色条来展示结果，设置ticks和clim来进一步美化结果的颜色条：

# 绘制图表结果
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1,
            c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6))
plt.colorbar(ticks=range(6), label='digit value')
plt.clim(-0.5, 5.5)

# 8.多个子图表
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
# plt.axes：手动构建子图表
# 例如，在距离左边和底部 65%的位置，以插图的形式放置一个宽度和高度都是 20%子图表，上述数值应该为[0.65, 0.65, 0.2, 0.2]：
ax1 = plt.axes()  # 标准图表
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2]) #子图表

# 使用这个方法来创建两个垂直堆叠的子图表：
fig = plt.figure() # 获得figure对象
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2)) # 左边10% 底部50% 宽80% 高40%
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2)) # 左边10% 底部10% 宽80% 高40%

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))

# plt.subplot：简单网格的子图表
# 函数接受三个整数参数，网格行数，网格列数以及该网格子图表的序号（从左上角向右下角递增）：
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')

# 下面的代码使用了与plt.subplot()等价的面向对象接口方法fig.add_subplot()：
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)),
           fontsize=18, ha='center')

# plt.subplots：一句代码设置所有网格子图表
# 创建一个  网格的子图表，其中每一行的子图表共享它们的 y 轴，而每一列的子图表共享它们的 x 轴：

fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# 使用 NumPy 索引的语法很简单的获得它们：
# axes是一个2×3的数组，可以通过[row, col]进行索引访问
for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)),
                      fontsize=18, ha='center')
fig

# plt.GridSpec：更复杂的排列
# 一个两行三列并带有指定的宽度高度间隔的 gridspec 可以如下创建：
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
# 指定子图表的位置和占据的网格，仅需要使用熟悉的 Python 切片语法即可：
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])

# 在需要创建多个直方图的联合图表中使用这种方法，如下例：
# 构建二维正态分布数据
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# 使用GridSpec创建网格并加入子图表
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# 在主图表中绘制散点图
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# 分别在x轴和y轴方向绘制直方图
x_hist.hist(x, 40, histtype='stepfilled',
            orientation='vertical', color='gray')
x_hist.invert_yaxis() # x轴方向（右下）直方图倒转y轴方向

y_hist.hist(y, 40, histtype='stepfilled',
            orientation='horizontal', color='gray')
y_hist.invert_xaxis() # y轴方向（左上）直方图倒转x轴方向

# 9.文本和标注
# 将要用到的模块和包导入 notebook：
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd
# 例子：节假日对美国出生率的影响
# 本例中的数据可以在 https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv 下载。
# 以图表展示这个结果：
births = pd.read_csv(r'D:\python\Github学习材料\Python数据科学手册\data\births.csv')

quartiles = np.percentile(births['births'], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')
births_by_date = births.pivot_table('births',
                                    [births.index.month, births.index.day])
births_by_date.index = [pd.datetime(2012, month, day)
                        for (month, day) in births_by_date.index]

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)
# 通过调用plt.text或ax.text函数来实现，它们可以在某个特定的 x，y 轴位置输出一段文字：
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# 在折线的特殊位置标注文字
style = dict(size=10, color='gray')

ax.text('2012-1-1', 3950, "New Year's Day", **style)
ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
ax.text('2012-9-4', 4850, "Labor Day", ha='center', **style)
ax.text('2012-10-31', 4600, "Halloween", ha='right', **style)
ax.text('2012-11-25', 4450, "Thanksgiving", ha='center', **style)
ax.text('2012-12-25', 3850, "Christmas ", ha='right', **style)

# 设置标题和y轴标签
ax.set(title='USA births by day of year (1969-1988)',
       ylabel='average daily births')

# 设置x轴标签月份居中
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))

# 转换和文本位置
# 使用这些转换将文字写在图表中不同位置的例子：
fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])

# transform=ax.transData是默认的，这里写出来是为了明确对比
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure)

# 改变了轴的最大长度，只有transData坐标会收到影响，其他两个还是保持在相同位置：
ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)
fig

# 箭头和标注
# 下面提供一些参数来使用annotate函数：
%matplotlib inline

fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')

ax.annotate('local maximum', xy=(6.28, 1), xytext=(10, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('local minimum', xy=(5 * np.pi, -1), xytext=(2, -6),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3,angleA=0,angleB=-90"))

# 在前面出生率图上再使用一些参数进行更多的说明：
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# 为图表添加标注
ax.annotate("New Year's Day", xy=('2012-1-1', 4100),  xycoords='data',
            xytext=(50, -30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=-0.2"))

ax.annotate("Independence Day", xy=('2012-7-4', 4250),  xycoords='data',
            bbox=dict(boxstyle="round", fc="none", ec="gray"),
            xytext=(10, -40), textcoords='offset points', ha='center',
            arrowprops=dict(arrowstyle="->"))

ax.annotate('Labor Day', xy=('2012-9-4', 4850), xycoords='data', ha='center',
            xytext=(0, -20), textcoords='offset points')
ax.annotate('', xy=('2012-9-1', 4850), xytext=('2012-9-7', 4850),
            xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|,widthA=0.2,widthB=0.2', })

ax.annotate('Halloween', xy=('2012-10-31', 4600),  xycoords='data',
            xytext=(-80, -40), textcoords='offset points',
            arrowprops=dict(arrowstyle="fancy",
                            fc="0.6", ec="none",
                            connectionstyle="angle3,angleA=0,angleB=-90"))

ax.annotate('Thanksgiving', xy=('2012-11-25', 4500),  xycoords='data',
            xytext=(-120, -60), textcoords='offset points',
            bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=80,rad=20"))


ax.annotate('Christmas', xy=('2012-12-25', 3850),  xycoords='data',
             xytext=(-30, 0), textcoords='offset points',
             size=13, ha='right', va="center",
             bbox=dict(boxstyle="round", alpha=0.1),
             arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1))

# 设置图表标题和坐标轴标记
ax.set(title='USA births by day of year (1969-1988)',
       ylabel='average daily births')

# 设置月份坐标居中显示
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'))

ax.set_ylim(3600, 5400)

# 10.自定义刻度
# 主要的和次要的刻度
# 在 Matplotlib 2.0 之后，当 axis 的跨度过大时，默认次要刻度将会不再展示，因此，下面的代码经过了修改，加上了 xlim 和 ylim 参数。
import matplotlib.pyplot as plt
plt.style.use('classic')
%matplotlib inline
import numpy as np
ax = plt.axes(xscale='log', yscale='log', xlim=[10e-5, 10e5], ylim=[10e-5, 10e5])
ax.grid()

# 下面我们来查看一下 x 轴的相应对象：

print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())

print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())

# 隐藏刻度和标签
# 可以通过使用plt.NullLocator()和plt.NullFormatter()来设置，如下例：
ax = plt.axes()
ax.plot(np.random.rand(50))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())

# 考虑下面的图表，包含着不同的头像，一个很常见的有监督机器学习问题：
fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)

# 从scikit-learn载入头像数据集
from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces().images

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")

# 减少或增加刻度的数量
# 默认设置的一个常见问题是当子图表较小时，刻度标签可能会粘在一起：

fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# Matplotlib 会自己计算按照这个最大数量计算的刻度位置：
# 对x和y轴设置刻度最大数量
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
fig

# 复杂的刻度格式
# 考虑下面的正弦和余弦图表：

# 绘制正弦和余弦图表
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw=3, label='Sine')
ax.plot(x, np.cos(x), lw=3, label='Cosine')

# 设置网格、图例和轴极限
ax.grid(True)
ax.legend(frameon=False)
ax.axis('equal')
ax.set_xlim(0, 3 * np.pi)

# 设置主要刻度为 Π/2 位置，设置次要刻度为 Π/4 位置：

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
fig

# 使用plt.FuncFormatter，这个对象能够接受一个用户自定义的函数来提供对于刻度标签的精细控制：
def format_func(value, tick_number):
    # N是pi/2的倍数
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0" # 0点
    elif N == 1:
        return r"$\frac{\pi}{2}$" # pi/2
    elif N == 2:
        return r"$\pi$" # pi
    elif N % 2 > 0:
        return r"$\frac{{%d}\pi}{2}$" %N # n*pi/2 n是奇数
    else:
        return r"${0}\pi$".format(N // 2) # n*pi n是整数

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
fig

# Formatter 和 Locator 总结
# 下表中列出的对象在plt命名空间中都是有效的：
'''
Locator 对象	    描述
NullLocator	        无刻度
FixedLocator	    固定刻度位置
IndexLocator	    序号图表刻度 (例如 x = range(len(y)))
LinearLocator	    从最小到最大值的均匀分割刻度
LogLocator	        从最小到最大值的对数分割刻度
MultipleLocator	    某个基数的倍数刻度
MaxNLocator	        刻度数量最大值
AutoLocator	        默认的刻度数量最大值
AutoMinorLocator	默认的次要刻度

Formatter 对象	    描述
NullFormatter	    无标签
IndexFormatter	    从一个列表获得标签
FixedFormatter	    从固定的字符串设置标签
FuncFormatter	    使用自定义函数设置标签
FormatStrFormatter	使用一个格式化字符串设置标签
ScalarFormatter	    默认的标量标签
LogFormatter	    默认的对数标签
'''

# 11.在 matplotlib 中创建三维图表
# 三维图表可以使用载入mplot3d工具包来激活，这个包会随着 Matplotlib 自动安装：
from mpl_toolkits import mplot3d
# 一旦模块被导入，三维 axes 就可以像其他普通 axes 一样通过关键字参数projection='3d'来创建：
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

# 三维的点和线
# 绘制一个三维中的三角螺旋，在线的附近在绘制一些随机的点：
ax = plt.axes(projection='3d')

# 三维螺旋线的数据
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# 三维散点的数据
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

# 三维轮廓图
# 展示一个三维的正弦函数轮廓图：
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# 在下面的例子中使用的是 60° 的水平角（即以 60° 俯视 x-y 平面）和 35° 的方位角（即将 z 轴逆时针旋转 35°）：
ax.view_init(60, 35)
fig

# 框线图和表面图
# 下面是一个框线图的例子：
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.set_title('wireframe')

# 添加色图用于填充多边形能够让图形表面展示出来：
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')

# 下面的例子使用surface3D绘制了一个部分极坐标网格，能够切入到函数内部观察效果：
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

# 表面三角剖分
# 使用一组随机的点来绘制三维图表
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)
# 使用它们来绘制一张散点图表现出样本所在表面的情况：
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)

# 绘制表面（注意的是这里的 x，y，z 是一维的数组）：
ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,
                cmap='viridis', edgecolor='none')

# 例子：绘制莫比乌斯环
'''莫比乌斯环是使用一条纸条，一端翻折后与另一端粘起来形成的环形。在拓扑学中这是非常有趣的一个形状，因为它只有一个面.
下面使用 Matplotlib 的三维工具绘制莫比乌斯环.
创建莫比乌斯环的关键在于能参数化它：莫比乌斯环是一个二维的环状结构，因此我们需要两个特定的维度.
一个我们称为 θ,取值范围是 0->2Π 表示整个环状，还有一个称为 ω,取值范围是  -1->1表示纸带的宽度：'''
theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)

phi = 0.5 * theta
# 用它来计算最终(x,y,z)  三维坐标系的坐标值：
# r是坐标点距离环形中心的距离值
r = 1 + w * np.cos(phi)
# 利用简单的三角函数知识算得x，y，z坐标值
x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))
# 下面的代码最终绘制图形：
# 在底层参数的基础上进行三角剖分
from matplotlib.tri import Triangulation
tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles,
                cmap='viridis', linewidths=0.2)

ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)

'''参考资料
[1]PythonDataScienceHandbook:https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks'''
