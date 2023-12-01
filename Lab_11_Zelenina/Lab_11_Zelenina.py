class Queue:
    def __init__(self) -> None:
        self.new_list_of_queue = []

    def put(self, elem) -> None:
        self.new_list_of_queue.append(elem)

    def get(self):
        if len(self.new_list_of_queue) == 0:
            return False
        else:
            elem = self.new_list_of_queue.pop(0)
            return elem

    def isempty(self):
        return len(self.new_list_of_queue) == 0


class NewQueue(Queue):
    def isempty(self):
        return super().isempty()


new_queue = NewQueue()
new_queue.put(1)
new_queue.put("dog")
new_queue.put(False)

for i in range(4):
    if not new_queue.isempty():
        print(new_queue.get())
    else:
        print("Our queue is empty")