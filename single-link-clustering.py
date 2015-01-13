import testdata
from sklearn import cluster

agglomerative = cluster.AgglomerativeClustering(n_clusters = 3,
                                                affinity = 'precomputed',
                                                linkage = 'average')

agglomerative.fit(testdata.distancematrix)
print(agglomerative.labels_)
