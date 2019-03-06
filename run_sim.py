import sim
import json

# number of nodes that are submitted
n = 35

# read in the graph
with open('test_graphs/1.8.35.1.json') as f:
    graph = json.load(f)

# read in strategy 1
f1 = open("closeness_clustering_submission.txt", "r")

# f1 = open("top_closeness_submission.txt", "r")
sub1 = []
i = 0
for line in f1:
    if i >= n:
        break;
    i += 1
    sub1.append(line.strip())

f1.close()

# # read in strategy 2
# f2 = open("submission_high_degree.txt", "r")

# read in strategy 2
f2 = open("better_top_closeness_submission.txt", "r")
sub2 = []
j = 0
for line in f2:
    if j >= n:
        break;
    j += 1
    sub2.append(line.strip())
    
f2.close()

# read in strategy 3
f3 = open("closeness_gang_up_submission.txt", "r")
sub3 = []
j = 0
for line in f3:
    if j >= n:
        break;
    j += 1
    sub3.append(line.strip())
    
f3.close()

# read in strategy 4
f4 = open("submission_high_degree.txt", "r")
sub4 = []
j = 0
for line in f4:
    if j >= n:
        break;
    j += 1
    sub4.append(line.strip())
    
f4.close()


# submissions for the strategies
strategies = {'strat1' : sub1, \
            'strat2': sub2, \
            'strat3' : sub3, \
            'strat4' : sub4}

print(strategies['strat1'])
print('')
print(strategies['strat2'])
print('')
print(strategies['strat3'])
print('')
print(strategies['strat4'])
print('')
# run sim
result = sim.run(graph, strategies)

print(result)