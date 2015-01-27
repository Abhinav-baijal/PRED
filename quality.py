from sklearn import metrics
import data_format
from math import sqrt

def normalized_mutual_information(clustering_a, clustering_b):
    labels_a = data_format.dict_to_list(clustering_a)
    labels_b = data_format.dict_to_list(clustering_b)

    return metrics.cluster.normalized_mutual_info_score(labels_a, labels_b)

def NMI_against_original_data(clustering, original_data):
    return {k: normalized_mutual_information(clustering,v) for k,v in original_data.items()}

def consensus_quality(consensus, original_data):
    return sqrt(metrics.mean_squared_error(list(NMI_against_original_data(consensus, original_data).values()), [1.0]*len(original_data)))