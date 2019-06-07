import unittest
import math
from ddt import ddt

def permutate_dfs_recursive(remaining, current='', solution=None):
    
    #  Initliaze solution
    if solution is None:
        solution = []
    
    # Termination condition
    # Print/ Store solution
    if remaining == '':
        solution.append(current)
    
    # Scan childrens
    for item in remaining:
        new_remaining = remaining.replace(item, '')
        permutate_dfs_recursive(new_remaining, current + item, solution)
    
    return solution

def permutate_dfs(remaining): 
    solution = []
    pending_items = [(remaining, '')] #remaining, current
    
    while len(pending_items) > 0:
        remaining, current = pending_items.pop(0)
        
        # Termination condition
        # Print/ Store solution
        if remaining == '':
            solution.append(current)
        
        for item in remaining:
            pending_items.insert(0, (remaining.replace(item, ''), current + item))
            
    return solution
        

@ddt
class TestPermutation(unittest.TestCase):
    
    def setUp(self):
        self.test_data = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
        self.test_algorithm = [permutate_dfs, permutate_dfs_recursive]
    
    # Number solutions must be n! where n is count of unique items
    def test_permutate_check_count(self):
        for tdata in self.test_data:
            for algorithm in self.test_algorithm:
                soln = algorithm(tdata)
                self.assertEqual(len(soln), 
                                 math.factorial(len(tdata)),
                                 'Solution is not {}! for {} with data ''{}'''.format(len(tdata), algorithm.__name__, tdata))
    
    # Each string in solution should be unique
    def test_permutate_check_uniquess(self):
        for tdata in self.test_data:
            for algorithm in self.test_algorithm:
                soln = algorithm(tdata)
                self.assertEqual(len(soln), 
                                 len(set(soln)),
                                 'Solution items are not unique for {} with data ''{}'''.format(algorithm.__name__, tdata))
    
    # Each string in solution has length same as input string            
    def test_permutate_check_length(self):
        for tdata in self.test_data:
            for algorithm in self.test_algorithm:
                soln = algorithm(tdata)
                self.assertTrue(all(len(s) == len(tdata) for s in soln),
                                "Solution item should have same length {} for {} with data ''{}''".format(len(tdata), algorithm.__name__, tdata))

if __name__ == '__main__':
    unittest.main(verbosity=2)
