import numpy as np

from scipy.stats import kendalltau as kt
from scipy.stats import spearmanr as sr

from sklearn.metrics import dcg_score as dcg
from sklearn.metrics import ndcg_score as ndcg

from sklearn.metrics import precision_score as ps
from sklearn.metrics import recall_score as rs
from sklearn.metrics import f1_score as f_one

#Kendall rank correlation coefficient
def kendall_rank_correlation(arr1, arr2, arr3):
    tau1 = kt(arr1,arr2)
    tau2 = kt(arr1,arr3)
    #print("Kendall rank correlation coefficient")
    #print(tau1[0], tau2[0], "\n")
    return(tau1[0], tau2[0])

#Spearman's rank correlation coefficient
def spearmans_rank_correlation_coefficient(arr1, arr2, arr3):
    r1 = sr(arr1,arr2)
    r2 = sr(arr1,arr3)

    #print("Spearman's rank correlation coefficient")
    #print(r1[0], r2[0], "\n")
    return(r1[0], r2[0])

#Discounted Cumulative Gain
def discounted_cumulative_gain(arr1, arr2, arr3):
    dcg1 = dcg([arr1], [arr2])
    dcg2 = dcg([arr1], [arr3])
    #print("Discounted Cumulative Gain")
    #print(dcg1, dcg2, "\n")
    return(dcg1, dcg2)

#Normalized Discounted Cumulative Gain
def normalized_discounted_cumulative_gain(arr1, arr2, arr3):
    ndcg1 = ndcg([arr1], [arr2])
    ndcg2 = ndcg([arr1], [arr3])
    #print("Normalized Discounted Cumulative Gain")
    #print(ndcg1, ndcg2, "\n")
    return(ndcg1,ndcg2)

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


def precision_at_k(rank1, rank2, rank3, k):
    precision1 = len(set(rank1[:k]) & set(rank2[:k])) / k
    precision2 = len(set(rank1[:k]) & set(rank3[:k])) / k
    return (precision1, precision2)

def recall_at_k(rank1, rank2, rank3, j, k):
    recall1 = len(set(rank1[:j]) & set(rank2[:k])) / len(rank1[:j])
    recall2 = len(set(rank1[:j]) & set(rank3[:k])) / len(rank1[:j])
    return (recall1, recall2)

def f1_score_at_k(rank1, rank2, rank3, j, k):
    try:
        f_one1 = 2 * precision_at_k(rank1, rank2, rank3, k)[0] * recall_at_k(rank1, rank2, rank3, j, k)[0] / (precision_at_k(rank1, rank2, rank3, k)[0] * recall_at_k(rank1, rank2, rank3, j, k)[0])
    except:
        f_one1 = 0
    try:
        f_one2 = 2 * precision_at_k(rank1, rank2, rank3, k)[1] * recall_at_k(rank1, rank2, rank3, j, k)[1] / (precision_at_k(rank1, rank2, rank3, k)[1] * recall_at_k(rank1, rank2, rank3, j, k)[1])
    except:
        f_one2 = 0
    return (f_one1, f_one2)

def fall_out_at_k(rank1, rank2, rank3, j, k):
    fall_out1 = len(set(rank1[j:]) & set(rank2[:k])) / len(rank1[j:])
    fall_out2 = len(set(rank1[j:]) & set(rank3[:k])) / len(rank1[j:])
    return (fall_out1, fall_out2)




