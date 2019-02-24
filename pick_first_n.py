# this script just picks the first n nodes given.

import json

n = 1

# load in data
with open('data.json') as f:
    graph = json.load(f)

# iterate through first n and save them
f = open("submission.txt", "w")
i = 0
for key in graph.keys():
    if i >= n:
        break;

    f.write(str(key))
    i++;
