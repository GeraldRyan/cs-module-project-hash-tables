import math

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

order_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z', '', '']
char_counter = {}
total_chars = 0
char_freq = {}
deciphered = ''

with open('ciphertext.txt') as f:
  words = f.read()

for char in words:
  if char in [' ', '?', '!', ';', '(', ')', ',', '.', ':', "-", "â", '€', "1", "'", '"']:
    continue
  if char not in char_counter:
    char_counter[char] = 1
  else:
    char_counter[char] += 1
  total_chars +=1

for char in char_counter:
  char_freq[char] = round(char_counter[char] / total_chars *100,2)


print(len(char_counter))
print("char counter", char_counter)
char_counter_sorted = sorted(char_counter, key=char_counter.__getitem__, reverse=True)
print("char counter sorted", char_counter_sorted)
mapped_chars = {}

for index, char in enumerate(char_counter_sorted):
  mapped_chars[char] = order_freq[index] 
print("mapped chars", mapped_chars)

for char in words:
  if char in [' ', '?', '!', ';', '(', ')', ',', '.', ':', "-", "â", '€', "1", "'", '"']:
    deciphered += char
  else:
    deciphered += mapped_chars[char]


print("Grand Total", total_chars)
print('char frequency', char_freq)

print(deciphered)