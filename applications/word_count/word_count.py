import re
def word_count(s):
    count = {}
    # Your code here
    s = s.lower()
    s = re.sub(r'[^\w\s]','',s)
    l = s.split()
    for w in l:
        if w in count:
            count[w] +=1
        else:
            count[w] = 1


    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))