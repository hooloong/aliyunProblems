#coding:utf-8
import pandas as pd
import numpy as np
import time
#拼接数据
def merge_table(df):
    df['field_results'] = df['field_results'].astype(str)
    if df.shape[0] > 1:
        merge_df = "".join(list(df['field_results']))
    else:
        merge_df = df['field_results'].value[0]
    return merge_df

if __name__ == '__main__':
    begin_time = time.time()
    data_part1 = pd.read_csv('f_train_20180204.csv',encoding='GBK')

    data_part2 = pd.read_csv('f_train_20180204.csv',encoding="GBK")

    #统计item的行数
    print(len(set(data_part1.id)))
    print(len(set(data_part2.id)))
    #打印前五行
    print(data_part1.head(5))
    #打印后五行
    print(data_part1.tail(5))
    #打印所有列标签
    print(data_part1.columns)

    #改变列标签
    df2 = data_part1.rename(columns={'SNP1':'SNP99'})
    data_part1.rename(columns={'SNP1': 'SNP99'},inplace=True)
    print(data_part1.head(5))

    #选择列或者行
    print("******************************")
    print(data_part1[['id','SNP3']])
    print(data_part1[(data_part1['SNP3'] > 2) & (data_part1['SNP11'] == 3)])

    #处理 丢失项目
    # dropna 若有丢失项目，就把改行该列丢掉
    data_part1.dropna()
    # fillna 填充丢失项
    #data_part2.fillna(value = 0) 可以填充平均值
    mean = data_part2['SNP11'].mean()
    data_part2['SNP11'].fillna(mean)

    #创建新列
    data_part1['newSNP1'] = data_part1['SNP11']
    data_part1['newSNP2'] = data_part1['SNP11'] + 10
    data_part1['newSNP3'] = data_part1['SNP11'] + data_part1['SNP12']
    print("创建新列。。。。。")
    print(data_part1.head(5))

    #groupby,聚合，分组级运算
    print("groupby...............")
    print(data_part1.groupby('SNP11').sum())
    print(data_part1.groupby(['SNP11','SNP12']).count())
    #透视表操作
    print("pivot......table....")
    df1 = pd.pivot_table(data_part1, values='newSNP1',index=['newSNP2','newSNP3'],columns=['SNP4'])
    print(df1.head(5))
    df2 = pd.pivot_table(data_part1, values='newSNP1', index=['newSNP2', 'newSNP3'], columns=['SNP4'], aggfunc=len)
    print(df2.head(5))

    #按照指定的行和列统计分组频数
    pd.crosstab(data_part1.newSNP3,data_part1.newSNP2)

    #merge concat
    pd.merge(data_part1,data_part2,on='SNP2',how='inner')  #left right outer

    #Map
    data_part1['newSNP1'].map(lambda x:10+x)

    #Apply
    data_part1[['newSNP1','newSNP2']].apply(sum)
    func = lambda x:x+2
    data_part1.applymap(func)

    #unique() 返回唯一值
    print(data_part1['newSNP2'].unique())

    #describe() 返回统计值 cov  Correlation
    print(data_part1.describe())
    print(data_part1.cov())
    print(data_part1.corr())
    print(time.time() - begin_time)

