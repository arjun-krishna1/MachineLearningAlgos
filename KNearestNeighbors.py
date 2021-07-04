import heapq
import math


def get_dist(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i]) ** 2
    return math.sqrt(res)


def get_positive_neighbors(neighbor_keys, examples):
    res = 0
    for key in neighbor_keys:
        res += examples[key]["is_intrusive"]
    return res


# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    neighbor_keys = find_k_nearest_neighbors(examples, features, k)
    neighbor_labels = [examples[pid][label_key] for pid in neighbor_keys]
    return round(sum(neighbor_labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    res = []
    heapq.heapify(res)

    for i in examples.keys():
        point = examples[i]
        dist = get_dist(features, point["features"])
        heapq.heappush(res, (dist, i))

    neighbors = list(heapq.nsmallest(k, res))
    neighbor_keys = [i[1] for i in neighbors]
    return neighbor_keys
