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
    ###################存进数据库#####################
    plt.figure(1)
    km_2d = KMeans(n_clusters= bestK, algorithm="full").fit(reduce_word_vec)
    y_kmeans = km_2d.predict(reduce_word_vec)
    plt.scatter(reduce_word_vec[:,0], reduce_word_vec[:,1], c=y_kmeans,cmap='rainbow')
    ###################存进数据库#####################

    plt.figure(2)
    plt.plot(K, meandistortions, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distotion')
    plt.title('The Elobow Method showing the optimal k')
    ###################存进数据库#####################

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
