import random

class Higher_Order_Markov_Chain:
    def __init__(self, corpus_file):
        self.corpus = self._read_corpus(corpus_file)
        self.chain = self._build_chain(self.corpus)
        self.historgram = self._generate_histogram(corpus_file)
        
    def _read_corpus(self, corpus_file):
        with open(corpus_file, 'r') as file:
            corpus = file.read()
        return corpus.split()

    def _generate_histogram(self, corpus_file):
        words = self.corpus
        histogram = {}
        for word in words:
            histogram[word] = histogram.get(word, 0) + 1

        return histogram

    def _build_chain(self, corpus):
        chain = {}
        for i in range(len(corpus)-1):
            current_word = corpus[i]
            next_word = corpus[i+1]
            if current_word in chain:
                chain[current_word].append(next_word)
            else:
                chain[current_word] = [next_word]

        return chain
    
    def generate_sentence(self):
        current_word = random.choice(list(self.chain.keys()))
        random_words = []
        
        for _ in range(random.randint(5, 30)):
            random_words.append(current_word)
            next_word_options = self.chain.get(current_word, [])
            if next_word_options:
                current_word = random.choice(next_word_options)
            else:
                break
        
        sentence = " ".join(random_words)
        sentence = sentence.capitalize() + '.'
        return sentence


corpus_file = 'Code/data/corpus.txt'  # Path to your corpus file
generator = Higher_Order_Markov_Chain(corpus_file)
sentence = generator.generate_sentence()
print(sentence)

