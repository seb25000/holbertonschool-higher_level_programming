#!/usr/bin/env python3
for i in range(100):
    for j in range(i, 100):
        if i != j:
            print("{:02d}, {:02d}".format(i, j), end=", " if i < 98 else "\n")
