import data as testdata
import images
import coassociation
import constraints
from sklearn import cluster
import image_utils

agglomerative = cluster.AgglomerativeClustering(n_clusters = 100,
                                                affinity = 'precomputed',
                                                linkage = 'average')

distancematrix = coassociation.dict_to_matrix(coassociation.distance_matrix(testdata.data))

for i in constraints.constraints_together:
    coassociation.constrain_together(distancematrix,i[0],i[1])


for i in constraints.constraints_apart:
    coassociation.constrain_apart(distancematrix,i[0],i[1])

    
agglomerative.fit(distancematrix)

result = dict(zip(images.imageids, agglomerative.labels_))

def display_cluster(cluster_id):
    image_utils.images_on_grid(image_utils.image_ids_to_paths([image for image,cluster in result.items() if cluster == cluster_id])).show()
    

