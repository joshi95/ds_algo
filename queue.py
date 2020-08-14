class Queue:
    def __init__(self):
        self.__queue = list()

    def push(self, x):
        self.__queue.append(x)

    def pop(self):
        self.__queue.pop(0)
    
    def get_front(self):
        return self.__queue[0]
    
    def get_rear(self):
        return self.__queue[-1]

queue = list()
x = 10
queue.append(x)
queue.pop(0)

front = 0 # which element is bound to be removed
rear = 0 # after which element should an
# element be inesrted

queue = [1, 2, 4, 5]


