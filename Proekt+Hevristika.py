from utils import *
from informed_search import *
import random
import math


"""def reduce_goal(positions, goal):


    new_goal = list(goal)
    new_positions = list(positions)

    print(positions)
    print(result)
    for i in range(len(goal)):
        for j in range(len(positions)):
            if goal[i] == positions[j]:
                new_goal.remove(goal[i])
                new_positions.remove(positions[j])
                
    return [tuple(new_goal), tuple(new_positions)]"""


def up(state, positions, M):
    permission = True
    index = 0

    for pos in positions:
        if state == pos:
            index = positions.index(pos)
        if state[0] == pos[0] and state[1] + 1 == pos[1]:
            permission = False

    if state[1] + 1 <= M and permission == True:
        new_state = [state[0], state[1] + 1, state[2]]
        positions[index] = tuple(new_state)

    return positions


def down(state, positions):
    permission = True
    index = 0

    for pos in positions:
        if state == pos:
            index = positions.index(pos)
        if state[0] == pos[0] and state[1] - 1 == pos[1]:
            permission = False

    if state[1] - 1 > 0 and permission == True:
        new_state = [state[0], state[1] - 1, state[2]]
        positions[index] = tuple(new_state)

    return positions


def right(state, positions, N):
    permission = True
    index = 0

    for pos in positions:
        if state == pos:
            index = positions.index(pos)
        if state[0] + 1 == pos[0] and state[1] == pos[1]:
            permission = False

    if state[0] + 1 <= N and permission == True:
        new_state = [state[0] + 1, state[1], state[2]]
        positions[index] = tuple(new_state)

    return positions


def left(state, positions):
    permission = True
    index = 0
    for pos in positions:
        if state == pos:
            index = positions.index(pos)
        if state[0] - 1 == pos[0] and state[1] == pos[1]:
            permission = False

    if state[0] - 1 > 0 and permission == True:
        new_state = [state[0] - 1, state[1], state[2]]
        positions[index] = tuple(new_state)

    return positions



class RollerskatingPacman(Problem):
    def __init__(self, initial, M, N, C, goal=None):
        super().__init__(initial, goal)
        self.M = M
        self.N = N
        self.C = C


    def successor(self, state):
        successors = dict()

        positions = list(state)
        self.C += 1

        for r in range(len(positions)):
            pickedState = positions[r]

            tempPos = positions[:]
            new_positions = up(pickedState, tempPos, self.M)
            if new_positions != positions:
                color = positions[r][-1]
                successors['UP '+color] = tuple(new_positions)
        
            tempPos = positions[:]
            new_positions = down(pickedState, tempPos)
            if new_positions != positions:
                color = positions[r][-1]
                successors['DOWN '+color] = tuple(new_positions)

            tempPos = positions[:]
            new_positions = right(pickedState, tempPos, self.N)
            if new_positions != positions:
                color = positions[r][-1]
                successors['RIGHT '+color] = tuple(new_positions)

            tempPos = positions[:]
            new_positions = left(pickedState, tempPos)
            if new_positions != positions:
                color = positions[r][-1]
                successors['LEFT '+color] = tuple(new_positions)

        return successors


    def actions(self, state):
        return self.successor(state).keys()


    def result(self, state, action):
        return self.successor(state)[action]


    def goal_test(self, state):
        return self.goal == state


    def h(self, node):
        state = node.state
        goal = list(self.goal)
        value = 0

        for x,y in zip(state, goal):
            value += (abs(x[0] - y[0]) + abs(x[1] - y[1]))*2
        print(value)
        return value


    def get_C(self):
        return self.C



if __name__ == '__main__':
    C = 0
    M = int(input())
    while M % 2 != 0:
        print("Vnesi paren broj za M")
        M = int(input())
    #number of both green and yellow pacman
    K = M//2

    N = int(input())
    while N < 4:
        print("N mora da bide pogolemo od 3")
        N = int(input())

    start_positions = []
    goal = []
    #yellow pacman
    for i in range(K):
        start_positions.append((1, M - i, "yellow"))
        goal.append((1, M - i, "green"))
    #green pacman
    for i in range(K):
        start_positions.append((N, 1 + i, "green"))
        goal.append((N, 1 + i, "yellow"))

    goal.reverse()
    goal = tuple(goal)
    start_positions = tuple(start_positions)

    rsPacman = RollerskatingPacman((start_positions), M, N, C, goal)

    result = astar_search(rsPacman)
    print(result.solve())
    print(rsPacman.get_C())
    print(start_positions)
    print(goal)
