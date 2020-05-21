
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from collections import Counter
import json
params = {}
columns = ['label','filename']
params['train'] = 'E:/learningsource/code/移动互联网应用/大作业/featureset/feature_trainselect.csv'
params['test'] = 'E:/learningsource/code/移动互联网应用/大作业/featureset/feature_testselect.csv'

def train():
    train_data = pd.read_csv(params['train'])
    train_data_y = train_data['label']
    # 除去标签的所有列就是特征
    train_data_x = train_data.drop(['label'], axis=1)
    model_ram_default = RandomForestClassifier(n_estimators=500,max_features=10,max_depth=10)
    # 模型训练
    model_ram_default.fit(train_data_x, train_data_y)
    joblib.dump(model_ram_default, 'E:/learningsource/code/移动互联网应用/大作业/model/RandomForest.model')

# 这里首先定义judge函数，以threhold为阈值，根据模型给出的分类概率进行判断，大于
# threhold为正常样本，反之为故障征兆样本


def test_model():
    test = np.array(pd.read_csv(params['test']))
    test_y = test[:, -1]
    test_x = test[:, :-1]

    model = joblib.load('E:/learningsource/code/移动互联网应用/大作业/model/RandomForest.model')

    predict = model.predict(test_x)
    print(predict)
    precision = precision_score(test_y, predict,average='macro')
    recall = recall_score(test_y, predict,average='macro')
    accuracy = accuracy_score(test_y, predict)
    res = {}
    res['precision'] = precision
    res['recall'] = recall
    res['accuracy'] = accuracy
    res['fMeasure'] = f1_score(test_y, predict,average='macro')
    print(json.dumps(res))



def test_lightgbm():
    # 加载模型
    model = joblib.load('E:/learningsource/code/移动互联网应用/大作业/model/RandomForest.model')
    test = []
    # 读取测试集,来源的特征文件同样经过特征提取和选择，只是不加标签，'label'列中表示
    # 其机组和数据组的信息，例如'M11_1'，方便我们统计各数据组的分类概率统计值进行排序
    for i in range(1,10):
        test.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST0' + str(i) + '_select.csv'))
    for i in range(10,15):
        test.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/featureset/TEST' + str(i) + '_select.csv'))

    result = []
    i = 0
    for test in test:
        #print(test)
        i = i+1
        final = []
        test = test.drop(['label'], axis=1)
        a = model.predict(test)
        counts = Counter(a).most_common(1)
        #print(model.predict(test))
        final.append(counts[0][0])
        if i <= 9 :
           final.extend(['TEST0' + str(i)])
        else:
           final.extend(['TEST' + str(i)])
        #print(final)
        result.append(final)
        y_pred = model.predict_proba(test)
        #print(y_pred)

    print(result)
    result = pd.DataFrame(result,columns = columns)
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/0325/final_result1.csv',index = False)

def test2():
    # 加载模型
    model = joblib.load('E:/learningsource/code/移动互联网应用/大作业/model/RandomForest.model')
    a = []
    for i in range(1,143):
        a.append(pd.read_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/dataf/TEST' + str(i) + 'select.csv'))
    result = []
    i = 0
    for test in a:
        #print(test)
        i = i+1
        final = []
        test = test.drop(['label'], axis=1)
        b = model.predict(test)
        counts = Counter(b).most_common(1)
        final.append(counts[0][0])
        final.extend(['TEST' + str(i)])
        #print(final)
        result.append(final)
    print(result)
    result = pd.DataFrame(result,columns = columns)
    result.to_csv('E:/learningsource/code/移动互联网应用/大作业/第二次数据集/final_result2_ram.csv',index = False)



train()
test_model()
test_lightgbm()
test2()

