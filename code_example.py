import sklearn 
from sklearn import metrics
import numpy as np

from random import shuffle

from scipy.stats import spearmanr
from scipy.stats import kendalltau as kt

def NDCG(rank1, rank2, k=None):
    return sklearn.metrics.ndcg_score(rank1, rank2, k=k)


t = np.arange(1,100)
t_asarray = np.asarray([t])

shuffle(t)
rank1_t_asarray = np.asarray([t])

k = 45

count_NDCG = 0

for j in range(1000):
    
    shuffle(t)
    rank2_t_asarray = np.asarray([t])
    
    if kt(rank1_t_asarray, t_asarray)[0] < kt(rank2_t_asarray, t_asarray)[0]:

        if NDCG(rank1_t_asarray, t_asarray) > NDCG(rank2_t_asarray, t_asarray):
            count_NDCG += 1
            print('count_NDCG ', count_NDCG) 