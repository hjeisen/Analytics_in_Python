def word_distribution(sent):
    if not(sent[-1].isalpha()):
        sent = sent [0:-1]
    word_dict = {}
    for i in sent.split():
        #print (i.lower())
        word = i.lower()
        if  word in word_dict:
            word_dict[word] +=1
            #print (word_dict)
        else:
             word_dict[word] = 1
             #print (word_dict)




    return word_dict
    exit

test_str = "That's when I saw Jane (John's sister)!"
print (word_distribution(test_str))