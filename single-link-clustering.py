import testdata
import coassociation
from sklearn import cluster

agglomerative = cluster.AgglomerativeClustering(n_clusters = 3,
                                                affinity = 'precomputed',
                                                linkage = 'average')

distancematrix = coassociation.dict_to_matrix(coassociation.distance_matrix(testdata.data))
agglomerative.fit(distancematrix)
print(agglomerative.labels_)
