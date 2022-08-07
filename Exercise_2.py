def annograms(word):
    """
    This function uses a WORD.LST file to return anagrams of the word given by parameter.

    Parameters:

    word = str
    """
    words = [w.rstrip() for w in open('WORD.LST')]
    anagram = ""

    for i in words:
        word_lst = list(i)

        for char in word:
            if char in word_lst:
                word_lst.remove(char)

        if len(word_lst) == 0 and (len(i) == len(word)):
            anagram = i
            break
            
    return anagram
            

if __name__ == "__main__":

    print(annograms("train"))
    print('--')
    print(annograms('drive'))
    print('--')
    print(annograms('python'))