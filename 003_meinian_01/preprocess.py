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
    data_part1 = pd.read_csv('../../data/aliyun_meinian/meinian_round1_data_part1_20180408.csv', sep='$')

    data_part2 = pd.read_csv('../../data/aliyun_meinian/meinian_round1_data_part2_20180408.csv', sep='$')

    print(len(set(data_part1.table_id)))
    print(len(set(data_part2.table_id)))
    data_part1_2 = pd.concat([data_part1,data_part2])
    data_part1_2 = pd.DataFrame(data_part1_2).sort_values('vid').reset_index(drop=True)
    #拼接数据
    print(data_part1_2.shape)
    is_happen = data_part1_2.groupby(['vid', 'table_id']).size().reset_index()
    #重新index来除重
    is_happen['new_index' ] = is_happen['vid'] + '_' + is_happen['table_id']
    is_happen_new = is_happen[is_happen[0] > 1]['new_index']
    data_part1_2['new_index'] = data_part1_2['vid'] + '_' + data_part1_2['table_id']

    unique_part = data_part1_2[data_part1_2['new_index'].isin(list(is_happen_new))]
    unique_part = unique_part.sort_values(['vid', 'table_id'])
    no_unique_part = data_part1_2[~data_part1_2['new_index'].isin(list(is_happen_new))]
    print("start....")
    data_part1_2_not_unique = unique_part.groupby(['vid','table_id']).apply(merge_table).reset_index()
    data_part1_2_not_unique.rename(columns={0:'field_results'},inplace=True)
    print("---------------")

    tmp = pd.concat([data_part1_2_not_unique, no_unique_part[['vid','table_id','filed_results']]])
    # 行列转换
    print("finish")
    tmp = tmp.pivot(index='vid',values='field_results',columns='tables')
    tmp.to_csv("../../data/aliyun_meinian/tmp.csv")
    print(tmp.shape)

    print(time.time() - begin_time)

