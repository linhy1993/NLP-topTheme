import nltk
import gensim
import word2vector

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

def kmeans_method(number_means, word_vec, words_list):
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

    for w in words_list:
        temp = result[km.classify(model.wv[w])]
        temp.append(w)

    return result

if __name__ == '__main__':

    word_list = ['X', 'team', 'collaborative', 'They', 'receive', 'requests', 'many', 'departments', 'CDPQ', 'still', 'tackle', 'professionally', 'mostly', 'time', 'X', 'particular', 'detailed', 'oriented', 'work', 'produced', 'team', 'high', 'standard', 'X', 'model', 'many', 'aspects', 'totally', 'genuine', 'generosity', 'knowledge', 'passionate', 'understanding', 'sensitive', 'easy', 'talk', 'open', 'mind', 'just', 'name', 'X', 'truly', 'cares', 'professional', 'development', 'satisfaction', 'supervision', 'This', 'resonates', 'work', 'team', 'individual', 'member', 'takes', 'pride', 'projects', 'feeling', 'sense', 'ownership', 'work', 'He', 'keeps', 'team', 'informed', 'aspects', 'work', 'including', 'purpose', 'goals', 'vision', 'recipients', 'member', 'able', 'comprehend', 'scope', 'work', 'envision', 'final', 'product', 'strive', 'produce', 'In', 'many', 'projects', 'discussing', 'vision', 'gives', 'team', 'members', 'independence', 'execute', 'allowing', 'display', 'creativity', 'skillsets', 'constantly', 'keeping', 'team', 'aware', 'underlying', 'goal', 'project', 'stays', 'focus', 'He', 'open', 'suggestions', 'edits', 'always', 'interested', 'hear', 'thoughts', 'concerns', 'team', 'member', 'He', 'proactive', 'anticipating', 'work', 'will', 'useful', 'collaborators', 'throughout', 'CDPQ', 'X', 'fair', 'pushes', 'team', 'meet', 'sometimes', 'stressful', 'deadlines', 'often', 'shoulders', 'longest', 'hours', 'demand', 'anything', 'wouldn', 't', 'demand', 'Even', 'workload', 'high', 'always', 'friendly', 'positive', 'makes', 'people', 'feel', 'valued', 'special', 'offering', 'praise', 'always', 'remembering', 'birthdays', 'important', 'personal']
    word_vec = word2vector.word2vector(word_list)
    result = kmeans_method(4, word_vec, word_list)
    print(result)