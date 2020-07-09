# Your code here

def filter_string(s1, s2):
  for c in s2:
    s1 = s1.replace(c, '')
  return s1


word_counter = {}

with open("robin.txt") as f:
  words = f.read()


filtered_words = filter_string(words, [",", ".", ":", ";", "!", '"', "'", "?", '\n'])
split_filtered_words = split(filtered_words)
print(split_filtered_words)