import nltk



from nltk.corpus import udhr



# text = nltk.corpus.genesis.words('english-kjv.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)

# print (cfd['with'].plot)

# print(generate_model(cfd, 'with'))

# puzzle_letters = nltk.FreqDist('egivrvonl')
# obligator = 'r'
# wordlist = nltk.corpus.words.words()
# print([w for w in wordlist if len(w)>=4 and obligator in w and nltk.FreqDist(w) <=puzzle_letters])

from nltk.corpus import wordnet as wn
print(wn.synsets('house'))
print(wn.synset('firm.n.01').examples())