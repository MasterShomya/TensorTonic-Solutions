import numpy as np
def k_means_assignment(points, centroids):
    output = []
    for point in points:
        distances = []
        for centroid in centroids:
            dist = 0
            for d in range(len(point)):
                dist+=((point[d]-centroid[d])**2)
            distances.append(dist)
        cluster_id = int(np.argmin(distances))
        output.append(cluster_id)

    return output

            
