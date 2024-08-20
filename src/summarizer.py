from text_processor import TextProcessor
from algorithms import SummarizationAlgorithms

class Summarizer:
    def __init__(self):
        self.processor = TextProcessor()

    def summarize(self, text, num_sentences=3):
        original_sentences, processed_sentences = self.processor.preprocess(text)
        
        # Compute TF-IDF
        tfidf_matrix = SummarizationAlgorithms.compute_tf_idf(processed_sentences)
        
        # Build similarity matrix
        similarity_matrix = SummarizationAlgorithms.build_similarity_matrix(tfidf_matrix)
        
        # Rank sentences
        scores = SummarizationAlgorithms.rank_sentences(similarity_matrix)
        
        # Select top-ranked sentences
        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(original_sentences)), reverse=True)
        summary = ' '.join([sentence for _, sentence in ranked_sentences[:num_sentences]])
        
        return summary
