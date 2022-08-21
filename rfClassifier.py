from os import replace
from sys import meta_path
import pandas as pd
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import csv
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import cross_val_score

# CSV_PATH = '/home/moumi/ARG-Network_analysis/databases/all_features.csv'
CSV_PATH = '/home/moumi/ARG-Network_analysis/databases/updated_all_features.csv'
CSV_PATH2 = '/home/moumi/ARG-Network_analysis/databases/AB_all_features.csv'
META_PATH = '/home/moumi/ARG-Network_analysis/negative_set/metabol_genes_ecoli.txt'

data = read_csv(CSV_PATH)

D = data.values
x = D[:,1:-1]
y = D[:,-1]
y=y.astype('int')
'''
for (i,j), value in numpy.ndenumerate(x):
    print(x,y) 
'''
arg_x = []
arg_y = []
nonarg_x = []
nonarg_y = []
meta_genes = []
with open(META_PATH,'r') as f_meta:
    lines = f_meta.readlines()
    for line in lines:
        meta_genes.append(line.strip())

for i in range(len(x)):
    if y[i] == 1:
        arg_x.append(x[i])
        arg_y.append(y[i])
    else:
        if D[i,0] in meta_genes:
            nonarg_x.append(x[i])
            nonarg_y.append(y[i])

# nonarg_x_indexes = list(np.random.choice(len(nonarg_x), len(arg_y), replace = False))
# nonarg_x_under = []
# for j in nonarg_x_indexes:
#     nonarg_x_under.append(nonarg_x[j])

nonarg_x_under = nonarg_x[0:len(arg_y)]
x = arg_x + nonarg_x_under
y = arg_y + [0 for k in range(len(arg_y))]

x_tr, x_ts, y_tr, y_ts = train_test_split(x,y,test_size=0.20, random_state = 25)

model = RandomForestClassifier(n_estimators = 10, random_state = 20)

model.fit(x_tr,y_tr)
scores = cross_val_score(model, x, y, cv=10)

print("cv results ",scores.mean())

#modification: using ecoli as test only, AB as train only

# data2 = read_csv(CSV_PATH2)

# D2 = data2.values
# x2 = D2[:,1:-1]
# y2 = D2[:,-1]
# y2=y2.astype('int')
# '''
# for (i,j), value in numpy.ndenumerate(x):
#     print(x,y) 
# '''
# arg_x2 = []
# arg_y2 = []
# nonarg_x2 = []
# nonarg_y2 = []
# for i2 in range(len(x2)):
#     if y2[i2] == 1:
#         arg_x2.append(x2[i2])
#         arg_y2.append(y2[i2])
#     else:
#         nonarg_x2.append(x2[i2])
#         nonarg_y2.append(y2[i2])

# print(len(arg_y2))

# nonarg_x_indexes2 = list(np.random.choice(len(nonarg_x2), len(arg_y2), replace = False))
# nonarg_x_under2 = []
# for j2 in nonarg_x_indexes2:
#     nonarg_x_under2.append(nonarg_x2[j2])

# x2 = arg_x2 + nonarg_x_under2
# y2 = arg_y2 + [0 for k2 in range(len(arg_y2))]

#modification ends

pred = model.predict(x_ts)
print("Accuracy: ",accuracy_score(y_ts, pred))

with open(CSV_PATH, 'r') as ff:
    d_reader = csv.DictReader(ff)
    headers = d_reader.fieldnames

feature_list = list(headers[1:-1])
feature_imp = pd.Series(model.feature_importances_, index = feature_list).sort_values(ascending = False)
print(feature_imp)

cm = confusion_matrix(y_ts,pred)
print(cm)

print(precision_recall_fscore_support(y_ts, pred, average = 'binary'))