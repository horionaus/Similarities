import gensim
import sys

from gensim.models import Word2Vec

model = Word2Vec.load("ModelTrained")
results = str(model.wv.similarity(w1=str(sys.argv[1]), w2=str(sys.argv[2])))
print("Similarity score: " + results)

