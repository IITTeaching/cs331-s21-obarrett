import urllib
import requests
import queue

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    l = radix_sort()
    a = []
    for i in range(len(l)):
        a.append(l[i].decode("ascii"))
    return a

def itemsToQueues(words,k,maxlen):
    q = [None] * 256
    for i in range(0,256):
        q[i] = []
    for x in range(0,len(words)):
        p = 0
        if not(maxlen - k - 1 >= len(word[j])):
            p = word[x][maxlen - k - 1]
        q[p].append(words[x])
    return q

def queueToArray(queues,numWords):
    w = [ [] for i in range(numWords) ]
    index = 0
    for i in range(0, len(queues)):
        que = queues[i]
        while len(que) > 0:
            w[index] = que.pop(0)
            index += 1
    return w

def radix_sort():
    lst = book_to_words()
    ml = 1
    for i in lst:
        if(len(i) > ml):
            ml = len(i)
    w = book_to_words()
    for x in range(0,lenest_word):
        w = queueToArray(itemsToQueues(words,x,lenest_word),len(w))
    return w
