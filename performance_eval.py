from Stack_Linked_List import *
import matplotlib.pyplot as plt
import time


running_times = []

# Increase size of n in increments. 
for n in range(0, 600, 10):
    s = StackLinkedList()
    # Add n elements to the set.
    for i in range(n):
        s.push(Node(n))

    start = time.time()
    # Insert operation you want to test here
    end = time.time()

    run_time = end - start
    print(n, run_time)
    running_times.append(run_time)
# Plot the running times
plt.plot(running_times, 'bx')
plt.xlabel('Size of N (x 1000)')
plt.ylabel('Time')
plt.show()

