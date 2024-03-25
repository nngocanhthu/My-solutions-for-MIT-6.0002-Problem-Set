from ps1a import *
from ps1b import *

def test_load_cows(filename, actual_result='Pass'):
    print('Actual result:', actual_result)
    print('Function result:', load_cows(filename))

def test_greedy_cow_transport(cows, limit=10, actual_result='Pass'):
    print('Actual result:', actual_result)
    print('Function result:', greedy_cow_transport(cows,limit))
    
def test_brute_force_cow_transport(cows,limit=10, actual_result='Pass'):
    print('Actual result:', actual_result)
    print('Function result:', brute_force_cow_transport(cows,limit=10))
# TEST

# Problem 1
filename = 'ps1_cow_data_2.txt'
test_load_cows(filename, actual_result='Pass')

print()

# Problem 2
cows = load_cows(filename)
test_greedy_cow_transport(cows, limit=10, actual_result='Pass')

print()

# Problem 3
test_brute_force_cow_transport(cows,limit=10, actual_result='Pass')