import pandas as pd

df_out_columns = ['time_mean','time_std','time_max','time_min','time_rms',
                  'time_ptp','time_median','time_iqr','time_pr',
                  'time_skew','time_kurtosis','time_var','time_amp',
                  'time_smr','time_wavefactor','time_peakfactor',
                  'time_pulse','time_margin','1X','2X','3X','1XRatio',
                  '2XRatio','3XRatio']
label_columns = ['label']
DE_columns = ['DE_'+ i for i in df_out_columns]
FE_columns = ['FE_'+ i for i in df_out_columns] + label_columns

all_columns = DE_columns + FE_columns

#将提取出的特征集划分为两半，一半用于模型训练，另一半用作测试集，评估模型指标

for i in range(1,3):
    divide = []
    divide2 = []
    feature_normal = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_normal0' + str(i) + '.csv')
    k = 0
    #循环终止的条件为k值达到特征集行数的一半
    while k < round(feature_normal.shape[0]/2) :
        line = []
        line2 = []
        #获取第k行所有列的数据
        line.extend(feature_normal.iloc[k,:])
        b = round(feature_normal.shape[0]/2) + k
        line2.extend(feature_normal.iloc[b,:])
        k = k + 1
        #分别把line与line2添加到两个不同的列表中储存
        divide.append(line)
        divide2.append(line2)
    divide = pd.DataFrame(divide, columns=all_columns)
    divide.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_nor' + str(i) + '.csv',index=False)
    divide2 = pd.DataFrame(divide2, columns=all_columns)
    divide2.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_nor' + str(i) + '.csv', index=False)

for i in range(1,7):
    divide = []
    divide2 = []
    feature_normal = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_b0' + str(i) + '.csv')
    k = 0
    while k < round(feature_normal.shape[0]/2) :
        line = []
        line2 = []
        line.extend(feature_normal.iloc[k,:])
        b = round(feature_normal.shape[0]/2) + k
        line2.extend(feature_normal.iloc[b,:])
        k = k + 1
        divide.append(line)
        divide2.append(line2)
    divide = pd.DataFrame(divide, columns=all_columns)
    divide.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_b' + str(i) + '.csv',index=False)
    divide2 = pd.DataFrame(divide2, columns=all_columns)
    divide2.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_b' + str(i) + '.csv', index=False)

for i in range(1,7):
    divide = []
    divide2 = []
    feature_normal = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_ir0' + str(i) + '.csv')
    k = 0
    while k < round(feature_normal.shape[0]/2) :
        line = []
        line2 = []
        line.extend(feature_normal.iloc[k,:])
        b = round(feature_normal.shape[0]/2) + k
        line2.extend(feature_normal.iloc[b,:])
        k = k + 1
        divide.append(line)
        divide2.append(line2)
    divide = pd.DataFrame(divide, columns=all_columns)
    divide.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_ir' + str(i) + '.csv',index=False)
    divide2 = pd.DataFrame(divide2, columns=all_columns)
    divide2.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_ir' + str(i) + '.csv', index=False)

for i in range(1,10):
    divide = []
    divide2 = []
    feature_normal = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_or0' + str(i) + '.csv')
    k = 0
    while k < round(feature_normal.shape[0]/2) :
        line = []
        line2 = []
        line.extend(feature_normal.iloc[k,:])
        b = round(feature_normal.shape[0]/2) + k
        line2.extend(feature_normal.iloc[b,:])
        k = k + 1
        divide.append(line)
        divide2.append(line2)
    divide = pd.DataFrame(divide, columns=all_columns)
    divide.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_or' + str(i) + '.csv',index=False)
    divide2 = pd.DataFrame(divide2, columns=all_columns)
    divide2.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_or' + str(i) + '.csv', index=False)

for i in range(10,15):
    divide = []
    divide2 = []
    feature_normal = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_or' + str(i) + '.csv')
    k = 0
    while k < round(feature_normal.shape[0]/2) :
        line = []
        line2 = []
        line.extend(feature_normal.iloc[k,:])
        b = round(feature_normal.shape[0]/2) + k
        line2.extend(feature_normal.iloc[b,:])
        k = k + 1
        divide.append(line)
        divide2.append(line2)
    divide = pd.DataFrame(divide, columns=all_columns)
    divide.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_or' + str(i) + '.csv',index=False)
    divide2 = pd.DataFrame(divide2, columns=all_columns)
    divide2.to_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_or' + str(i) + '.csv', index=False)

