"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        #TODO
        return (None,)
    
    def is_goal(self,node):
        """is True if node is a goal"""
        #TODO
        return len(node) % 2 == 0 # dummy goal, state has two items in it

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        #TODO
        return [Arc(node, node+(None,), 1, 'ADD-NONE')]

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        #TODO
        return 0
    

