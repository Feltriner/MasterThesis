import numpy as np

from scipy.stats import kendalltau as kt
from scipy.stats import spearmanr as sr

from sklearn.metrics import dcg_score as dcg
from sklearn.metrics import ndcg_score as ndcg

from sklearn.metrics import precision_score as ps
from sklearn.metrics import recall_score as rs
from sklearn.metrics import f1_score as f_one

from rexmex import ranking as r, classification as c
from sklearn.metrics import average_precision_score as aps
from sklearn.metrics import roc_auc_score as ras




arr1 = [1,2,3,4,5]
arr2 = [3,1,5,2,4]
arr3 = [5,3,4,2,1]



#Kendall rank correlation coefficient
def kendall_rank_correlation(rank1, rank2, rank3):
    tau1 = kt(rank1,rank2)
    tau2 = kt(rank1,rank3)
    #print("Kendall rank correlation coefficient")
    #print(tau1[0], tau2[0], "\n")
    return tau1[0], tau2[0]

#Spearman's rank correlation coefficient
def spearmans_rank_correlation_coefficient(rank1, rank2, rank3):
    r1 = sr(rank1,rank2)
    r2 = sr(rank1,rank3)

    #print("Spearman's rank correlation coefficient")
    #print(r1[0], r2[0], "\n")
    return r1[0], r2[0]

#Discounted Cumulative Gain
def discounted_cumulative_gain(rank1, rank2, rank3):
    dcg1 = dcg([rank1], [rank2])
    dcg2 = dcg([rank1], [rank3])
    #print("Discounted Cumulative Gain")
    #print(dcg1, dcg2, "\n")
    return dcg1, dcg2

#Normalized Discounted Cumulative Gain
def normalized_discounted_cumulative_gain(rank1, rank2, rank3):
    ndcg1 = ndcg([rank1], [rank2])
    ndcg2 = ndcg([rank1], [rank3])
    #print("Normalized Discounted Cumulative Gain")
    #print(ndcg1, ndcg2, "\n")
    return ndcg1, ndcg2

"""
#Precision
def precision(arr1, arr2, arr3):
    precision1 = ps(arr1, arr2, average=None)
    precision2 = ps(arr1, arr3, average=None)

    precision_count1 = np.count_nonzero(precision1 == 1)
    precision_count2 = np.count_nonzero(precision2 == 1)

    #print("Precision")
    #print(precision1, precision2)
    #print(precision_count1, precision_count2, "\n")
    return(precision_count1, precision_count2)

#Precision@k
def precision_at_k(arr1, arr2, arr3, k):
    precision1 = ps(arr1, arr2, average=None)
    precision2 = ps(arr1, arr3, average=None)

    precision_count_at_k1 = np.count_nonzero(precision1[:k] == 1)
    precision_count_at_k2 = np.count_nonzero(precision2[:k] == 1)

    #print("Precision@" + str(k))
    #print(precision_count_at_k1, precision_count_at_k2, "\n")
    return(precision_count_at_k1, precision_count_at_k2)

#Recall
def recall(arr1, arr2, arr3):
    recall1 = rs(arr1, arr2, average=None)
    recall2 = rs(arr1, arr3, average=None)

    recall_count1 = np.count_nonzero(recall1 == 1)
    recall_count2 = np.count_nonzero(recall2 == 1)

    #print("Recall")
    #print(recall1, recall2)
    #print(recall_count1, recall_count2, "\n")
    return(recall_count1, recall_count2)

#F1 Score
def f1_score(arr1, arr2, arr3):
    f_one1 = f_one(arr1, arr2, average=None)
    f_one2 = f_one(arr1, arr3, average=None)

    f_one_count1 = np.count_nonzero(f_one1 == 1)
    f_one_count2 = np.count_nonzero(f_one2 == 1)

    #print("F1 Score")
    #print(f_one1, f_one2)
    #print(f_one_count1, f_one_count2, "\n")
    return(f_one_count1, f_one_count2)
"""

#Precision@k
def precision_at_k(rank1, rank2, rank3, k):
    precision1 = len(set(rank1[:k]) & set(rank2[:k])) / k
    precision2 = len(set(rank1[:k]) & set(rank3[:k])) / k
    return precision1, precision2

#Recall@k
def recall_at_k(rank1, rank2, rank3, j, k):
    recall1 = len(set(rank1[:j]) & set(rank2[:k])) / len(rank1[:j])
    recall2 = len(set(rank1[:j]) & set(rank3[:k])) / len(rank1[:j])
    return recall1, recall2

#F1-Score@k
def f1_score_at_k(rank1, rank2, rank3, j, k):
    try:
        f_one1 = 2 * precision_at_k(rank1, rank2, rank3, k)[0] * recall_at_k(rank1, rank2, rank3, j, k)[0] / (precision_at_k(rank1, rank2, rank3, k)[0] * recall_at_k(rank1, rank2, rank3, j, k)[0])
    except:
        f_one1 = 0
    try:
        f_one2 = 2 * precision_at_k(rank1, rank2, rank3, k)[1] * recall_at_k(rank1, rank2, rank3, j, k)[1] / (precision_at_k(rank1, rank2, rank3, k)[1] * recall_at_k(rank1, rank2, rank3, j, k)[1])
    except:
        f_one2 = 0
    return f_one1, f_one2

#Fall-Out@k
def fall_out_at_k(rank1, rank2, rank3, j, k):
    fall_out1 = len(set(rank1[j:]) & set(rank2[:k])) / len(rank1[j:])
    fall_out2 = len(set(rank1[j:]) & set(rank3[:k])) / len(rank1[j:])
    return fall_out1, fall_out2


#Mean Reciprocal Rank (MMR)
def mean_reciprocal_rank(rank1, rank2, rank3, k):
    arr1 = rank1[:k]
    sum2 = 0
    sum3 = 0

    for item in arr1:
        if item in rank2:
            rank = rank2.index(item) + 1
            reciprocal_rank2 = 1 / rank
            sum2 += reciprocal_rank2
        if item in rank3:
            rank = rank3.index(item) + 1
            reciprocal_rank3 = 1 / rank
            sum3 += reciprocal_rank3

    result1 = sum2 / len(rank1)
    result2 = sum3 / len(rank1)
    return result1, result2
#print(mean_reciprocal_rank(arr1,arr2,arr3,3))


#Hit-Rate@k
def hit_rate_at_k(rank1, rank2, rank3, k):
    hit_rate1 = len(set(rank1[:k]) & set(rank2[:k])) / min(len(set(rank1[:k])),k)
    hit_rate2 = len(set(rank1[:k]) & set(rank3[:k])) / min(len(set(rank1[:k])),k)
    return hit_rate1, hit_rate2


#mean Average Precision@k (mAP)
def mean_average_precision_at_k(rank1, rank2, rank3,k):
    arr1 = [rank1[:k]]
    arr2 = [rank2[:k]]
    arr3 = [rank3[:k]]

    map1 = r.mean_average_precision_at_k(arr1, arr2, k)
    map2 = r.mean_average_precision_at_k(arr1, arr3, k)

    return map1, map2
#print(mean_average_precision_at_k(arr1,arr2,arr3,3))

#arr1 = [1,1,1,0]
#arr2 = [1,1,0,1]
#arr3 = [0,0,0,0]

#Area Under The Curve - ROC curve@k (AUC-ROC)
def area_under_the_curve_receiver_operator_characteristic_at_k(rank1, rank2, rank3, k):
    arr1 = rank1[:k]
    arr2 = rank2
    arr3 = rank3

    arr1_transformed = []
    arr2_transformed = []
    arr3_transformed = []

    for item in range(k):
            arr1_transformed.append(1)
    for item in range(len(rank1)-k):
            arr1_transformed.append(0)

    for item in arr2:
        if item in arr1:
            arr2_transformed.append(1)
        else:
            arr2_transformed.append(0)

    for item in arr3:
        if item in arr1:
            arr3_transformed.append(1)
        else:
            arr3_transformed.append(0)

    #print(arr1_transformed,arr2_transformed,arr3_transformed)

    rocauc1 = ras(arr1_transformed, arr2_transformed)
    rocauc2 = ras(arr1_transformed, arr3_transformed)
    return rocauc1, rocauc2


#print(area_under_the_curve_receiver_operator_characteristic(arr1, arr2, arr3, 3))


#Area Under the Precision-Recall Curve@k (PRAUC)
def area_under_the_precision_recall_curve_at_k(rank1, rank2, rank3, k):
    arr1 = rank1[:k]
    arr2 = rank2
    arr3 = rank3

    arr1_transformed = []
    arr2_transformed = []
    arr3_transformed = []

    for item in range(k):
        arr1_transformed.append(1)
    for item in range(len(rank1) - k):
        arr1_transformed.append(0)

    for item in arr2:
        if item in arr1:
            arr2_transformed.append(1)
        else:
            arr2_transformed.append(0)

    for item in arr3:
        if item in arr1:
            arr3_transformed.append(1)
        else:
            arr3_transformed.append(0)

    # print(arr1_transformed,arr2_transformed,arr3_transformed)

    prauc1 = aps(arr1_transformed, arr2_transformed)
    prauc2 = aps(arr1_transformed, arr3_transformed)
    return prauc1, prauc2

#print(area_under_the_precision_recall_curve(arr1,arr2,arr3, 3))


