# Time Complexity : O(1) for push, O(n) for pop
# Space Complexity : O(n) for storing n nodes in stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = Node(-1)
        self.count = 0

    def push(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.count+=1

    def pop(self):
        if self.count >= 1:
            curr = self.head.next
            while curr.next and curr.next.next:
                curr = curr.next

            res = curr.next.data if curr.next else curr.data
            curr.next = None
            self.tail = curr
            self.count-=1
            return res


a_stack = Stack()
while True:
    # Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print("push <value>")
    print("pop")
    print("quit")
    do = input("What would you like to do? ").split()
    # Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == "push":
        a_stack.push(int(do[1]))
    elif operation == "pop":
        popped = a_stack.pop()
        if popped is None:
            print("Stack is empty.")
        else:
            print("Popped value: ", int(popped))
    elif operation == "quit":
        break
