import pandas as pd
import matplotlib.pyplot as plt

#数据清洗函数，通过观察数据的分布，设定参数清洗掉与大部分数据偏差较远的数值
#threshold与threshold1分别为设定的下限与上限，低于下限或高于上限的数值会被剔除
def datacleaning(input_file,threhold,threhold1,output_file):
    df = pd.read_csv(input_file)
    print(df.shape)   
    df = df[(df.iloc[:,0]>threhold) & (df.iloc[:,1]>threhold1) & (df.iloc[:,0]<abs(threhold)) & (df.iloc[:,1]<abs(threhold1))]
    df = df.reset_index(drop=True)
    print(df.shape)
    df.to_csv(output_file,index=False)
    plt.figure(figsize=(15,6))
    plt.plot(df.iloc[:, 0])
    plt.show()





df = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/Bout.csv')
#设置画布大小
plt.figure(figsize=(15,6))
#将6个传感器以叠加的形式呈现在画布上一起观察

plt.plot(df.iloc[:,0])
plt.show()