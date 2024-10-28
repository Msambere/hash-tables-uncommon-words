'''
- Challenge #1
  - Extend to handle any number of sentences. 
  A word may still only occur once in the sentence in which it appears to be 
  considered uncommon.
'''

def uncommon_from_sentences(sentences):
    word_freq={}
    for sentence in sentences:
        sentence = sentence.split(" ")
        for word in sentence:
            print(word)
            count = word_freq.get(word, 0)
            word_freq[word]= count+1
    print(word_freq)

    results =[]
    
    for word, count in word_freq.items():
        if count == 1:
            results.append(word)
    return results
