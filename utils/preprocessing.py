def preprocess_sentences(sentences):
    # Basic preprocessing: lowercasing and stripping
    return [s.lower().strip() for s in sentences]