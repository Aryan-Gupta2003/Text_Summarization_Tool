import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import networkx as nx

class SummarizationAlgorithms:
    
    @staticmethod
    def compute_tf_idf(sentences):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(sentences)
        return X.toarray()

    @staticmethod
    def build_similarity_matrix(tfidf_matrix):
        similarity_matrix = np.dot(tfidf_matrix, tfidf_matrix.T)
        return similarity_matrix
    
    @staticmethod
    def rank_sentences(similarity_matrix):
        graph = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(graph)
        return scores
