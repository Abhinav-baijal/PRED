import data
import coassociation
import data_format
from sklearn import cluster
import image_utils
import quality

agglomerative = cluster.AgglomerativeClustering(n_clusters = 100,
                                                affinity = 'precomputed',
                                                linkage = 'average')

distancematrix = data_format.dict_to_matrix(coassociation.distance_matrix(data.data))
agglomerative.fit(distancematrix)

result = data_format.labels_as_dictionary(agglomerative.labels_)

def display_cluster(cluster_id):
    image_utils.images_on_grid(image_utils.image_ids_to_paths([image for image,cluster in result.items() if cluster == cluster_id])).show()

def result_quality():
    return quality.consensus_quality(data_format.list_to_dict(agglomerative.labels_), data.data)

def original_clusterings_quality():
    return [quality.consensus_quality(x, data.data) for x in data.data.values()]

def graph_quality():
    import plot
    plot.consensus_quality_bar_chart(result_quality(), original_clusterings_quality())
