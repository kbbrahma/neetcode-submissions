def get_longer_word(word1: str, word2: str) -> str:
    l1 = len(word1)
    l2 = len(word2)
    maxx = l1
    if l1>=l2:
        maxx = word1
    else:
        maxx = word2    
    return maxx    



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
