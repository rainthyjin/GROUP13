#导入文件和目录处理模块os以及数据处理包pandas
import pandas as pd
import os
#定义函数datagena，输入为机组文件夹路径path_machine，输出为整合后csv数据文件的存放路径out_machine
def datagena(path_machine,out_machine):
    #读取机组文件夹下各数据组文件夹的路径并按文件名排序，保证整合时
    #数据组文件夹读取的顺序固定，使接下来的读取以a-e或1-5的顺序进行
    dirs_machine = os.listdir(path_machine)
    #print(dirs_machine)
    dirs_machine.sort()
    rpath_machine = [os.path.join(path_machine,name) for name in dirs_machine]
    #print(rpath_machine)
    # #建立输入数据的dataframe对象
    df_machinerow = pd.DataFrame()
    # #建立循环，对机组内数据组从a-e或1-5依次进行读取，进行数据整合
    for j in range(0,len(rpath_machine)):
         path_class = rpath_machine[j]
         label = dirs_machine[j]
         print("The name of datagroup is " + label)
    minnum = len(dirs_machine)
    #print(minnum)

    result = pd.concat([pd.read_csv(i,header = None,skiprows=1) for i in rpath_machine])
    result.to_csv(out_machine,index = False)
    #print(all)

inputfolder = 'E:/learningsource/code/移动互联网应用/大作业/dataset/train/B/' #这里输入机组文件夹的路径
outputfile = 'E:/learningsource/code/移动互联网应用/大作业/datacsv/Bout.csv' #这里输入整合后数据输出文件想要存储的路径

datagena(inputfolder,outputfile)
datagena('E:/learningsource/code/移动互联网应用/大作业/dataset/train/IR/','E:/learningsource/code/移动互联网应用/大作业/datacsv/IRout.csv')
datagena('E:/learningsource/code/移动互联网应用/大作业/dataset/train/NOR/','E:/learningsource/code/移动互联网应用/大作业/datacsv/NORout.csv')
datagena('E:/learningsource/code/移动互联网应用/大作业/dataset/train/OR/','E:/learningsource/code/移动互联网应用/大作业/datacsv/ORout.csv')
#datagena('E:/learningsource/code/移动互联网应用/大作业/dataset/test/TEST/','E:/learningsource/code/移动互联网应用/大作业/datacsv/TESTout.csv')

for i in range(1,7):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/train/B/B0' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/B0' +str(i) + 'out.csv',index = False)

for i in range(1,7):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/train/IR/IR0' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/IR0' +str(i) + 'out.csv',index = False)

for i in range(1,3):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/train/NOR/NORMAL0' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/NOR0' +str(i) + 'out.csv',index = False)

for i in range(1,10):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/train/OR/OR0' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/OR0' +str(i) + 'out.csv',index = False)

for i in range(10,15):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/train/OR/OR' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/OR' +str(i) + 'out.csv',index = False)


for i in range(1,10):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/test/TEST/TEST0' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/TEST0' +str(i) + 'out.csv',index = False)

for i in range(10,15):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/test/TEST/TEST' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/datacsv/TEST' +str(i) + 'out.csv',index = False)

for i in range(1,143):
    result = pd.concat([pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/data/TEST' + str(i) + '.csv',header = None,skiprows=1)] )
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/dataout/TEST' +str(i) + 'out.csv',index = False)