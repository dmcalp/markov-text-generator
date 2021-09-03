from collections import defaultdict
import random

with open('YOUR_TEXT_FILE.txt', encoding='utf8') as txt:
    script = txt.read()

def create_tf_matrix(text):
  
  words = text.split(" ")

  tf_matrix = defaultdict(list)
  succeeding_words = zip(words[0:-1], words[1:])

  for w1, w2 in succeeding_words:
    tf_matrix[w1].append(w2)

  tf_matrix = dict(tf_matrix)
  return tf_matrix


def generate_sentence(matrix, word_limit=10):
  current_word = random.choice(list(matrix.keys()))
  sentence = current_word.capitalize()

  for i in range(word_limit-1):
    next_word = random.choice(matrix[current_word])
    sentence += ' ' + next_word
    if next_word.endswith('.'):
      return sentence
    current_word = next_word
  
  sentence += '.'
  return sentence
  

matrix = create_tf_matrix(script)
print(generate_sentence(matrix, 20))