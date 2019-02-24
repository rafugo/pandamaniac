import sim
import json

# read in the graph
with open('testgraph1.json') as f:
    graph = json.load(f)

# generate nodes
strategies = {'strat1' : ['83', '463', '319', '149', '254'], \
            'strat2': ['447', '164', '301', '369', '222']}

# run sim
result = sim.run(graph, strategies)

print(result)