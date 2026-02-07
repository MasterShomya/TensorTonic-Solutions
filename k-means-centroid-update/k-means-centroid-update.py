def k_means_centroid_update(points, assignments, k):
    # number of dimensions
    dim = len(points[0])

    # create empty clusters
    clusters = [[] for _ in range(k)]
    
    # group points
    for point, cid in zip(points, assignments):
        clusters[cid].append(point)

    centroids = []

    for cluster in clusters:
        # empty cluster case
        if len(cluster) == 0:
            centroids.append([0.0] * dim)
            continue

        centroid = []
        for d in range(dim):
            mean_d = sum(p[d] for p in cluster) / len(cluster)
            centroid.append(float(mean_d))

        centroids.append(centroid)

    return centroids
