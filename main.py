import random
import math

import numpy as np
import measures as m
from inspect import signature

#Initialize Arrays
arr_length = 20
k = int(arr_length/3)
j = int(2*(arr_length/3))

factorial = math.factorial(arr_length)
print("Factorial: " + str(factorial))

S = np.arange(1, arr_length + 1)
R1 = np.arange(1, arr_length + 1)
R2 = np.arange(1, arr_length + 1)

#Loop with different measures
def comparison(measure1, measure2, string1, string2, j=None, k=None):
    seed1 = i = 0
    seed2 = factorial

    sig1 = signature(measure1)
    params1 = sig1.parameters
    sig2 = signature(measure2)
    params2 = sig2.parameters

    while i < factorial:
        random.Random(seed1).shuffle(R1)
        random.Random(seed2).shuffle(R2)
        #np.random.shuffle(R1)
        #np.random.shuffle(R2)

        if k is None and j is None:
            m1 = measure1(S, R1, R2)
            m2 = measure2(S, R1, R2)

        elif len(params1) == 3 and len(params2) == 4:
            m1 = measure1(S, R1, R2)
            m2 = measure2(S, R1, R2, k)

        elif len(params1) == 4 and len(params2) == 3:
            m1 = measure1(S, R1, R2, k)
            m2 = measure2(S, R1, R2)

        elif len(params1) == 3 and len(params2) == 4:
            m1 = measure1(S, R1, R2)
            m2 = measure2(S, R1, R2, k)

        elif len(params1) == 3 and len(params2) == 5:
            m1 = measure1(S, R1, R2)
            m2 = measure2(S, R1, R2, j, k)

        elif len(params1) == 5 and len(params2) == 3:
            m1 = measure1(S, R1, R2, j, k)
            m2 = measure2(S, R1, R2)

        elif len(params1) == 4 and len(params2) == 4:
            m1 = measure1(S, R1, R2, k)
            m2 = measure2(S, R1, R2, k)

        elif len(params1) == 4 and len(params2) == 5:
            m1 = measure1(S, R1, R2, k)
            m2 = measure2(S, R1, R2, j, k)

        elif len(params1) == 5 and len(params2) == 4:
            m1 = measure1(S, R1, R2, j, k)
            m2 = measure2(S, R1, R2, k)

        else:
            m1 = measure1(S, R1, R2, j, k)
            m2 = measure2(S, R1, R2, j, k)




        if ((m1[0] < m1[1]) and (m2[0] > m2[1]) or (m1[0] > m1[1]) and (m2[0] < m2[1])):
            print("\n", "S:" + str(S))
            print("R1:" + str(R1))
            print("R2:" + str(R2), "\n")
            print(string1)
            print(m1[0], m1[1], "\n")
            print(string2)
            print(m2[0], m2[1])
            break

        #if(i==1000):
        #    break

        #print("Iteration: ", i)
        i = i + 1
        seed1 = seed1 + 1
        seed2 = seed2 - 1

    if i >= factorial:
        print("\n")
        print("NOT FOUND!!!" + " - " + string1 + " & " + string2)


#Kendall rank correlation coefficient & Spearman's rank correlation coefficient
comparison(m.kendall_rank_correlation, m.spearmans_rank_correlation_coefficient, "Kendall rank correlation coefficient", "Spearman's rank correlation coefficient")

#Kendall rank correlation coefficient & Discounted Cumulative Gain
comparison(m.kendall_rank_correlation, m.discounted_cumulative_gain, "Kendall rank correlation coefficient", "Discounted Cumulative Gain")

#Kendall rank correlation coefficient & Normalized Discounted Cumulative Gain
comparison(m.kendall_rank_correlation, m.normalized_discounted_cumulative_gain, "Kendall rank correlation coefficient", "Normalized Discounted Cumulative Gain")

#Kendall rank correlation coefficient & Precision@k
comparison(m.kendall_rank_correlation, m.precision_at_k, "Kendall rank correlation coefficient", "Precision@k", k=k)

#Kendall rank correlation coefficient & Recall@k
comparison(m.kendall_rank_correlation, m.recall_at_k, "Kendall rank correlation coefficient", "Recall@k", j, k=k)

#Kendall rank correlation coefficient & F1 Score@k
comparison(m.kendall_rank_correlation, m.f1_score_at_k, "Kendall rank correlation coefficient", "F1 Score@k", j, k=k)

#Kendall rank correlation coefficient & Fall-out@k
comparison(m.kendall_rank_correlation, m.fall_out_at_k, "Kendall rank correlation coefficient", "Fall-out@k", j, k=k)



#Spearman's rank correlation coefficient & Discounted Cumulative Gain
comparison(m.spearmans_rank_correlation_coefficient, m.discounted_cumulative_gain, "Spearman's rank correlation coefficient", "Discounted Cumulative Gain")

#Spearman's rank correlation coefficient & Normalized Discounted Cumulative Gain
comparison(m.spearmans_rank_correlation_coefficient, m.normalized_discounted_cumulative_gain, "Spearman's rank correlation coefficient", "Normalized Discounted Cumulative Gain")

#Spearman's rank correlation coefficient & Precision@k
comparison(m.spearmans_rank_correlation_coefficient, m.precision_at_k, "Spearman's rank correlation coefficient", "Precision@k", k=k)

#Spearman's rank correlation coefficient & Recall@k
comparison(m.spearmans_rank_correlation_coefficient, m.recall_at_k, "Spearman's rank correlation coefficient", "Recall@k", j, k=k)

#Spearman's rank correlation coefficient & F1 Score@k
comparison(m.spearmans_rank_correlation_coefficient, m.f1_score_at_k, "Spearman's rank correlation coefficient", "F1 Score@k", j, k=k)

#Spearman's rank correlation coefficient & Fall-out@k
comparison(m.spearmans_rank_correlation_coefficient, m.fall_out_at_k, "Spearman's rank correlation coefficient", "Fall-out@k", j, k=k)



#Discounted Cumulative Gain & Normalized Discounted Cumulative Gain
#comparison(m.discounted_cumulative_gain, m.normalized_discounted_cumulative_gain, "Discounted Cumulative Gain", "Normalized Discounted Cumulative Gain")

#Discounted Cumulative Gain & Precision@k
comparison(m.discounted_cumulative_gain, m.precision_at_k, "Discounted Cumulative Gain", "Precision@k", k=k)

#Discounted Cumulative Gain & Recall@k
comparison(m.discounted_cumulative_gain, m.recall_at_k, "Discounted Cumulative Gain", "Recall@k", j, k=k)

#Discounted Cumulative Gain & F1 Score@k
comparison(m.discounted_cumulative_gain, m.f1_score_at_k, "Discounted Cumulative Gain", "F1 Score@k", j, k=k)

#Discounted Cumulative Gain & Fall-out@k
comparison(m.discounted_cumulative_gain, m.fall_out_at_k, "Discounted Cumulative Gain", "Fall-out@k", j, k=k)



#Normalized Discounted Cumulative Gain & Precision@k
comparison(m.normalized_discounted_cumulative_gain, m.precision_at_k, "Normalized Discounted Cumulative Gain", "Precision@k", k=k)

#Normalized Discounted Cumulative Gain & Recall@k
comparison(m.normalized_discounted_cumulative_gain, m.recall_at_k, "Normalized Discounted Cumulative Gain", "Recall@k", j, k=k)

#Normalized Discounted Cumulative Gain & F1 Score@k
comparison(m.normalized_discounted_cumulative_gain, m.f1_score_at_k, "Normalized Discounted Cumulative Gain", "F1 Score@k", j, k=k)

#Normalized Discounted Cumulative Gain & Fall-out@k
comparison(m.normalized_discounted_cumulative_gain, m.fall_out_at_k, "Normalized Discounted Cumulative Gain", "Fall-out@k", j, k=k)



#Precision@k & Recall@k
comparison(m.precision_at_k, m.recall_at_k, "Precision@k", "Recall@k", j, k=k)

#Precision@k & F1 Score@k
#comparison(m.precision_at_k, m.f1_score_at_k, "Precision@k", "F1 Score@k", j, k=k)

#Precision@k & Fall-out@k
comparison(m.precision_at_k, m.fall_out_at_k, "Precision@k", "Fall-out@k", j, k=k)



#Recall@k & F1 Score@k
comparison(m.recall_at_k, m.f1_score_at_k, "Recall@k", "F1 Score@k", j, k=k)

#Recall@k & Fall-out@k
comparison(m.recall_at_k, m.fall_out_at_k, "Recall@k", "Fall-out@k", j, k=k)



#F1 Score@k & Fall-out@k
comparison(m.f1_score_at_k, m.fall_out_at_k, "F1 Score@k", "Fall-out@k", j, k=k)

