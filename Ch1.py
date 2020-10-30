def reverse_str(a,b):
    len_word = len(b)
    pos = a.find(b)
    b_rev = b[::-1]
    i = 0
    c = ""
    while i < pos:
        c += (a[i])
        i +=1
    c += (b_rev)
    i += len(b)
    while i < len(a):
        c +=(a[i])
        i+=1
    return c
    
print (reverse_str("This was the way!!", "was"))

