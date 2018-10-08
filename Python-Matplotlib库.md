> 本文转载来源：[Python绘图库Matplotlib入门教程](http://qiangbo.space/2018-04-06/matplotlib_l1/)
> 本文同时使用了这里的教学代码：[Matplotlib 画图教程系列 _ 莫烦Python](https://morvanzhou.github.io/tutorials/data-manipulation/plt/)
************************************************************************
## 0、入门代码示例
下面我们先看一个最简单的代码示例，让我们感受一下Matplotlib是什么样的：
```
import matplotlib.pyplot as plt
import numpy as np

#需要展现的数据
data = np.arange(100, 201)

#设定x，y轴的最大、最小值
plt.axis([0,100,50,300])

#另一种设定x，y轴的最大、最小值的方式
#plt.xlim(0,100)
#plt.ylim(50,300)

#设定x轴标记，可以用字符代替
plt.xticks(np.linspace(0,100,5,endpoint=True),['$one$','$two$','one','two','five'])

#设定y轴标记
plt.yticks(np.linspace(50,300,5,endpoint=True))

 #设定图表标题
plt.title('Easy as 1, 2, 3')

#设定x，y轴标签的字体，颜色
plt.xlabel('x numbers',fontsize=14, color='red')      
plt.ylabel('y numbers',fontsize=14, color='red')

#在图表内增加公式
plt.text(20, 250, r'$\mu=100,\ \sigma=15,\bigcap $')

#设置背景网格线
plt.grid(True)

#设置打印线段的颜色、线宽、线型
plt.plot(data,color="blue", linewidth=1.0, linestyle="-")

plt.show()

#保存图片
plt.savefig('my_first_chart.png')
```
这段代码=绘制出了一个非常直观的线性图，如下所示：
![](https://upload-images.jianshu.io/upload_images/4353065-e44f916936b805ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


对照着这个线形图，我们来讲解一下三行代码的逻辑：

1.  通过`np.arange(100, 201)`生成一个[100, 200]之间的整数数组，它的值是：[100, 101, 102, … , 200]
2.  通过`matplotlib.pyplot`将其绘制出来。很显然，绘制出来的值对应了图中的纵坐标（y轴）。而matplotlib本身为我们设置了图形的横坐标（x轴）：[0, 100]，因为我们刚好有100个数值
3.  通过`plt.show()`将这个图形显示出来


> [查看更多公式的写法](https://matplotlib.org/users/mathtext.html#mathtext-tutorial)


************************************************************************
## 1、一次绘制多个图形
有些时候，我们可能希望一次绘制多个图形，例如：两组数据的对比，或者一组数据的不同展示方式等。

可以通过下面的方法创建多个图形：

### 多个figure
可以简单的理解为一个figure就是一个图形窗口。matplotlib.pyplot会有一个默认的figure，我们也可以通过plt.figure()创建更多个。如下面的代码所示：
```
import matplotlib.pyplot as plt
import numpy as np

#创建第1个图形窗口
plt.figure()

#创建第2个窗口并设定窗口名称为3、尺寸（8*6）、分辨率80
plt.figure(num = 3，figsize=(8,6), dpi=80)

data = np.arange(100, 201)
plt.plot(data)

plt.figure(figsize=(8,6), dpi=80)

data2 = np.arange(200, 301)
plt.plot(data2)

plt.show()

```
这段代码绘制了两个窗口的图形，它们各自是一个不同区间的线形图，如下所示：
![](http://upload-images.jianshu.io/upload_images/4353065-09ab982213894621.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
************************************************************************
### 多个subplot
有些情况下，我们是希望在同一个窗口显示多个图形。此时就这可以用多个subplot。下面是一段代码示例：
```
import matplotlib.pyplot as plt
import numpy as np

data = np.arange(100, 201)
#选择2行1列subplot中的第1个subplot
plt.subplot(2, 1, 1)  #等于plt.subplot(211)
plt.plot(data)

data2 = np.arange(200, 301)
#选择2行1列subplot中的第2个subplot
plt.subplot(2, 1, 2)  #等于plt.subplot(212)
plt.plot(data2)

plt.show()
```
这段代码中，除了subplot函数之外都是我们熟悉的内容。subplot函数的前两个参数指定了subplot数量，即：它们是以矩阵的形式来分割当前图形，两个整数分别指定了矩阵的行数和列数。而第三个参数是指矩阵中的索引。

所以这段代码的结果是这个样子：
![](http://upload-images.jianshu.io/upload_images/4353065-a1a3f64041846dd2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

不均匀图中图：
![不均匀图中图](https://upload-images.jianshu.io/upload_images/4353065-9d7c62006c2238c2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

代码：
```
#相当于将画布分为2行3列
#第一行图占了3个位置
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

#第二行第1个图从4开始
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(235)
plt.plot([0,1],[0,3])

plt.subplot(236)
plt.plot([0,1],[0,4])

plt.show()  # 展示
```
更复杂的不均匀图中图：
![](https://upload-images.jianshu.io/upload_images/4353065-a68636f857c25404.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
代码：
```
#画第一部分
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
#使用plt.subplot2grid来创建第1个小图, (3,3)表示将整个图像窗口分成3行3列, (0,0)表示从第0行第0列开始作图，colspan=3表示列的跨度为3, rowspan=1表示行的跨度为1. colspan和rowspan缺省, 默认跨度为1

ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

#继续画其他部分
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

#可以对每个部分单独设置图表和其他属性
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')  #！设置坐标轴标签要用set_xlabel
ax4.set_ylabel('ax4_y')
```

> `subplot`函数的详细说明参见这里：[matplotlib.pyplot.subplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot)
> [Subplot分格显示](https://morvanzhou.github.io/tutorials/data-manipulation/plt/4-2-subplot2/)
************************************************************************
## 2、常用图形示例

Matplotlib可以生成非常多的图形式样，多到令人惊叹的地步。大家可以在这里：[Matplotlib Gallery](https://matplotlib.org/gallery/index.html) 感受一下。

本文作为第一次的入门教程，我们先来看看最常用的一些图形的绘制。

### 线性图

前面的例子中，线性图的横轴的点都是自动生成的，而我们很可能希望主动设置它。另外，线条我们可能也希望对其进行定制。看一下下面这个例子：
```
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [3, 6, 9], '-r',label="xxx")
plt.plot([1, 2, 3], [2, 4, 9], ':g',label="yyy")

#图例位置
plt.legend(loc='upper left')  #loc指定图裂位置，loc='best'让系统自动判断最佳位置

plt.show()
```
这段代码可以让我们得到这样的图形：
![](https://upload-images.jianshu.io/upload_images/4353065-d7f759d84eae397e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这段代码说明如下：

1.  `plot`函数的第一个数组是横轴的值，第二个数组是纵轴的值，所以它们一个是直线，一个是折线；
2.  最后一个参数是由两个字符构成的，分别是线条的样式和颜色。前者是红色的直线，后者是绿色的点线。关于样式和颜色的说明请参见`plot`函数的API Doc：[matplotlib.pyplot.plot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)
3.  [plt.legend 的 loc可选参数](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend)
************************************************************************
### 散点图

`scatter`函数用来绘制散点图。同样，这个函数也需要两组配对的数据指定x和y轴的坐标。下面是一段代码示例：
```
import matplotlib.pyplot as plt
import numpy as np

N = 20

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='r', s=100, alpha=0.5)

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='g', s=200, alpha=0.5)

plt.scatter(np.random.rand(N) * 100,
            np.random.rand(N) * 100,
            c='b', s=300, alpha=0.5)

plt.show()
```
这段代码说明如下：

这幅图包含了三组数据，每组数据都包含了20个随机坐标的位置
参数c表示点的颜色，s是点的大小，alpha是透明度
这段代码绘制的图形如下所示：
![](http://upload-images.jianshu.io/upload_images/4353065-88b1d326444edabb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> `scatter`函数的详细说明参见这里：[matplotlib.pyplot.scatter](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter)
************************************************************************
### 饼状图
pie函数用来绘制饼状图。饼状图通常用来表达集合中各个部分的百分比。
```
import matplotlib.pyplot as plt
import numpy as np

labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

data = np.random.rand(7) * 100

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend()

plt.show()
```
这段代码说明如下：

1. data是一组包含7个数据的随机数值
2. 图中的标签通过labels来指定
3. autopct指定了数值的精度格式
4. plt.axis('equal')设置了坐标轴大小一致
5. plt.legend()指明要绘制图例（见下图的右上角）
这段代码输出的图形如下所示：
![](http://upload-images.jianshu.io/upload_images/4353065-6889453037d79dcf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> `pie`函数的详细说明参见这里：[matplotlib.pyplot.pie](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html?highlight=pie#matplotlib.pyplot.pie)
************************************************************************
### 条形图
bar函数用来绘制条形图。条形图常常用来描述一组数据的对比情况，例如：一周七天，每天的城市车流量。

下面是一个代码示例：
```
import matplotlib.pyplot as plt
import numpy as np

N = 7

#设定x，y的数值
x = np.arange(N)
data = np.random.randint(low=0, high=100, size=N)

#设定每条数值的颜色
colors = np.random.rand(N * 3).reshape(N, -1)

#设定x轴数值标签
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

#设定y轴范围
plt.ylim(0,130)

#设定图表标题
plt.title("Weekday Data")

#创建条形图
plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)

#设定数值标签
for i,j in zip(x,data):
    plt.text(i,j+1,
             '%.2f' %j,
             ha='center',  #ha: horizontal alignment
             va='bottom'  #va: vertical alignment
             )

plt.show()
```
这段代码说明如下：

1.  这幅图展示了一组包含7个随机数值的结果，每个数值是[0, 100]的随机数
2.  它们的颜色也是通过随机数生成的。`np.random.rand(N * 3).reshape(N, -1)`表示先生成21（N x 3）个随机数，然后将它们组装成7行，那么每行就是三个数，这对应了颜色的三个组成部分。如果不理解这行代码，请先学习一下[Python 机器学习库 NumPy 教程](http://qiangbo.space/2018-01-06/AI_NumPy_Tutorial/)
3.  `title`指定了图形的标题，`labels`指定了标签，`alpha`是透明度

这段代码输出的图形如下所示：
![](https://upload-images.jianshu.io/upload_images/4353065-f0d9d0183575e771.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> `bar`函数的详细说明参见这里：[matplotlib.pyplot.bar](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html?highlight=bar#matplotlib.pyplot.bar)
************************************************************************
### 直方图
hist函数用来绘制直方图。直方图看起来是条形图有些类似。但它们的含义是不一样的，直方图描述了数据中某个范围内数据出现的频度。这么说有些抽象，我们通过一个代码示例来描述就好理解了：
```
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randint(0, n, n) for n in [3000, 4000, 5000]]
labels = ['3K', '4K', '5K']
bins = [0, 100, 500, 1000, 2000, 3000, 4000, 5000]

plt.hist(data, bins=bins, label=labels)
plt.legend()

plt.show()
```
上面这段代码中，[np.random.randint(0, n, n) for n in [3000, 4000, 5000]]生成了包含了三个数组的数组，这其中：

- 第一个数组包含了3000个随机数，这些随机数的范围是 [0, 3000)
- 第二个数组包含了4000个随机数，这些随机数的范围是 [0, 4000)
- 第三个数组包含了5000个随机数，这些随机数的范围是 [0, 5000)
bins数组用来指定我们显示的直方图的边界，即：[0, 100) 会有一个数据点，[100, 500)会有一个数据点，以此类推。所以最终结果一共会显示7个数据点。同样的，我们指定了标签和图例。

这段代码的输出如下图所示：
![](http://upload-images.jianshu.io/upload_images/4353065-57370865aba3c72a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在这幅图中，我们看到，三组数据在3000以下都有数据，并且频度是差不多的。但蓝色条只有3000以下的数据，橙色条只有4000以下的数据。这与我们的随机数组数据刚好吻合。

> `hist`函数的详细说明参见这里：[matplotlib.pyplot.hist](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html?highlight=hist#matplotlib.pyplot.hist)
************************************************************************
### 次坐标轴图
*定义：即在同个图上有第 2个 y轴存在*
```
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 *y1

#获取figure默认的坐标系 ax1
fig, ax1 = plt.subplots()

#对ax1调用twinx()方法，生成如同镜面效果后的ax2
ax2 = ax1.twinx()    # mirror the ax1
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')

plt.show()
```
![](https://upload-images.jianshu.io/upload_images/4353065-482b8c84b846b679.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

************************************************************************
## 3、附加
解决matplotlib显示中文的方法
```
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
```
************************************************************************
## 4、参考资料与推荐读物

>01、 [Matplotlib官方网站](https://matplotlib.org/)

>02、 [Matplotlib 教程（译文）](https://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)

>03、 [Matplotlib 教程（原文）](http://www.labri.fr/perso/nrougier/teaching/matplotlib/)




