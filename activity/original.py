'''
- A sentence is a string of single-space separated words where each word consists only of lowercase letters.
- A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
- Given two sentences s1 and s2, return a list of all the uncommon/unique words. The words may be returned in any order.
'''

def uncommon_from_sentences(s1, s2):
    word_list = s1.split(" ")+s2.split(" ")
    word_freq={}

    for word in word_list:
        count = word_freq.get(word, 0)
        word_freq[word]= count+1
    
    results =[]
    
    for word, count in word_freq.items():
        if count == 1:
            results.append(word)
    return results
