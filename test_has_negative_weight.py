from has_negative_weight import has_negative_weight
# Test Case 6: Graph with positive weights only
graph6 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1)],
    'C': []
}
expected_output6 = False
assert has_negative_weight(graph6) == expected_output6

# Test Case 7: Graph with a single negative weight
graph7 = {
    'A': [('B', 2), ('C', -4)],
    'B': [('C', 1)],
    'C': []
}
expected_output7 = True
assert has_negative_weight(graph7) == expected_output7

# Test Case 8: Graph with multiple nodes and edges
graph8 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1)],
    'C': [('D', -3)],
    'D': []
}
expected_output8 = True
assert has_negative_weight(graph8) == expected_output8

# Test Case 9: Graph with self-loop and negative weight
graph9 = {
    'A': [('A', -2)],
    'B': [('C', 1)],
    'C': []
}
expected_output9 = True
assert has_negative_weight(graph9) == expected_output9

# Test Case 10: Graph with disconnected components
graph10 = {
    'A': [('B', 2)],
    'B': [],
    'C': [('D', -4)],
    'D': []
}
expected_output10 = True
assert has_negative_weight(graph10) == expected_output10

print("All test cases passed!")