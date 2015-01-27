import data
import coassociation
import data_format
from sklearn import cluster
import image_utils
import quality

from distance_matrix import distance_matrix
#distancematrix = data_format.dict_to_matrix(coassociation.distance_matrix(data.data))

def agglomerative_clustering(clusters, linkage_type):
    agglomerative = cluster.AgglomerativeClustering(n_clusters = clusters,
                                                    affinity = 'precomputed',
                                                    linkage = linkage_type)

    agglomerative.fit(distance_matrix)

    return data_format.list_to_dict(agglomerative.labels_.copy())

results = {
    'average_10' : agglomerative_clustering(10,'average'),
    'average_50' : agglomerative_clustering(50,'average'),
    'average_100' : agglomerative_clustering(100,'average'),

    'complete_10' : agglomerative_clustering(10,'complete'),
    'complete_50' : agglomerative_clustering(50,'complete'),
    'complete_100' : agglomerative_clustering(100,'complete')
}

def display_cluster(result, cluster_id):
    image_utils.images_on_grid(image_utils.image_ids_to_paths(result[cluster_id])).show()

def result_quality(result):
    return quality.consensus_quality(result, data.data)

#def original_clusterings_quality():
#    return [quality.consensus_quality(x, data.data) for x in data.data.values()]
def original_clusterings_quality():
    from quality_values import quality_values
    return quality_values

def graph_quality(result):
    import plot
    plot.consensus_quality_bar_chart(result_quality(result), original_clusterings_quality())
