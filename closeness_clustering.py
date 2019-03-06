# this script picks from nodes with high closeness centrality

import json
import random
import networkx as nx
import operator
import math

n = 35
num_considered = n * 3

### 
### LOAD IN DATA
###
with open('2.5.4.json') as f:
    graph = json.load(f)

keys = graph.keys()
G = nx.Graph()

for item in graph.items():
    for j in range(len(item[1])):
        G.add_edge(item[0], item[1][j])

###
### GET NUM_CONSIDERED HIGH DEGREE NODES
###
degree = len(graph[keys[0]])
nodes = [keys[0]]
min = (keys[0], degree)
i = 1

while i < num_considered:
    degree = len(graph[keys[i]])
    nodes.append(keys[i])
    if degree < min[1]:
        min = (keys[i], degree)
    i += 1
    
while i < len(graph):
    degree = len(graph[keys[i]])
    if degree > min[1]:
        nodes.remove(min[0])
        nodes.append(keys[i])
        min = (keys[i], degree)
        for node in nodes:
            if len(graph[node]) < min[1]:
                min = (node, len(graph[node]))
    i += 1


###
### LABEL ALL THE POINTS WITH CLOSENESS RATING
###
avg = 0
for j in range(len(nodes)):
    # create tuples of (node, closeness)
    node = nodes[j]
    closeness = nx.closeness_centrality(G, node)
    clusterness = nx.clustering(G, nodes = [node])
    clusterness = clusterness[node]

    print("Closeness for node " + str(node) + ": " + str(closeness))
    print("Clustering for node " + str(node) + ": " + str(clusterness) + '\n')

    avg += (closeness - clusterness)

    nodes[j] = (node, closeness + clusterness)

print("Average difference: " + str(avg / len(nodes)))

###
### SORT THE POINTS FROM SMALLEST TO LARGEST
### ON THE COMPONENT
###
nodes = sorted(nodes, key=operator.itemgetter(1))

###
### SELECT THE TOP N NODES FROM THE END
###
top_nodes = []
for j in range(-1, -(n + 1), -1):
    index = (j+1) * -1
    top_nodes.append(nodes[index][0])

###
### WRITE THE SUBMISSION
###
f = open("closeness_clustering_submission.txt", "w")
submission_str = ''
for node in top_nodes:
    submission_str += str(node) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()