import random
import math

import numpy as np
import measures as m
from inspect import signature

#Initialize Arrays
arr_length = 9
#k = int(arr_length/3)
#j = int(2*(arr_length/3))
k = 7
j = 4

factorial = math.factorial(arr_length)
iterations = int(factorial/2)
print("Factorial: " + str(factorial))
print("Iterations: " + str(iterations))

S = np.arange(1, arr_length + 1).tolist()
R1 = np.arange(1, arr_length + 1).tolist()
R2 = np.arange(1, arr_length + 1).tolist()

#Loop with different measures
def comparison(measure1, measure2, string1, string2, j=None, k=None):
    seed1 = i = 0
    seed2 = factorial

    sig1 = signature(measure1)
    params1 = sig1.parameters
    sig2 = signature(measure2)
    params2 = sig2.parameters


    while i < iterations:
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

        if(i==iterations-1):
            print("\n")
            print("NOT FOUND!!!" + " - " + string1 + " & " + string2)
            break

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

#Kendall rank correlation coefficient & Mean Reciprocal Rank (MMR)
comparison(m.kendall_rank_correlation, m.mean_reciprocal_rank, "Kendall rank correlation coefficient", "Mean Reciprocal Rank (MMR)", k=k)

#Kendall rank correlation coefficient & Hit-Rate@k
comparison(m.kendall_rank_correlation, m.hit_rate_at_k, "Kendall rank correlation coefficient", "Hit-Rate@k", k=k)

#Kendall rank correlation coefficient & mean Average Precision@k (mAP)
comparison(m.kendall_rank_correlation, m.mean_average_precision_at_k, "Kendall rank correlation coefficient", "mean Average Precision@k (mAP)", k=k)

#Kendall rank correlation coefficient & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.kendall_rank_correlation, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Kendall rank correlation coefficient", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Kendall rank correlation coefficient & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.kendall_rank_correlation, m.area_under_the_precision_recall_curve_at_k, "Kendall rank correlation coefficient", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



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

#Spearman's rank correlation coefficient & Mean Reciprocal Rank (MMR)
comparison(m.spearmans_rank_correlation_coefficient, m.mean_reciprocal_rank, "Spearman's rank correlation coefficient", "Mean Reciprocal Rank (MMR)", k=k)

#Spearman's rank correlation coefficient & Hit-Rate@k
comparison(m.spearmans_rank_correlation_coefficient, m.hit_rate_at_k, "Spearman's rank correlation coefficient", "Hit-Rate@k", k=k)

#Spearman's rank correlation coefficient & mean Average Precision@k (mAP)
comparison(m.spearmans_rank_correlation_coefficient, m.mean_average_precision_at_k, "Spearman's rank correlation coefficient", "mean Average Precision@k (mAP)", k=k)

#Spearman's rank correlation coefficient & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.spearmans_rank_correlation_coefficient, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Spearman's rank correlation coefficient", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Spearman's rank correlation coefficient & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.spearmans_rank_correlation_coefficient, m.area_under_the_precision_recall_curve_at_k, "Spearman's rank correlation coefficient", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



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

#Discounted Cumulative Gain & Mean Reciprocal Rank (MMR)
comparison(m.discounted_cumulative_gain, m.mean_reciprocal_rank, "Discounted Cumulative Gain", "Mean Reciprocal Rank (MMR)", k=k)

#Discounted Cumulative Gain & Hit-Rate@k
comparison(m.discounted_cumulative_gain, m.hit_rate_at_k, "Discounted Cumulative Gain", "Hit-Rate@k", k=k)

#Discounted Cumulative Gain & mean Average Precision@k (mAP)
comparison(m.discounted_cumulative_gain, m.mean_average_precision_at_k, "Discounted Cumulative Gain", "mean Average Precision@k (mAP)", k=k)

#Discounted Cumulative Gain & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.discounted_cumulative_gain, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Discounted Cumulative Gain", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Discounted Cumulative Gain & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.discounted_cumulative_gain, m.area_under_the_precision_recall_curve_at_k, "Discounted Cumulative Gain", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Normalized Discounted Cumulative Gain & Precision@k
comparison(m.normalized_discounted_cumulative_gain, m.precision_at_k, "Normalized Discounted Cumulative Gain", "Precision@k", k=k)

#Normalized Discounted Cumulative Gain & Recall@k
comparison(m.normalized_discounted_cumulative_gain, m.recall_at_k, "Normalized Discounted Cumulative Gain", "Recall@k", j, k=k)

#Normalized Discounted Cumulative Gain & F1 Score@k
comparison(m.normalized_discounted_cumulative_gain, m.f1_score_at_k, "Normalized Discounted Cumulative Gain", "F1 Score@k", j, k=k)

#Normalized Discounted Cumulative Gain & Fall-out@k
comparison(m.normalized_discounted_cumulative_gain, m.fall_out_at_k, "Normalized Discounted Cumulative Gain", "Fall-out@k", j, k=k)

#Normalized Discounted Cumulative Gain & Mean Reciprocal Rank (MMR)
comparison(m.normalized_discounted_cumulative_gain, m.mean_reciprocal_rank, "Normalized Discounted Cumulative Gain", "Mean Reciprocal Rank (MMR)", k=k)

#Normalized Discounted Cumulative Gain & Hit-Rate@k
comparison(m.normalized_discounted_cumulative_gain, m.hit_rate_at_k, "Normalized Discounted Cumulative Gain", "Hit-Rate@k", k=k)

#Normalized Discounted Cumulative Gain & mean Average Precision@k (mAP)
comparison(m.normalized_discounted_cumulative_gain, m.mean_average_precision_at_k, "Normalized Discounted Cumulative Gain", "mean Average Precision@k (mAP)", k=k)

#Normalized Discounted Cumulative Gain & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.normalized_discounted_cumulative_gain, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Normalized Discounted Cumulative Gain", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Normalized Discounted Cumulative Gain & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.normalized_discounted_cumulative_gain, m.area_under_the_precision_recall_curve_at_k, "Normalized Discounted Cumulative Gain", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Precision@k & Recall@k
comparison(m.precision_at_k, m.recall_at_k, "Precision@k", "Recall@k", j, k=k)

#Precision@k & F1 Score@k
comparison(m.precision_at_k, m.f1_score_at_k, "Precision@k", "F1 Score@k", j, k=k)

#Precision@k & Fall-out@k
comparison(m.precision_at_k, m.fall_out_at_k, "Precision@k", "Fall-out@k", j, k=k)

#Precision@k & Mean Reciprocal Rank (MMR)
comparison(m.precision_at_k, m.mean_reciprocal_rank, "Precision@k", "Mean Reciprocal Rank (MMR)", k=k)

#Precision@k & Hit-Rate@k
comparison(m.precision_at_k, m.hit_rate_at_k, "Precision@k", "Hit-Rate@k", k=k)

#Precision@k & mean Average Precision@k (mAP)
comparison(m.precision_at_k, m.mean_average_precision_at_k, "Precision@k", "mean Average Precision@k (mAP)", k=k)

#Precision@k & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.precision_at_k, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Precision@k", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Precision@k & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.precision_at_k, m.area_under_the_precision_recall_curve_at_k, "Precision@k", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Recall@k & F1 Score@k
comparison(m.recall_at_k, m.f1_score_at_k, "Recall@k", "F1 Score@k", j, k=k)

#Recall@k & Fall-out@k
comparison(m.recall_at_k, m.fall_out_at_k, "Recall@k", "Fall-out@k", j, k=k)

#Recall@k & Mean Reciprocal Rank (MMR)
comparison(m.recall_at_k, m.mean_reciprocal_rank, "Recall@k", "Mean Reciprocal Rank (MMR)", k=k)

#Recall@k & Hit-Rate@k
comparison(m.recall_at_k, m.hit_rate_at_k, "Recall@k", "Hit-Rate@k", k=k)

#Recall@k & mean Average Precision@k (mAP)
comparison(m.recall_at_k, m.mean_average_precision_at_k, "Recall@k", "mean Average Precision@k (mAP)", k=k)

#Recall@k & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.recall_at_k, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Recall@k", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Recall@k & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.recall_at_k, m.area_under_the_precision_recall_curve_at_k, "Recall@k", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#F1 Score@k & Fall-out@k
comparison(m.f1_score_at_k, m.fall_out_at_k, "F1 Score@k", "Fall-out@k", j, k=k)

#F1 Score@k & Mean Reciprocal Rank (MMR)
comparison(m.f1_score_at_k, m.mean_reciprocal_rank, "F1 Score@k", "Mean Reciprocal Rank (MMR)", k=k)

#F1 Score@k & Hit-Rate@k
comparison(m.f1_score_at_k, m.hit_rate_at_k, "F1 Score@k", "Hit-Rate@k", k=k)

#F1 Score@k & mean Average Precision@k (mAP)
comparison(m.f1_score_at_k, m.mean_average_precision_at_k, "F1 Score@k", "mean Average Precision@k (mAP)", k=k)

#F1 Score@k & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.f1_score_at_k, m.area_under_the_curve_receiver_operator_characteristic_at_k, "F1 Score@k", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#F1 Score@k & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.f1_score_at_k, m.area_under_the_precision_recall_curve_at_k, "F1 Score@k", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Fall-Out@k & Mean Reciprocal Rank (MMR)
comparison(m.fall_out_at_k, m.mean_reciprocal_rank, "Fall-Out@k", "Mean Reciprocal Rank (MMR)", k=k)

#Fall-Out@k & Hit-Rate@k
comparison(m.fall_out_at_k, m.hit_rate_at_k, "Fall-Out@k", "Hit-Rate@k", k=k)

#Fall-Out@k & mean Average Precision@k (mAP)
comparison(m.fall_out_at_k, m.mean_average_precision_at_k, "Fall-Out@k", "mean Average Precision@k (mAP)", k=k)

#Fall-Out@k & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.fall_out_at_k, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Fall-Out@k", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Fall-Out@k & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.fall_out_at_k, m.area_under_the_precision_recall_curve_at_k, "Fall-Out@k", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Mean Reciprocal Rank (MMR) & Hit-Rate@k
comparison(m.mean_reciprocal_rank, m.hit_rate_at_k, "Mean Reciprocal Rank (MMR)", "Hit-Rate@k", k=k)

#Mean Reciprocal Rank (MMR) & mean Average Precision@k (mAP)
comparison(m.mean_reciprocal_rank, m.mean_average_precision_at_k, "Mean Reciprocal Rank (MMR)", "mean Average Precision@k (mAP)", k=k)

#Mean Reciprocal Rank (MMR) & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.mean_reciprocal_rank, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Mean Reciprocal Rank (MMR)", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Mean Reciprocal Rank (MMR) & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.mean_reciprocal_rank, m.area_under_the_precision_recall_curve_at_k, "Mean Reciprocal Rank (MMR)", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Hit-Rate@k & mean Average Precision@k (mAP)
comparison(m.hit_rate_at_k, m.mean_average_precision_at_k, "Hit-Rate@k", "mean Average Precision@k (mAP)", k=k)

#Hit-Rate@k & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.hit_rate_at_k, m.area_under_the_curve_receiver_operator_characteristic_at_k, "Hit-Rate@k", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#Hit-Rate@k & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.hit_rate_at_k, m.area_under_the_precision_recall_curve_at_k, "Hit-Rate@k", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#mean Average Precision@k (mAP) & Area Under The Curve - ROC curve@k (AUC-ROC)
comparison(m.mean_average_precision_at_k, m.area_under_the_curve_receiver_operator_characteristic_at_k, "mean Average Precision@k (mAP)", "Area Under The Curve - ROC curve@k (AUC-ROC)", k=k)

#mean Average Precision@k (mAP) & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.mean_average_precision_at_k, m.area_under_the_precision_recall_curve_at_k, "mean Average Precision@k (mAP)", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)



#Area Under The Curve - ROC curve@k (AUC-ROC) & Area Under the Precision-Recall Curve@k (PRAUC)
comparison(m.area_under_the_curve_receiver_operator_characteristic_at_k, m.area_under_the_precision_recall_curve_at_k, "Area Under The Curve - ROC curve@k (AUC-ROC)", "Area Under the Precision-Recall Curve@k (PRAUC)", k=k)