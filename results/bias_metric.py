import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def compute_bias(sentences_dict, embeddings_dict):
    langs = list(sentences_dict.keys())
    n = len(langs)
    similarity_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            # Compute average similarity across all sentence pairs
            sims = cosine_similarity(embeddings_dict[langs[i]], embeddings_dict[langs[j]])
            similarity_matrix[i, j] = sims.mean()

    df = pd.DataFrame(similarity_matrix, index=langs, columns=langs)
    df.to_csv('results/bias_report.csv')
    return df