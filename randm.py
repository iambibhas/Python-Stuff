import sys
import random

def get_random_string(length=8):
    """Returns a string of random characters of given length."""
    string = ''
    avail_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?><._abcdefghijklmnopqrstuvwxyz1234567890'

    for i in range(0, length):
        randm[0] = random.randrange(0, len(avail_chars))
        randm[1] = random.randrange(0, len(avail_chars))
        rand = random.randrange(0,2)
        string += avail_chars[randm[rand]]

    return string

def levenshtein(a,b):
    """Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]
