import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_similarity_heatmap(embeddings_dict, results_folder):
    langs = list(embeddings_dict.keys())
    sim_matrix = pd.read_csv(f'{results_folder}/bias_report.csv', index_col=0)
    plt.figure(figsize=(8,6))
    sns.heatmap(sim_matrix, annot=True, cmap='coolwarm')
    plt.title('Multilingual Sentence Similarity Heatmap')
    plt.savefig(f'{results_folder}/similarity_matrix.png')