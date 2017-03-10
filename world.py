import os


def where_is_robot():
    return robot


def move_robot(j, i):
    robot.clear()
    robot.append(j)
    robot.append(i)
    return robot


def is_feasible(j, i):
    if j >= 0 and j < n:
        if i >= 0 and i < n:
            if world[j][i] != 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def goal_reached(robot1, robot2, goal1, goal2):
    if robot1 == goal1 and robot2 == goal2:
        return True
    else:
        return False

if os.path.isfile("other/world1.dat"):
    f1 = open("other/world1.dat", 'r')
    
    counter = 0
    n = 0
    
    for line in f1:
        counter += 1
        line = line.replace(",", " ")
        line = line.replace("x", " ")
        line = line.split()
        
        if counter == 1:
            n = int(line[0])
            world = [[0 for _ in range(n)] for _ in range(n)]            
                 
        if line[0] == 'w':
            j, i = int(line[1]), int(line[2])
            world[j][i] = 1
            
        if line[0] == 'r2d2':
            j, i = int(line[1]), int(line[2])
            world[j][i] = 'R'
            robot = [j, i]
            
            
        if line[0] == 'goal':
            j, i = int(line[1]), int(line[2])
            world[j][i] = 'G'
            goal = [j, i]
else:
    print("Error: File does not exist.")            

if __name__ == '__main__':
    result = ""
    for row in world:
        result += (" ".join(map(str,row))) + "\n"
    print(str(result))    
    

