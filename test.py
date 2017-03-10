from Stack_Linked_List import *
import sys
from world import *


def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = ("Test at line {0} FAILED.".format(line_num))
    print(msg)
    
    
def test_simple():
    
    test(where_is_robot() == [7, 0])
    test(move_robot(5, 0) == [5, 0])
    test(where_is_robot() == [5, 0])
    test(is_feasible(0, 10) == False) 
    test(is_feasible(1, 5) == False) 
    test(move_robot(0, 7) == [0, 7])
    test(goal_reached(robot[0], robot[1], goal[0], goal[1])==True)
    test(is_feasible(0, 9) == False)
    test(is_feasible(0, 7) == True)

    #Test The Stack
    move_robot(0, 7)
    current_path.push('07')
    move_robot(0, 6)
    current_path.push('06')
    test(is_feasible(0, 7) == True)
    test(is_feasible(0, 7) and current_path.push(str(0) + str(7)) == False)

print(test_simple())