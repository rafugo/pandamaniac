import sim
import json

# read in the graph
with open('testgraph1.json') as f:
    graph = json.load(f)



# generate nodes
strategies = {'strat1' : ['1'], 'strat2': ['344']}

# run sim
result = sim.run(graph, strategies)

print(result)