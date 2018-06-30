import nltk
import word2vector
from data import str_of

IF_DEBUG = True

def kmeans_em(num_cluster, word_matrix, word_vec_map):
    kmeans_clustered = kmeans(num_cluster, word_matrix, word_vec_map)
    if IF_DEBUG:
        result_kmeans = kmeas_clustered.get('clusters')
        print("[INFO]------ Result of Kmeans -------")
        for r in result_kmeans:
            print(r)
            print('\n')
        print("-------------------------------------")

    centers = kmeans_clustered.get("centers")

    em_clustered = em_cluster(centers, word_matrix, word_vec_map)

    return em_clustered


def kmeans(number_means, matrix, word_vec_map):
    if IF_DEBUG:
        print("[INFO] start doing Kmeans clustering")
    km = nltk.cluster.KMeansClusterer(num_means=number_means, distance=nltk.cluster.util.euclidean_distance)
    km.cluster(matrix)

    result = []

    for i in range(0, number_means):
        temp = []
        result.append(temp)

    words_list = list(word_vec_map.keys())
    for w in words_list:
        temp = result[km.classify(word_vec_map.get(w))]
        temp.append(w)

    return_data = {}
    return_data['clusters'] = result
    return_data['centers'] = km.means()
    return return_data


def em_cluster(centers, matrix, word_vec_map):
    if IF_DEBUG:
        print("[INFO] start doing EM clustering")
    em = nltk.cluster.EMClusterer(initial_means = centers, bias=0.1)
    em.cluster(matrix)

    result = []
    num_cluster = len(centers)
    for i in range(0, num_cluster):
        temp = []
        result.append(temp)

    words_list = list(word_vec_map.keys())
    for w in words_list:
        temp = result[em.classify(word_vec_map.get(w))]
        temp.append(w)
    return result
