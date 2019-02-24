import sim
import json

# number of nodes that are submitted
n = 5

# read in the graph
with open('testgraph1.json') as f:
    graph = json.load(f)

# read in strategy 1
f1 = open("top_clustering_submission.txt", "r")
sub1 = []
i = 0
for line in f1:
    if i >= n:
        break;
    i += 1
    sub1.append(line.strip())


# read in strategy 2
f2 = open("submission.txt", "r")
sub2 = []
j = 0
for line in f2:
    if j >= n:
        break;
    j += 1
    sub2.append(line.strip())
# submissions for the strategies
strategies = {'strat1' : sub1, \
            'strat2': sub2}

# run sim
result = sim.run(graph, strategies)

print(result)