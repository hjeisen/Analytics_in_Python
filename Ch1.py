def reverse_str(a,b):
    len_word = len(b)
    pos = a.find(b)
    b_rev = b[::-1]
    c= a[0:pos] + b_rev + a[pos+len_word::]

    return c
    
print (reverse_str("This is the was way!!", "is"))

