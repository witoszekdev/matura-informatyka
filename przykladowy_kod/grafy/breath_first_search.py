from collections import deque

def bfs(graph):
    search_queue = deque()
    search_queue += graph["you"]
    checked_people = []
    while search_queue:
        person_name, gardener = search_queue.popleft()
        if person_name not in checked_people:
            if gardener:
                print(person_name, "jest ogrodnikiem")
            else:
                search_queue += graph[person_name]
                checked_people.append(person_name)

if __name__ == "__main__":
    my_graph = {
        "you": [("janusz", False), ("grażyna", False), ("karyna", False)],
        "janusz": [("grażyna", False), ("bożena", False), ("mariusz", False)],
        "grażyna": [("janusz", False), ("marlenka", True), ("grzesiu", False)],
        "mariusz": [],
        "karyna": [],
        "marlenka": [],
        "grzesiu": [],
        "bożena": []
    }
    print(bfs(my_graph))
