import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

def word2vector(words_list):
    """
    input a list of words and obatin the vector of each word
    :param words_list: 
    :type list
    :return: word's vector
    :type list
    """
    word_vec = []
    for word in words_list:
        word_vec.append(model.wv[word])
    return word_vec

# if __name__ == '__main__':
#     words_list = ['X', 'team', 'collaborative', 'They', 'receive', 'requests', 'many', 'departments', 'CDPQ', 'still', 'tackle', 'professionally', 'mostly', 'time', 'X', 'particular', 'detailed', 'oriented', 'work', 'produced', 'team', 'high', 'standard', 'X', 'model', 'many', 'aspects', 'totally', 'genuine', 'generosity', 'knowledge', 'passionate', 'understanding', 'sensitive', 'easy', 'talk', 'open', 'mind', 'just', 'name', 'X', 'truly', 'cares', 'professional', 'development', 'satisfaction', 'supervision', 'This', 'resonates', 'work', 'team', 'individual', 'member', 'takes', 'pride', 'projects', 'feeling', 'sense', 'ownership', 'work', 'He', 'keeps', 'team', 'informed', 'aspects', 'work', 'including', 'purpose', 'goals', 'vision', 'recipients', 'member', 'able', 'comprehend', 'scope', 'work', 'envision', 'final', 'product', 'strive', 'produce', 'In', 'many', 'projects', 'discussing', 'vision', 'gives', 'team', 'members', 'independence', 'execute', 'allowing', 'display', 'creativity', 'skillsets', 'constantly', 'keeping', 'team', 'aware', 'underlying', 'goal', 'project', 'stays', 'focus', 'He', 'open', 'suggestions', 'edits', 'always', 'interested', 'hear', 'thoughts', 'concerns', 'team', 'member', 'He', 'proactive', 'anticipating', 'work', 'will', 'useful', 'collaborators', 'throughout', 'CDPQ', 'X', 'fair', 'pushes', 'team', 'meet', 'sometimes', 'stressful', 'deadlines', 'often', 'shoulders', 'longest', 'hours', 'demand', 'anything', 'wouldn', 't', 'demand', 'Even', 'workload', 'high', 'always', 'friendly', 'positive', 'makes', 'people', 'feel', 'valued', 'special', 'offering', 'praise', 'always', 'remembering', 'birthdays', 'important', 'personal']
#     vector = word2vector(words_list)
#     print(vector)