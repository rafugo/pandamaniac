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


# read in strategy 2
f2 = open("submission_high_degree.txt", "r")
sub2 = []
j = 0
for line in f2:
    if j >= n:
        break;

    sub2.append(line.strip())
    j += 1

# submissions for the strategies
strategies = {'strat1' : sub1, \
            'strat2': sub2}

# run sim
result = sim.run(graph, strategies)

print(result)