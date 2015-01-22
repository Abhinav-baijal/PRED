import images
import data
import coassociation
import data_format
from sklearn import cluster
import image_utils

agglomerative = cluster.AgglomerativeClustering(n_clusters = 100,
                                                affinity = 'precomputed',
                                                linkage = 'average')

distancematrix = data_format.dict_to_matrix(coassociation.distance_matrix(data.data))
agglomerative.fit(distancematrix)

result = data_format.labels_as_dictionary(agglomerative.labels_)

def display_cluster(cluster_id):
    image_utils.images_on_grid(image_utils.image_ids_to_paths([image for image,cluster in result.items() if cluster == cluster_id])).show()
