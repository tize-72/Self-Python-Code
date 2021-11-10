"""
author：QiZhao
date : 2021.11.10
"""

import numpy as np
import pandas as pd

# reading all names
data_name_all = pd.read_excel(r'/Users/tize-72/Desktop/OneDrive/总结文档.xlsx', sheet_name="All_name")
data_name_all.rename(columns={'Unnamed: 0': "姓名"}, inplace=True)
names = data_name_all['姓名']
names = list(names)
# begin reading single names
data_name_single = pd.read_excel(r'/Users/tize-72/Desktop/OneDrive/总结文档.xlsx', sheet_name="Single_record")
# print(data_name_single)
names_single = data_name_single['姓名']
names_single = list(names_single)
# print(names_single)

notDo = []
for item in names:
    if item not in names_single:
        notDo.append(item)
# print(notDo)
print('目前还未进行青年大学习的同学有:')
for x in notDo:
    print(x)
