from collections import deque 




def path_to_exit(maze, start, exit):
    queue       = deque()
    revisited   = {}
    queue.append(start)
    while queue:
        position = queue.pop()
        revisited[str(position[0])+""+str(position[1])] = True
        print("We're at position",position)
        print(revisited)
    print(queue)    
    print(maze)
    print(start)
    print(exit)


maze = [[0,0,1],
        [1,0,1],
        [1,0,1]]

path_to_exit(maze,[0,0],[2,1])