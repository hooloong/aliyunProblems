import os
import random
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale  # 使用scikit-learn进行数据预处理

user_data_file = "../../data/fresh_comp_offline/tianchi_fresh_comp_train_user.csv"
goods_data_file = "../../data/fresh_comp_offline/tianchi_fresh_comp_train_item.csv"

user_data = pd.read_csv(user_data_file, header=0)
goods_data = pd.read_csv(goods_data_file, header=0)
goods_data.to_csv("./items.csv",index=False,index_label=False, columns=["item_geohash"],)
# train_goods = scale(np.asarray(goods_data.ix[:, 2]))
# train_user_data = scale(np.asarray(goods_data.ix[:, 2]))
# print(train_user_data)