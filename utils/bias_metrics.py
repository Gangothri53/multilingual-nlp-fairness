import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compute_bias(sentences_dict, embeddings_dict):
    # Example: compute pairwise cosine similarity across languages
    langs = list(sentences_dict.keys())
    n = len(langs)
    similarity_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sim = cosine_similarity([embeddings_dict[langs[i]][0]], [embeddings_dict[langs[j]][0]])[0][0]
            similarity_matrix[i,j] = sim
    df = pd.DataFrame(similarity_matrix, index=langs, columns=langs)
    df.to_csv('results/bias_report.csv')
    return df