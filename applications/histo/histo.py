# Your code here

def filter_string(s1, s2):
  for c in s2:
    s1 = s1.replace(c, '')
  return s1




with open("robin.txt") as f:
  words = f.read()



# print(words)

filtered_words = filter_string(words, [",", ".", ":", ";", "!", '"', "'", "?", '\n'])