def no_dups(s):
    # Your code here

    # I think this is very bad code but it's working nonetheless. 
    duplicate_tracker = {}

    listify = s.split()
    final_list = []
    for word in listify:
        if word in duplicate_tracker:
            next 
        else:
            final_list.append(word)
            duplicate_tracker[word] = word

    
    string = " ".join(final_list)


    return string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))