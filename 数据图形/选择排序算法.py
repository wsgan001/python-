# -*- coding: cp936 -*-
data_set = [ 9,1,22,31,45,3,6,2,11 ]
 
smallest_num_index = 0 #��ʼ�б���Сֵ,Ĭ��Ϊ��һ��

loop_count = 0
for j in range(len(data_set)):
    for i in range(j,len(data_set)):
        if data_set[i] < data_set[smallest_num_index]: #��ǰֵ ��֮ǰѡ��������Сֵ ��ҪС,�ǾͰ���������Сֵ
            smallest_num_index = i
        loop_count +=1
    else:
        print("smallest num is ",data_set[smallest_num_index])
        tmp = data_set[smallest_num_index]
        data_set[smallest_num_index] =  data_set[j]
        data_set[j] = tmp

    print(data_set)
    print("loop times", loop_count)
    # ��ȷ��Ԫ������С�������ڵ�һλ��Ȼ��˳������ȷ��