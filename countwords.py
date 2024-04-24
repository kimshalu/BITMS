def countwords(sentence):
    wordcount = {}
    words = sentence.split()
    for i in words:
        if i in wordcount:
            wordcount[i] += 1
        else:
            wordcount[i] = 1
    return wordcount

sentence =input('enter the string\n')
countdict = countwords(sentence)
print(countdict)
