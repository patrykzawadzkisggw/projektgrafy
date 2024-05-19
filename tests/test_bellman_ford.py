import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bellman_ford import bellman_ford

# Test Case 1: Shortest path exists
graph1 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1)],
    'C': []
}
start1 = 'A'
end1 = 'C'
expected_output1 = (['A', 'B', 'C'], 3)
assert bellman_ford(graph1, start1, end1) == expected_output1

# Test Case 2: Shortest path does not exist
graph2 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1)],
    'C': []
}
start2 = 'B'
end2 = 'A'
expected_output2 = (['A'], float('inf'))
assert bellman_ford(graph2, start2, end2) == expected_output2

# Test Case 3: Negative cycle exists
graph3 = {
    'A': [('B', 2), ('C', -4)],
    'B': [('C', 1)],
    'C': []
}
start3 = 'A'
end3 = 'C'
expected_output3 = (['A', 'C'], -4)
assert bellman_ford(graph3, start3, end3) == expected_output3

# Test Case 4: Graph with no edges
graph4 = {}
start4 = 'A'
end4 = 'B'
expected_output4 = None
assert bellman_ford(graph4, start4, end4) == expected_output4

print("All test cases passed!")