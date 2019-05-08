# -*- coding:utf-8 -*-

def jaccard_similarity(x, y):
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))
    return intersection / float(union)

def dice_similarity_coefficient(list_a,list_b):
    # 集合Aと集合Bの積集合(set型)を作成
    set_intersection = set.intersection(set(list_a),set(list_b))
    # 集合Aと集合Bの積集合の要素数
    num_intersection = len(set_intersection)
    
    # 集合Aの要素数を取得
    num_listA = len(list_a)
    # 集合Bの要素数を取得
    num_listB = len(list_b)
    
    # 定義式に伴いDice係数を算出
    try:
        return float(2.0 * num_intersection) / (num_listA + num_listB)
    except ZeroDivisionError:
        return 1.0

# Simpson係数
def overlap_coefficient(list_a,list_b):
    #　集合Aと集合Bの積集合(set型)を作成
    set_intersection = set.intersection(set(list_a),set(list_b))
    # 集合Aと集合Bの積集合
    num_intersection = len(set_intersection)
    
    # 集合Aの要素数を取得
    num_listA = len(list_a)
#     集合Bの要素数を取得
    num_listB = len(list_b)
    try:
        return float(num_intersection) / min([num_listA,num_listB])
    except ZeroDivisionError:
        return 1.0
