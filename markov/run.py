import markov

file_ = open('dream.txt')
# file_ = open('alice.txt')
# file_ = open('test.txt')

text = markov.Markov(file_)
print text.generate_markov_text()
