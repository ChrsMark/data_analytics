import numpy as np
from sklearn.neighbors import NearestNeighbors


X = np.array([[37.776181, -122.413414], [39.19198813, -122.937563],
              [39.776181, -122.413414], [30.19198813, -118.937563]])

 # k = 3
nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(X)

distances, indices = nbrs.kneighbors(X)

print(distances[0])
print(indices[0])

# now take the max value of first array itm

