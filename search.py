# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()
    

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    perimeter = util.Stack()
    visited = []
    
    perimeter.push((problem.getStartState(), [], 0)) # [] = list of entire path to goal | 0 = cost of entire path
    while not perimeter.isEmpty():
        vFrom = perimeter.pop()
        if problem.isGoalState(vFrom[0]):
                return vFrom[1]
        if vFrom[0] not in visited:
            for edge in problem.getSuccessors(vFrom[0]):
                perimeter.push((edge[0], vFrom[1] + [edge[1]], edge[2] + vFrom[2]))
            visited.append(vFrom[0])

def _old_breadthFirstSearch(problem: SearchProblem):
    node = { "state": problem.getStartState(), "cost": 0 }
    
    if problem.isGoalState(node["state"]):
        return []
    
    perimeter = util.Queue()
    perimeter.push(node)
    visited = set()
    
    while True:
        node = perimeter.pop()
        visited.add(node["state"])
        successors = problem.getSuccessors(node["state"])
        for successor in successors:
            child = { "state": successor[0], "action": successor[1], "cost": successor[2], "parent": node }
            if child["state"] not in visited:
                if problem.isGoalState(child["state"]):
                    actions = []
                    node = child
                    while "parent" in node:
                        actions.append(node["action"])
                        node = node["parent"] 
                    actions.reverse() # because we need to backtrack from the ending to the beginning, but we want correct order
                    return actions
                perimeter.push(child)

def breadthFirstSearch(problem: SearchProblem):
    perimeter = util.Queue()
    visited = set()

    perimeter.push((problem.getStartState(), [])) 
    visited.add(problem.getStartState())

    while not perimeter.isEmpty():
        vFrom = perimeter.pop()
        if (problem.isGoalState(vFrom[0])):
            return vFrom[1]
        for edge in problem.getSuccessors(vFrom[0]):
            to = edge[0]
            if to not in visited:
                perimeter.push((to, vFrom[1] + [edge[1]]))
                visited.add(to)
    return []

def dijkstraSearch(problem: SearchProblem):
    # save the path to the goal in edgeTo
    edgeTo = {}
    distTo = {}

    perimeter = util.PriorityQueue()
    perimeter.push(problem.getStartState(), 0)
    distTo[problem.getStartState()] = 0

    while not perimeter.isEmpty():
        u = perimeter.pop()

        for v in problem.getSuccessors(u):
            if(v[0] not in distTo):
                distTo[v[0]] = sys.maxsize # infinity
            oldDist = distTo[v[0]]
            newDist = distTo[u] + v[2]
            if newDist < oldDist:
                distTo[v[0]] = newDist
                edgeTo[v[0]] = (u, v[1])

                if problem.isGoalState(v[0]):
                    print(f"found goal. cost: {newDist}")
                    path = []
                    v = edgeTo[v[0]] # ends in wall without this
                    while v[0] != problem.getStartState():
                        path.append(v[1])
                        v = edgeTo[v[0]]
                    path.append(v[1])
                    path.reverse()
                    return path
                
                if perimeter.heap.__contains__(v[0]):
                    perimeter.update(v[0], newDist)
                else:
                    perimeter.push(v[0], newDist)
        
    return []
                

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
djk = dijkstraSearch