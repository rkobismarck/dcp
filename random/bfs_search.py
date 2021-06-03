# Definition of the elements

from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob']    = ['anuj','peggy']
graph['alice']  = ['peggy']
graph['claire'] = ['thom','jhony']
graph['anuj']   = []
graph['peggy']  = []
graph['thom']   = []
graph['jhony']  = []

def breadth_first_search(start_point):
    seen_persons = {}
    if start_point == None:
        return 'Non traverse possible'
    else:
        search_queue = deque()
        search_queue += start_point
        while search_queue:
            person = search_queue.popleft()
            if person not in seen_persons:
                print("Person name will be:", person)
                search_queue += graph[person]
                seen_persons[person] = True
        
    return None

breadth_first_search(graph['you'])