# this is just a rough outline for completing problem 1 from programming assignment 1
# you don't have to use this code if you don't want to, but at least read and understand it

#     here are suggested interfaces for the Stack and Queue classes
#
#     interface stack {
#         Boolean is_empty();           // returns True if empty, False if not
#         void push(Type X);            // pushes X onto the stack
#         Type pop() raises Underflow;  // pops top element of the stack,
#                                          raises Underflow if stack is empty
#     }
#
#     interface queue {
#         Boolean is_empty();               // returns True if empty, False if not
#         void enqueue(Type X);             // appends X to the queue
#         Type dequeue() raises Underflow;  // removes front element of the
#
#                       queue, raises Underflow if queue is empty
#     };

import sys
from doublellsentinel import DoubleLLSentinel
import copy
# custom Underflow exception
class Underflow(Exception):
    pass  # make it fancier if you want :)

class Queue:

    def __init__(self):
        self.t = DoubleLLSentinel()

    def enqueue(self, x):
        self.t.insertQueue(x)

    def dequeue (self):
        if self.is_empty():
            return ("QueueError")
        self.d = self.t.sntl.next.data
        self.t.delete(self.t.sntl.next)
        return self.d

    def is_empty(self):
        return len(self.t) == 0

# TODO: implement the print function
def print_queue(s):
    # only use s.push, s.pop, and s.is_empty
    s2 = copy.deepcopy(s)
    if s2.is_empty():
        print("Empty")
    else:
        v=''
        for i in range(len(s2.t)):
            v += "{} ".format(s2.dequeue(), end = '')
        print(v.strip())

def driver():
    s = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                # TODO: implement push action
                s.enqueue(value)
            elif action == "dequeue":
                # TODO: implement pop action
                try:
                    print(s.dequeue())
                except Underflow:
                    print("QueueError")
            elif action == "print":
                # TODO: implement print action
                print_queue(s)  # change this!
# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
