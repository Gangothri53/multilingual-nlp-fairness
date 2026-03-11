from utils.preprocessing import preprocess_sentences
from utils.embeddings import get_embeddings
from utils.bias_metrics import compute_bias
from utils.visualization import plot_similarity_heatmap
import pandas as pd
from config import LANGUAGES, DATA_FOLDER, RESULTS_FOLDER

all_sentences = {}

for lang in LANGUAGES:
    df = pd.read_csv(f'{DATA_FOLDER}/{lang.lower()}_sentences.csv')
    all_sentences[lang] = preprocess_sentences(df['sentence'].tolist())

embeddings = get_embeddings(all_sentences)
bias_report = compute_bias(all_sentences, embeddings)
plot_similarity_heatmap(embeddings, RESULTS_FOLDER)
print('Analysis complete! Check the results folder.')