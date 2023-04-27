from itertools import groupby
from operator import itemgetter

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.iteritems(), key=itemgetter(1))
for k, g in groupby(di, key=itemgetter(1)):
    print( k, map(itemgetter(0), g))

def getVal (i,x):
     return i - x

data = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in groupby(enumerate(data), getVal(i,x)):
     print( map(itemgetter(1), g))