from world import goal_reached, is_feasible, where_is_robot, goal, world
from Stack_Linked_List import *


def run_robot(j, i, path):

    print(i, j)

    # Base Case
    if goal_reached(j, i, goal[0], goal[1]):
        return "You have found a solution! " + str(path)

    # Push onto the stack the current position of the robot
    path.push(str(j) + str(i))

    # Check which direction doesn't have a wall and hasn't been visited before...
    if is_feasible(j-1, i) and path.push(str(j-1) + str(i)):
        return run_robot(j-1, i, path)

    if is_feasible(j+1, i) and path.push(str(j+1) + str(i)):
        return run_robot(j+1, i, path)

    if is_feasible(j, i-1) and path.push(str(j) + str(i-1)):
        return run_robot(j, i-1, path)

    if is_feasible(j, i+1) and path.push(str(j) + str(i+1)):
        return run_robot(j, i+1, path)

    '''If no direction is feasible then do as follows....
    1) Remove the head of the stack
    2) Turn your current position into a wall so you cannot backtrack
    3) Read the head of the stack so that you know the previous coordinates
    4) Feed the coordinates and the stack into the recursion'''
    path.pop()
    world[j][i] = 1
    z = str(current_path.head())[6:]
    return run_robot(int(z[0]), int(z[1]), current_path)


if __name__ == '__main__':
    x, y = where_is_robot()
    print(run_robot(x, y, current_path))