class Queue(object):
    def __init__(self):
        """
        Initializes the internal array for the queue
        """
        self._queue = []
    
    def enqueue(self, item):
        """
        Adds a new item into the queue
        """
        self._queue.insert(0, item)
        return True

    def dequeue(self):
        """
        Removes the item in front of in the queue
        """
        if self.is_empty():
            return False
        self._queue.pop()
        return True
    
    def peek(self):
        """
        Returns the item in front of the queue. It returns -1 if queue is empty
        """
        if (self.is_empty()):
            return -1
        return self._queue[-1]
    
    def length(self):
        """
        Returns the current length of the queue
        """
        return len(self._queue)

    def is_empty(self):
        """
        Returns true if queue is empty
        """
        return self.length() == 0


# Test cases

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print (f'queue length should be 3: {queue.length() == 3}')
queue.dequeue()


print (f'queue length should be 2: {queue.length() == 2}')
print (f'queue.peek() should be 2: {queue.peek() == 2}')

queue.dequeue()
queue.dequeue()
print (f'queue.is_empty() should be true: {queue.is_empty() == True}')