# -*- coding: cp936 -*-
data_set = [ 9,1,22,31,45,3,6,2,11 ]
 
loop_count = 0
for j in range(len(data_set)):
    for i in range(len(data_set) - j- 1): # -1 ����Ϊÿ�αȶԵĶ� ��i ��i +1,����1�Ļ�,���һ�ζԱȻᳬ��list ��ȡ��Χ,-j����Ϊ,ÿһ�δ�loop�ʹ����������һ�����ֵ,�������б������,�´�loop�Ͳ����������Ѿ�������˵�ֵ ��
        if data_set[i] > data_set[i+1]: #switch
            tmp = data_set[i]
            data_set[i] = data_set[i+1]
            data_set[i+1] = tmp
        loop_count +=1
    print data_set
print data_set             # ������Ҫ���ǱȽϴ�С��ȷ�����һ������������ǰ
print("loop times", loop_count)