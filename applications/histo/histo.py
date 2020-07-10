# Your code here

def filter_string(s1, s2):
  for c in s2:
    s1 = s1.replace(c, '')
  return s1

def sort_dict(dic):
  return {k: v for k, v in sorted(dic.items(), key=lambda item: (-item[1], item))}



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

word_counter_sorted = sort_dict(word_counter)
print(word_counter_sorted)