def histogram(source_text):
    histogram = {}
    with open(source_text, 'r') as file:
        word_data = file.read().split(' ')
        for word in word_data:
            word = word.strip()
            if word in histogram.keys():
                 histogram[word] += 1
            else:
                histogram[word] = 1
    return histogram

def unique_words(histogram):
    return len(histogram.keys())

def frequency(histogram, word):
    return histogram.get(word, 0)

sample_words = histogram('Code/histogram.txt')
print(sample_words)
number_unique_words = unique_words(sample_words)
print(f"Number of unique words: {number_unique_words}")
word = 'gently'
frequency = frequency(sample_words, 'gently')
print(f"Gently appear {frequency} times")
