import pandas as pd
from collections import deque
import operator
"""
Return a callable object that fetches the given item(s) from its operand.
After f = itemgetter(2), the call f(r) returns r[2].
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
"""
from operator import *
from BibleOutline import BibleOutline
r = {'a': {'t': 10}, 'b': {'t': 9}, 'c': {'t': 12}, 'd': {'t': 8}}
rit = iter(r)
# newlist = sorted(rit, key=lambda k_v: k_v[1]['t'])
newlist = sorted(r.items(), key=lambda x: getitem(x[1], 't'))
newlist2 = [(v['abbr'], v['order']) for k, v in BibleOutline.bible_outline.items()]
newlist3 = sorted(newlist2, key=operator.itemgetter(1))
print(newlist3)
