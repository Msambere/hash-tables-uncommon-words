'''
- Challenge #2
  - Allow a word to appear any number of times in a single sentence for it to still be
considered uncommon. 
  If it appears in more than one sentence, then it is no longer uncommon.
'''
def uncommon_from_sentences(sentences):
    word_freq={}
    for sentence in sentences:
        sentence = sentence.split(" ")
        sentence = list(set(sentence))
        for word in sentence:
            print(word)
            count = word_freq.get(word, 0)
            word_freq[word]= count+1

    results =[]
    
    for word, count in word_freq.items():
        if count == 1:
            results.append(word)
    return results
