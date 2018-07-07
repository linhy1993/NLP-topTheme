import nltk
import word2vector
from data import str_of
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
import numpy as np
from sklearn.decomposition import PCA



IF_DEBUG = True
#
# def kmeans_em(num_cluster, word_matrix, word_vec_map):
#     kmeans_clustered = kmeans(num_cluster, word_matrix, word_vec_map)
#     if IF_DEBUG:
#         result_kmeans = kmeans_clustered.get('clusters')
#         print("[INFO]------ Result of Kmeans -------")
#         for r in result_kmeans:
#             print(r)
#             print('\n')
#         print("-------------------------------------")
#
#     centers = kmeans_clustered.get("centers")
#
#     # em_clustered = em_cluster(centers, word_matrix, word_vec_map)
#
#     return result_kmeans


def kmeans(number_means, matrix, word_list):
    if IF_DEBUG:
        print("[INFO] start doing Kmeans clustering...")
    km = nltk.cluster.KMeansClusterer(num_means=number_means, distance=nltk.cluster.util.euclidean_distance)
    km.cluster(matrix)
    result = []
    print('#########2D########')
    pca = PCA(n_components=2)
    reduce_word_vec = pca.fit_transform(matrix)
    # print(reduce_word_vec)

    K = range(3, number_means)
    meandistortions = []
    sc_scores = []
    reduce_word_vec = np.array(reduce_word_vec).reshape(len(reduce_word_vec),2)
    for k in K:
        kmeans_sk = KMeans(n_clusters=k).fit(reduce_word_vec)
        sc_score = silhouette_score(reduce_word_vec,kmeans_sk.labels_,metric='euclidean')
        meandistortions.append(sum(np.min(cdist(reduce_word_vec, kmeans_sk.cluster_centers_, 'euclidean'), axis=1)) / reduce_word_vec.shape[0])
        sc_scores.append(sc_score)

    bestK = np.argmax(sc_scores) + 3
    # print(bestK)

    plt.figure(1)
    km_2d = KMeans(n_clusters= bestK, algorithm="full").fit(reduce_word_vec)
    y_kmeans = km_2d.predict(reduce_word_vec)
    plt.scatter(reduce_word_vec[:,0], reduce_word_vec[:,1], c=y_kmeans,cmap='rainbow')

    plt.figure(2)
    plt.plot(K, meandistortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distotion')
    plt.title('The Elobow Method showing the optimal k')

    plt.figure(3)
    plt.plot(K, sc_scores, '*-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Coefficient Score')

    plt.show()

    result = []
    for i in range(0, bestK):
        temp = []
        result.append(temp)

    for i in range(0, len(matrix) - 1):
        index_word = (km_2d.labels_)[i]
        result[index_word].append(word_list[i])
    print(result)

    return_data = {}
    return_data['clusters'] = result
    return_data['centers'] = km_2d.cluster_centers_
    print(return_data)
    return return_data

    # for i in range(0, number_means):
    #     temp = []
    #     result.append(temp)
    #
    # words_list = list(word_vec_map.keys())
    # for w in words_list:
    #     temp = result[km.classify(word_vec_map.get(w))]
    #     temp.append(w)
    #
    # return_data = {}
    # return_data['clusters'] = result
    # return_data['centers'] = km.means()
    # return return_data

    # K = range(2, number_means)
    # meandistortions = []
    # sc_scores = []
    # matrix = np.array(matrix)
    # for k in K:
    #     kmeans_sk = KMeans(n_clusters=k, n_init=10).fit(matrix)
    #     # meandistortions.append(kmeans_sk.inertia_)
    #     sc_score = silhouette_score(matrix,kmeans_sk.labels_,metric='euclidean')
    #     meandistortions.append(sum(np.min(cdist(matrix, kmeans_sk.cluster_centers_, 'euclidean'), axis=1)) / matrix.shape[0])
    #     sc_scores.append(sc_score)
    #
    # plt.figure(1)
    # plt.plot(K, meandistortions, 'b-')
    # plt.xlabel('k')
    #
    # plt.figure(2)
    # plt.plot(K, sc_scores, '*-')
    # plt.xlabel('Number of Clusters')
    # plt.ylabel('Silhouette Coefficient Score')
    #
    # plt.show()

    # result = []
    # for i in range(0, number_means):
    #     temp = []
    #     result.append(temp)
    #
    # for i in range(0, len(matrix) - 1):
    #     index_word = (kmeans_sk.labels_)[i]
    #     print(index_word)
    #     result[index_word].append(word_list[i])
    # print(result)
    # return sc_score


# def em_cluster(centers, matrix, word_vec_map):
#     if IF_DEBUG:
#         print("[INFO] start doing EM clustering...")
#     em = nltk.cluster.EMClusterer(initial_means = centers, bias=0.1)
#     em.cluster(matrix)
#
#     result = []
#     num_cluster = len(centers)
#     for i in range(0, num_cluster):
#         temp = []
#         result.append(temp)
#
#     words_list = list(word_vec_map.keys())
#     for w in words_list:
#         temp = result[em.classify(word_vec_map.get(w))]
#         temp.append(w)
#     return result
