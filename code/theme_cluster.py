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
from func import language_regonize
from repo import insert

version = 0.2
IF_DEBUG = True

def kmeans(number_means, matrix, word_list, get_word_vec):
    if IF_DEBUG:
        print("[INFO] start doing Kmeans clustering...")
    # print(len(matrix))
    # print('#########2D########')
    pca = PCA(n_components=2)
    reduce_word_vec = pca.fit_transform(matrix)

    reduce_word_vec_lst = {}
    map_vec = list(get_word_vec.keys())

    for i in range(0, len(matrix) - 1):
        temp_vec = reduce_word_vec[i]
        temp_token = map_vec[i]
        reduce_word_vec_lst[temp_token] = temp_vec

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
    for i in K:
        input_cluster_analysis = {"_id": "K value is  "+str(i) }
        input_cluster_analysis["elbow value"] = meandistortions[i - 3]
        input_cluster_analysis["sc scores"] = sc_scores[i - 3]
        insert("cluster_analysis", input_cluster_analysis)

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

    # plt.show()

    result = []
    nearest_word = []
    for i in range(0, bestK):
        temp = []
        result.append(temp)
        nearest_word.append(temp)

    for i in range(0, len(matrix) - 1):
        index_word = (km_2d.labels_)[i]
        result[index_word].append(word_list[i])
    # print(result)
    # for i in range(0, bestK):
    #     print(km_2d.cluster_centers_[i])


    for i in range(0, bestK):
        tempValue = 100
        for w in result[i]:
            distance = calculate_distance(reduce_word_vec_lst.get(w), km_2d.cluster_centers_[i])
            if distance < tempValue:
                tempValue = distance
                nearest_word[i] = w
            else:
                tempValue = tempValue

    return_data = {}
    return_data['clusters'] = result
    return_data['centers'] = km_2d.cluster_centers_
    return_data['representative'] = nearest_word

    ########save theme#######
    for i in range(0, bestK):
        input_theme = {"_id": "theme"+str(i) }
        input_theme["themes"] = nearest_word[i]
        input_theme["tokens"] = result[i]
        insert("themes",input_theme)

    return return_data

def calculate_distance(word1, word2):
    distance = np.sqrt(np.sum(np.square(word1 - word2)))
    return distance


