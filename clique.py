import json
import networkx as nx
import operator

# number of nodes that are submitted
n = 20

ppl = 2


# # number considered of top degree nodes
num_considered = n * ppl

with open('6.20.1.json') as f:
    graph = json.load(f)

keys = graph.keys()
G = nx.Graph()

for item in graph.items():
    for j in range(len(item[1])):
        G.add_edge(item[0], item[1][j])

# get high degree corresponding to top ppl * number of nodes
degree = len(graph[keys[0]])
high_degree_nodes = [keys[0]]
min = (keys[0], degree)
i = 1

while i < num_considered:
    degree = len(graph[keys[i]])
    high_degree_nodes.append(keys[i])
    if degree < min[1]:
        min = (keys[i], degree)
    i += 1
    
while i < len(graph):
    degree = len(graph[keys[i]])
    if degree > min[1]:
        high_degree_nodes.remove(min[0])
        high_degree_nodes.append(keys[i])
        min = (keys[i], degree)
        for node in high_degree_nodes:
            if len(graph[node]) < min[1]:
                min = (node, len(graph[node]))
    i += 1

high_degree_nodes = sorted(high_degree_nodes)

cliques = nx.cliques_containing_node(G, high_degree_nodes)

max_size = 0
best_node = 0
max_index = 0
for key in cliques:
    j = 0
    for lst in cliques[key]:
        if max_size < len(lst):
            max_size = len(lst)
            max_index = j
            best_node = key
        j+=1

best_clique = cliques[best_node][max_index]
print("size of best clique: ", max_size)
print("best_clique: ", best_clique)
print("best_node: ", best_node)

top_nodes = []
for i in range(len(best_clique)):
    c = nx.closeness_centrality(G, best_clique[i])
    top_nodes.append((best_clique[i], c))

top_nodes = sorted(top_nodes, key=operator.itemgetter(1))[::-1]

# take out the closeness part
for i in range(len(top_nodes)):
    top_nodes[i] = top_nodes[i][0]

print("Top nodes: ", top_nodes)

if len(top_nodes) < n:
    i = -1
    while len(top_nodes) < n:
        top_nodes.append(high_degree_nodes[i])
        i -= 1

else:
    top_nodes = top_nodes[:n]


    
# write the chosen nodes 50 times
f = open("clique_submission.txt", "w")
submission_str = ''
for node in top_nodes:
    submission_str += str(node) + '\n'

for i in range(50):
    f.write(submission_str)

f.close()

