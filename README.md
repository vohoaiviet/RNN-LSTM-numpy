# 基于RNN-LSTM的唐诗生成器
## 采用了Keras来搭建一个两层的LSTM网络
----------------------------
### 1.数据来自《全唐诗》，分别取自李白，杜甫，孟浩然，杜牧四人共400多首
### 2.数据格式进行了简单处理，更格式化一些，相较未处理之前，结果更像唐诗一些。。。
### 3.限于机器性能，使用的数据量还是太小，相信在更大数据集上会有更好表现。
------------------------------

## 迭代80次后生成的“唐诗”
>骅骝作驹已汗血，鸷鸟举翮连青云。<br />
词源倒流三峡水，笔阵独扫千人军。<br />
泪崒阳,陵抱落扁虾钜回,山如兵又夜行月。<br />
其同我上岁食世。<br />
客还人闻头，有郭成云寒，所增一载必。<br />
学与光螭地，息洪云活炎。<br />
具魂鞭丈年，处顿客不山驻，楼舞我言。<br />
丽尽尊奚以。骝吹千，万淫晨短令。世溪奚渔芰<br />

-------
## 网络结构
### 1.输入层是01向量表示的数组
### 2.一个输出层512维的LSTM层+Dropout
### 3.另一个512维的LSTM层+Dropout
### 4.一个全连接层
### 5.输出加一个softmax
-----------------------------
