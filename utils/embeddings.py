from sentence_transformers import SentenceTransformer

def get_embeddings(sentences_dict):
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    embeddings = {}
    for lang, sents in sentences_dict.items():
        embeddings[lang] = model.encode(sents)
    return embeddings