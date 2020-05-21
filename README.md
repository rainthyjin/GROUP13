# GROUP13项目说明

## 项目概述
  > 本项目通过不同故障轴承的运行数据，提取故障特征，建立模型，实现了根据机组运行的数据对机组轴承故障预测的目标，并通过小程序端，将机组运行数据和出现的故障，利用图表等形式展现出来，方便机组运维人员更好的监测机组的运行情况。
## 目录结构
> ### 【code】
> >* STEP1_datagena.py
> >* STEP2_trainset.py
> >* STEP3_featureget.py
> >* STEP4_featureselect.py
> >* STEP5_LabelTest1.py
> >* STEP6_devide.py
> >* STEP7_train.py
    
> ### 【model】（已训练完成）
> >* RamdomForest.model

> ### 【dataset】
> >* train:训练集
> >* test:测试集

> ### 【轴承】（小程序文件包）
> >* cloudfunctions：小程序云函数配置
> >* miniprogram：小程序主要文档
> > >- dist : vant组件包
> > >- ec-canvas ： echarts组件库
> > >- images ： 小程序中用到的图片
> > >-  pages
> > > >   predict：小程序首页，进入小程序后，由此进行故障预测  
> > > >   dataprocessing：数据处理及特征提取页  
> > > >   model：模型预测页  
> > > >   result：模型故障预测结果页  
> > > >   index：机组预览页，可看到监测机组的数量及各机组故障数量对比  
> > > >   faultlibrary：运行详情页  
> > > >   datapreview：机组运行数据查看页  
> > > >   charts:各个机组故障种类数量饼状图显示页  
> > > >   mine：“我的”页  
> > >-  style : 系统默认文件
> > >- util：用户配置文件
> > >- app.js / app.json / app.wxss：全局配置文件
> > >- sitemap.json：配置其小程序页面是否允许微信索引

> ### 【其他文件】
> > datacleaned,datacsv,featureset,featuretest文件夹用于存放各步骤完成后的生成.csv文件

## 版本管理（可选，便于之后的维护）
* 第一版：上传小程序文档

* 第二版：上传数据处理算法，模型和数据集

* 第三版：补充程序运行过程中产生的数据集，如特征提取后的数据集

## 依赖配置
### 小程序端

1. 微信开发者工具，可从官网下载：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html  

2. vant weapp组件库，下载安装及使用说明可见官网：https://youzan.github.io/vant-weapp/#/quickstart  

3. e-charts组件，下载地址：https://github.com/ecomfe/echarts-for-weixin 将下载好的文件中 ec-canvas目录 放在小程序项目目录中即可，在 page目录的某个页面中使用echarts的话，需要在该页面json文件中中添加以下配置"usingComponents": {"ec-canvas": "../../ec-canvas/ec-canvas" }  

### 后端
1. python环境  ：python 3.6.6版本  

2. python依赖包
>pandas-0.23.2-cp37-cp37m-win_amd64  
numpy-1.16.6-cp37-cp37m-win_amd64  
scikit_learn-0.19.2-cp37-cp37m-win_amd64  

3. 项目IDE  : pycharm  



## 部署说明
> ### 小程序端
> > Github上直接下载轴承文件夹，并用微信开发者工具打开即可运行。

> ### 后端
> >Github上下载完全的数据集，并在代码中将对应文件路径修改为本机绝对路径

## 运行说明
>### 小程序端
> > 下载好轴承文件夹，打开微信开发者工具->打开项目，找到相应的轴承文件夹->填写自己的小程序id并打开即可运行。

>### 后端
> > 1. 数据预处理
运行datagena.py文件，完成对训练集和测试集文件的去除标签工作，输出的文件保存于datacsv文件夹中，需要自行修改文件路径为本机绝对路径。
> > 2. 为数据添加label
运行trainset.py文件，完成对训练集和测试集文件的添加label工作，输出的文件保存于datacsv文件夹中，需要自行修改文件路径为本机绝对路径。
> > 3. 特征获取及特征选择
运行featureget.py文件后运行featureselect.py文件，完成对训练集和测试集文件的特征获取及特征选择工作，输出的文件保存于featureset文件夹中，需要自行修改文件路径为本机绝对路径。
> > 4. 划分基础训练集
运行divide.py文件，将训练集的一半划分为测试集用于对模型评分，输出的文件保存于dataset文件夹中，需要自行修改文件路径为本机绝对路径。
> > 5. 模型训练及结果获取
运行train.py文件，完成模型训练和对TEST文件获取结果的工作，输出的文件保存路径需自行设定。

## 注意事项
> ### 小程序端
> >进入小程序编译成功后，首先应点击首页故障预测的按钮开始预测，之后小程序才会记录存储机组故障的相应信息，其他页面才会显示相应的图表。
> ### 后端
> >按照步骤完成相应操作即可
