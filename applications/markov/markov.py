import random

def check_upper(c):
    if c >= 'A' and c <= 'Z':
        return True
    else:
        return False

def is_end_word(w):
    l = len(w)-1
    if w[l] in [".", "?", "!"] or (w[l] == '"' and w[l-1] in [".", "?", "!"]):
        return True

def is_start_word(w):
    if check_upper(w[0]) or (w[0] == '"' and check_upper(w[1])):
        return True


can_follow = {}
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

start_words = []
end_words = []

list_of_words = words.split()

for index, word in enumerate(list_of_words):
    if (index < len(list_of_words)-1):
        if is_start_word(word):
            start_words.append(word)
        if is_end_word(word):
            end_words.append(word)
        if word in can_follow:
            can_follow[word].append(list_of_words[index+1])
            continue
        else:
            can_follow[word] = [(list_of_words[index+1])]
            continue


    


# print(list_of_words)
# print("Can follow", can_follow)
print("start words", start_words)

random_start = random.choice(start_words)
print("random start:", random_start)
print("X start words", len(start_words))

# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here



