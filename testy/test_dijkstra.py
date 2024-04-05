import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dijkstra import dijkstra

# Test Case 1: Basic graph with positive weights
graph1 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1)],
    'C': []
}
start1 = 'A'
end1 = 'C'
expected_output1 = (['A', 'B', 'C'], 3)
assert dijkstra(graph1, start1, end1) == expected_output1

# Test Case 2: Graph with a negative weight
graph2 = {
    'A': [('B', 2), ('C', -4)],
    'B': [('C', 1)],
    'C': []
}
start2 = 'A'
end2 = 'C'
expected_output2 = (['A', 'C'], -4)
assert dijkstra(graph2, start2, end2) == expected_output2

# Test Case 3: Graph with multiple negative weights
graph3 = {
    'A': [('B', -2), ('C', -4)],
    'B': [('C', 1)],
    'C': []
}
start3 = 'A'
end3 = 'C'
expected_output3 = (['A', 'C'], -4)
assert dijkstra(graph3, start3, end3) == expected_output3

# Test Case 4: Graph with no edges
graph4 = {}
start4 = 'A'
end4 = 'C'
expected_output4 = None
assert dijkstra(graph4, start4, end4) == expected_output4

# Test Case 5: Graph with only negative weights
graph5 = {
    'A': [('B', -2), ('C', -4)],
    'B': [('C', -1)],
    'C': []
}
start5 = 'A'
end5 = 'C'
expected_output5 = (['A', 'C'], -4)
assert dijkstra(graph5, start5, end5) == expected_output5

print("All test cases passed!")