import pandas as pd
import numpy as np
# feature_normal = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_normal.csv')
# feature_b = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_b.csv')
# feature_or = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_or.csv')
# feature_ir = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_ir.csv')
b = []
ir = []
nor = []
or_ = []

for i in range(1, 7):
    b.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_b' + str(i) + '.csv'))
for i in range(1, 7):
    ir.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_ir' + str(i) + '.csv'))
for i in range(1, 3):
    nor.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_nor' + str(i) + '.csv'))
for i in range(1, 15):
    or_.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/train_or' + str(i) + '.csv'))
#这里将正常样本和故障征兆样本合并

feature_finalb = pd.concat([b[i] for i in range(0,6)])
feature_finalir = pd.concat([ir[i] for i in range(0,6)])
feature_finalnor = pd.concat([nor[i] for i in range(0,2)])
feature_finalor = pd.concat([or_[i] for i in range(0,14)])
feature_final = pd.concat([feature_finalir,feature_finalb,feature_finalnor,feature_finalor])
feature_final.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_train.csv',index=False)
#重置索引，否则可能造成索引混乱

feature_final = feature_final.reset_index(drop=True)
#可以修改以下list调整需要留下的特征
feature_selected_list = ['DE_time_rms','DE_1XRatio','DE_2XRatio','DE_3XRatio','DE_time_smr','DE_time_skew','DE_time_ptp','DE_time_var','FE_time_rms','FE_1XRatio',
'FE_2XRatio','FE_3XRatio','FE_time_smr','FE_time_skew','FE_time_ptp','FE_time_var','label']
feature_selected = feature_final[feature_selected_list]
feature_selected.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_trainselect.csv',index=False)



b.clear()
ir.clear()
nor.clear()
or_.clear()
for i in range(1, 7):
    b.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_b' + str(i) + '.csv'))
for i in range(1, 7):
    ir.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_ir' + str(i) + '.csv'))
for i in range(1, 3):
    nor.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_nor' + str(i) + '.csv'))
for i in range(1, 15):
    or_.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/dataset/分类集/test_or' + str(i) + '.csv'))
#这里将正常样本和故障征兆样本合并

feature_finalb = pd.concat([b[i] for i in range(0,6)])
feature_finalir = pd.concat([ir[i] for i in range(0,6)])
feature_finalnor = pd.concat([nor[i] for i in range(0,2)])
feature_finalor = pd.concat([or_[i] for i in range(0,14)])
feature_final = pd.concat([feature_finalir,feature_finalb,feature_finalnor,feature_finalor])
feature_final.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_test.csv',index=False)

feature_selected = feature_final[feature_selected_list]
feature_selected.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/feature_testselect.csv',index=False)



test_select1 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST01feature.csv')
test_select2 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST02feature.csv')
test_select3 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST03feature.csv')
test_select4 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST04feature.csv')
test_select5 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST05feature.csv')
test_select6 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST06feature.csv')
test_select7 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST07feature.csv')
test_select8 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST08feature.csv')
test_select9 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST09feature.csv')
test_select10 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST10feature.csv')
test_select11 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST11feature.csv')
test_select12 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST12feature.csv')
test_select13 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST13feature.csv')
test_select14 = pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST14feature.csv')


test_selected_list = ['DE_1XRatio','DE_2XRatio','DE_3XRatio',
                         'DE_time_ptp','FE_1XRatio','FE_2XRatio','FE_3XRatio','FE_time_ptp','label']

test_select1 = test_select1[feature_selected_list]
test_select1.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST01_select.csv',index=False)
test_select2 = test_select2[feature_selected_list]
test_select2.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST02_select.csv',index=False)
test_select3 = test_select3[feature_selected_list]
test_select3.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST03_select.csv',index=False)
test_select4 = test_select4[feature_selected_list]
test_select4.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST04_select.csv',index=False)
test_select5 = test_select5[feature_selected_list]
test_select5.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST05_select.csv',index=False)
test_select6 = test_select6[feature_selected_list]
test_select6.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST06_select.csv',index=False)
test_select7 = test_select7[feature_selected_list]
test_select7.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST07_select.csv',index=False)
test_select8 = test_select8[feature_selected_list]
test_select8.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST08_select.csv',index=False)
test_select9 = test_select9[feature_selected_list]
test_select9.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST09_select.csv',index=False)
test_select10 = test_select10[feature_selected_list]
test_select10.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST10_select.csv',index=False)
test_select11 = test_select11[feature_selected_list]
test_select11.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST11_select.csv',index=False)
test_select12 = test_select12[feature_selected_list]
test_select12.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST12_select.csv',index=False)
test_select13 = test_select13[feature_selected_list]
test_select13.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST13_select.csv',index=False)
test_select14 = test_select14[feature_selected_list]
test_select14.to_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST14_select.csv',index=False)
a = []
for i in range(1,143):
    a.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/dataf/TEST' + str(i) + 'f.csv'))

for i in range(0,142):
    a[i] = a[i][feature_selected_list]
    a[i].to_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/dataf/TEST' + str(i+1) + 'select.csv', index=False)


