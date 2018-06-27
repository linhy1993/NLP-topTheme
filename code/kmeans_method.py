import nltk
import word2vector
from data import str_of

def kmeans(number_means, word_vec, word_vec_map):
    """
    input:  number of clusters
            word vector
            original word list
    :param number_means:
    :type  int
    :param word_vec:
    :return:
    """
    km = nltk.cluster.KMeansClusterer(num_means=number_means, distance=nltk.cluster.util.euclidean_distance)
    assigned_clusters = km.cluster(word_vec)

    result = []

    for i in range(0, number_means):
        temp = []
        result.append(temp)

    words_list = list(word_vec_map.keys())
    for w in words_list:
        temp = result[km.classify(word_vec_map.get(w))]
        temp.append(w)

    return_val = {}
    return_val['clustered'] = result
    return_val['centers'] = km.means()

    return return_val

if __name__ == '__main__':
    word_list = ['team','collaborative', 'they', 'receive', 'requests', 'many', 'departments', 'CDPQ', 'still', 'tackle', 'professionally', 'mostly', 'time', 'particular', 'detailed', 'oriented', 'work']
    word_vec = word2vector.word2vector(word_list)
    result = kmeans(4, word_vec, word_list)
    print(result)
