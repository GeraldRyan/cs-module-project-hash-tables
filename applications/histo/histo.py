# Your code here

def filter_string(s1, s2):
  for c in s2:
    s1 = s1.replace(c, '')
  return s1


word_counter = {}

with open("robin.txt") as f:
  words = f.read().lower()


filtered_words = filter_string(words, [",", ".", ":", ";", "!", '"', "'", "?"])
split_filtered_words = filtered_words.split()
# print(split_filtered_words)

for word in split_filtered_words:
  if word in word_counter:
    word_counter[word] +=1
  else:
    word_counter[word] = 1

print(word_counter)