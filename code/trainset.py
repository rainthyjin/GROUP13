#读取数据集并为其添加标签
import pandas as pd

for i in range(1,7):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacleaned/B0' + str(i) + 'out.csv')
    B['label'] = 1
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/b0' + str(i) + '.csv', index=False)

for i in range(1,7):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacleaned/IR0' + str(i) + 'out.csv')
    B['label'] = 3
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/ir0' + str(i) + '.csv', index=False)

for i in range(1,3):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/NOR0' + str(i) + 'out.csv')
    B['label'] = 0
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/normal0' + str(i) + '.csv', index=False)

for i in range(1,10):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacleaned/OR0' + str(i) + 'out.csv')
    B['label'] = 2
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/or0' + str(i) + '.csv', index=False)

for i in range(10,15):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacleaned/OR' + str(i) + 'out.csv')
    B['label'] = 2
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/or' + str(i) + '.csv', index=False)


for i in range(1,10):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/TEST0' + str(i) + 'out.csv')
    B['label'] = 'TEST' + str(i)
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/0325/test/TEST0' + str(i) + 'label.csv', index=False)
for i in range(10,15):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/TEST' + str(i) + 'out.csv')
    B['label'] = 'TEST' + str(i)
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/0325/test/TEST' + str(i) + 'label.csv', index=False)

#循环读取TEST1 - TEST142文件，添加标签后再输出
for i in range(1,143):
    B = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/dataout/TEST' + str(i) + 'out.csv')
    B['label'] = 'TEST' + str(i)
    B.to_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/dataout/TEST' + str(i) + 'label.csv', index=False)