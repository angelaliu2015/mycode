#!/usr/bin/env python3
mess= [1, 2, [3, 4, 5, {"six":6, "seven":7, "eight":8}]]
a = mess[-1][-1]
print(a.get('eight','number eight does not exsit'))
