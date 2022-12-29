alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

def missing_letters(s):
    histo = histogram(s)
    miss = []
    for l in alphabet:
        if l not in histo:
            miss.append(l)

    return ''.join(miss)


for test in test_miss:
    missing = missing_letters(test)
    if(missing):
        print(test + ' is missing letters ' + missing)
    else:
        print(test + ' uses all the letters')