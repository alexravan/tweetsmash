class BigramLM:
    def __init__(self, unigram_counts, vocabulary = set()):
        self.vocabulary = vocabulary
        self.unigram_counts = unigram_counts
        self.bigram_counts = defaultdict(float)
        self.log_probs = defaultdict(float)
    """ Implement the functions EstimateBigrams, CheckDistribution, Perplexity and any 
    other function you might need here.
    """
    def get_bigram_counts(self, data):
        for sent in data:
            for i in range(1, len(sent)):
                bigram = (sent[i-1], sent[i])
                self.bigram_counts[bigram] += 1

    def estimate_bigrams(self):
        for bigram, count in self.bigram_counts.iteritems():
            self.log_probs[bigram] = log(count/self.unigram_counts[bigram[0]])

def preprocessText(data, vocabulary, unigram_counts):
    processed_text = []

    for sent in data:
        sent.insert(0, START_TOKEN)
        sent.append(END_TOKEN)
        processed_text.append(sent)
        for word in sent:
            unigram_counts[word] += 1

    # adds only words that appear more than once to vocabulary set
    for word in unigram_counts:
        if unigram_counts[word] > 1:
            vocabulary.add(word)

    for sent in processed_text:
        for i in range(len(sent)):
            if sent[i] not in vocabulary:
                sent[i] = UNKNOWN_TOKEN
                unigram_counts[UNKNOWN_TOKEN] += 1
    return processed_text

def main():
    tweets = 
    vocabulary = set()
    unigram_counts = defaultdict(float)

    processed_text = preprocessText(tweets, vocabulary, unigram_counts)

    bML = BigramLM(unigram_counts, vocabulary)
    bML.get_bigram_counts(training_set_prep)
    bML.estimate_bigrams()

