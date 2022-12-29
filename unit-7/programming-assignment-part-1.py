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

def has_duplicates(s):
    histo = histogram(s)

    for value in histo.values():
        if(value > 1):
            return True
    
    return False


for test in test_dups:
    if(has_duplicates(test)):
        print(test + ' has duplicates')
    else:
        print(test + ' has no duplicates')