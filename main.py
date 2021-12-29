import numpy as np
import measures as m

#Initialize Arrays
arr_length = 20
k = int(arr_length/3)

S = np.arange(1, arr_length + 1)
R1 = np.arange(1, arr_length + 1)
R2 = np.arange(1, arr_length + 1)

#Loop with different measures
def comparison(measure1, measure2, string1, string2):
    i = 0
    while True:
        np.random.shuffle(R1)
        np.random.shuffle(R2)

        m1 = measure1(S, R1, R2)
        m2 = measure2(S, R1, R2)

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

def comparison_at_k(measure1, measure2, string1, string2, k):
    i = 0
    while True:
        np.random.shuffle(R1)
        np.random.shuffle(R2)

        m1 = measure1(S, R1, R2)
        m2 = measure2(S, R1, R2, k)

        if ((m1[0] < m1[1]) and (m2[0] > m2[1]) or (m1[0] > m1[1]) and (m2[0] < m2[1])):
            print("\n", "S:" + str(S))
            print("R1:" + str(R1[:k]))
            print("R2:" + str(R2[:k]), "\n")
            print(string1)
            print(m1[0], m1[1], "\n")
            print(string2)
            print(m2[0], m2[1])
            break

        #if(i==1000):
        #    break

        #print("Iteration: ", i)
        i = i + 1

#Kendall rank correlation coefficient & Spearman's rank correlation coefficient
comparison(m.kendall_rank_correlation, m.spearmans_rank_correlation_coefficient, "Kendall rank correlation coefficient", "Spearman's rank correlation coefficient")

#Kendall rank correlation coefficient & Discounted Cumulative Gain
comparison(m.kendall_rank_correlation, m.dicscounted_cumulative_gain, "Kendall rank correlation coefficient", "Discounted Cumulative Gain")

#Kendall rank correlation coefficient & Nromalized Discounted Cumulative Gain
comparison(m.kendall_rank_correlation, m.normalized_dicscounted_cumulative_gain, "Kendall rank correlation coefficient", "Normalized Discounted Cumulative Gain")

#Kendall rank correlation coefficient & Precision
comparison(m.kendall_rank_correlation, m.precision, "Kendall rank correlation coefficient", "Precision")

#Kendall rank correlation coefficient & Precision@k
comparison_at_k(m.kendall_rank_correlation, m.precision_at_k, "Kendall rank correlation coefficient", "Precision", k)

#Kendall rank correlation coefficient & Recall
comparison(m.kendall_rank_correlation, m.recall, "Kendall rank correlation coefficient", "Recall")

#Kendall rank correlation coefficient & F1 Score
comparison(m.kendall_rank_correlation, m.f1_score, "Kendall rank correlation coefficient", "F1 Score")



#Spearman's rank correlation coefficient & Discounted Cumulative Gain
comparison(m.spearmans_rank_correlation_coefficient, m.dicscounted_cumulative_gain, "Spearman's rank correlation coefficient", "Discounted Cumulative Gain")

#Spearman's rank correlation coefficient & Normalized Discounted Cumulative Gain
comparison(m.spearmans_rank_correlation_coefficient, m.normalized_dicscounted_cumulative_gain, "Spearman's rank correlation coefficient", "Normalized Discounted Cumulative Gain")

#Spearman's rank correlation coefficient & Precision
comparison(m.spearmans_rank_correlation_coefficient, m.precision, "Spearman's rank correlation coefficient", "Precision")

#Spearman's rank correlation coefficient & Precision@k
comparison_at_k(m.spearmans_rank_correlation_coefficient, m.precision_at_k, "Spearman's rank correlation coefficient", "Precision@k", k )

#Spearman's rank correlation coefficient & Recall
comparison(m.spearmans_rank_correlation_coefficient, m.recall, "Spearman's rank correlation coefficient", "Recall")

#Spearman's rank correlation coefficient & F1 Score
comparison(m.spearmans_rank_correlation_coefficient, m.f1_score, "Spearman's rank correlation coefficient", "F1 Score")



#Discounted Cumulative Gain & Normalized Discounted Cumulative Gain
#comparison(m.dicscounted_cumulative_gain, m.normalized_dicscounted_cumulative_gain, "Discounted Cumulative Gain", "Normalized Discounted Cumulative Gain")

#Discounted Cumulative Gain & Precision
comparison(m.dicscounted_cumulative_gain, m.precision, "Discounted Cumulative Gain", "Precision")

#Discounted Cumulative Gain & Precision@k
comparison_at_k(m.dicscounted_cumulative_gain, m.precision_at_k, "Discounted Cumulative Gain", "Precision@k", k )

#Discounted Cumulative Gain & Recall
comparison(m.dicscounted_cumulative_gain, m.recall, "Discounted Cumulative Gain", "Recall")

#Discounted Cumulative Gain & F1 Score
comparison(m.dicscounted_cumulative_gain, m.f1_score, "Discounted Cumulative Gain", "F1 Score")



#Normalized Discounted Cumulative Gain & Precision
comparison(m.normalized_dicscounted_cumulative_gain, m.precision, "Normalized Discounted Cumulative Gain", "Precision")

#Normalized Discounted Cumulative Gain & Precision@k
comparison_at_k(m.normalized_dicscounted_cumulative_gain, m.precision_at_k, "Normalized Discounted Cumulative Gain", "Precision@k", k )

#Normalized Discounted Cumulative Gain & Recall
comparison(m.normalized_dicscounted_cumulative_gain, m.recall, "Normalized Discounted Cumulative Gain", "Recall")

#Normalized Discounted Cumulative Gain & F1 Score
comparison(m.normalized_dicscounted_cumulative_gain, m.f1_score, "Normalized Discounted Cumulative Gain", "F1 Score")



#Precision & Precision@k
comparison_at_k(m.precision, m.precision_at_k, "Precision", "Precision@k", k )

#Precision & Recall
comparison(m.precision, m.recall, "Precision", "Precision@k")

#Precision & F1 Score
comparison(m.precision, m.f1_score, "Precision", "F1 Score")



#Precision@k & Recall
comparison_at_k(m.recall, m.precision_at_k, "Precision@k", "Recall", k )

#Precision@k & F1 Score
comparison_at_k(m.f1_score, m.precision_at_k, "Precision@k", "F1 Score", k )



#Recall & F1 Score
comparison(m.recall, m.f1_score, "Recall", "F1 Score")


