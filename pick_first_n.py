# this script just picks the first n nodes given.

import json
import random

n = 1

# load in data
with open('testgraph1.json') as f:
    graph = json.load(f)

# iterate through first n and save them

i = 0

keys = graph.keys()
random.shuffle(keys)

nodes = []

for key in keys:
    if i >= n:
        break

    nodes.append(key)
    i += 1


# write the chosen nodes 50 times
f = open("submission.txt", "w")
submission_str = ''
for node in nodes:
    submission_str += str(node) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()