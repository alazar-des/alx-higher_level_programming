#!/usr/bin/python3
import hidden_4
name = dir(hidden_4)
for i in range(len(name)):
    if name[i][0] == '_' and name[i][1] == '_':
        continue
    print("{}".format(name[i]))
