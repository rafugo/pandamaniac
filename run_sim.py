import sim
import json

# number of nodes that are submitted
n = 5

# read in the graph
with open('testgraph1.json') as f:
    graph = json.load(f)

# read in strategy 1
f1 = open("submission.txt", "r")
sub1 = []
i = 0
for line in f1:
    if i >= n:
        break;

    sub1.append(line.strip())
    i += 1

f1.close()


# read in strategy 2
f2 = open("submission_neighbors.txt", "r")
sub2 = []
i = 0
for line in f2:
    if i >= n:
        break;

    sub2.append(line.strip())
    i += 1
    
f2.close()

# submissions for the strategies
strategies = {'strat1' : sub1, \
            'strat2': sub2}

print(strategies)
# run sim
result = sim.run(graph, strategies)

print(result)