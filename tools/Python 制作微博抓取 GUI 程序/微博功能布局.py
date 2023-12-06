# -*- coding:utf-8 -*-
# ！/usr/bin/env python




# 创建微博 Widget
def weiboWidget(self):
    self.left_button_widget_3 = QtWidgets.QWidget()
    self.weiboWebEngine = QWebEngineView()
    self.weiboWebEngine2 = QWebEngineView()
    self.progressWidget = QtWidgets.QWidget()
    self.ciyunWidget = QtWidgets.QWidget()

    # matplotlib 绘图区域
    self.figure = plt.figure(figsize=(7, 2))
    self.canvas = FigureCanvasQTAgg(self.figure)  # 绘图区域放到图层canvas之中
    self.gridLayout_weibo.addWidget(self.canvas, 5, 0, 1, 9)  # 图层放到pyqt布局之中


# 创建微博查询
def doWeiboQuery(self):
    weibo_link = self.lineEdit_weibo_link.text()
    weibo_name = self.lineEdit_weibo_name.text()
    weibo_page = self.weibo_comboBox.currentText()
    if not weibo_link or not weibo_name:
        QMessageBox.information(self, "Error", "微博链接或者用户名称不能为空",
                                QMessageBox.Yes)
        return
    self.weiboWebEngine.load(QUrl(weibo_link))
    self.qth = WeiBoQueryThread()
    self.qth.update_data.connect(self.weiboPgbUpdate)
    self.qth.draw_ciyun.connect(self.drawCiyun)
    self.qth.weibo_page = weibo_page
    self.qth.weibo_link = weibo_link
    self.qth.weibo_name = weibo_name
    self.qth.start()

def weiboPgbUpdate(self, data):
    self.pgb.setValue(data)

def drawCiyun(self):
    self.canvas.draw()
    self.toolbar = NavigationToolbar2QT(self.canvas, self)
    self.gridLayout_weibo.addWidget(self.toolbar, 8, 0, 1, 9)

"""子进程微博查询"""
class WeiBoQueryThread(QThread):
    # 创建一个信号，触发时传递当前时间给槽函数
    update_data = pyqtSignal(int)
    draw_ciyun = pyqtSignal()
    weibo_name = None
    weibo_link = None
    weibo_page = None
    total_pv = 0
    timestamp = str(int(time.time()))
    def run(self):
        # 微博爬虫
        try:
            file_name = self.weibo_name + "_" + self.timestamp + 'comment.csv'
            my_weibo = weibo_interface.Weibo(self.weibo_name)
            uid, blog_info = my_weibo.weibo_info(self.weibo_link)
            pv_max = int(self.weibo_page)
            pre_pv = 100 // pv_max
            for i in range(int(self.weibo_page)):
                my_weibo.weibo_comment(uid, blog_info, str(i), file_name)
                self.total_pv += pre_pv
                self.update_data.emit(self.total_pv)
            print("所有微博评论爬取完成！")
            print("开始生成词云")
            font, img_array, STOPWORDS, words = ciyun(file_name)
            wc = WordCloud(width=2000, height=1800, background_color='white', font_path=font, mask=img_array,
                           stopwords=STOPWORDS, contour_width=3, contour_color='steelblue').generate(words)
            plt.imshow(wc)
            plt.axis("off")
            self.draw_ciyun.emit()
            print("生成词云完成")
        except Exception as e:
            print(e)


# 词云制作
def ciyun(file, without_english=True):
    font = 'C:\windows\Fonts\FZSTK.TTF'
    STOPWORDS = {"回复", "@", "我", "你", "他", "了", "的", "吧", "吗", "在", "啊", "不", "也",
                 "还", "是", "说", "都", "就", "没", "做", "人", "赵薇", "被", "不是", "现在", "什么", "这", "呢", "知道", "邓"}
    df = pd.read_csv(file, usecols=[0])
    df_copy = df.copy()
    df_copy['comment'] = df_copy['comment'].apply(lambda x: str(x).split())
    df_list = df_copy.values.tolist()
    comment = jieba.cut(str(df_list), cut_all=False)
    words = ' '.join(comment)
    if without_english:
        words = re.sub('[a-zA-Z]', '', words)
    img = Image.open('ciyun.png')
    img_array = np.array(img)
    return font, img_array, STOPWORDS, words