class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        # check the length of the buffer
        if len(self.storage) == self.capacity:
            # if the buffer is full
            # replace the oldest item
            if self.oldest >= self.capacity:
                self.oldest = 0
                self.storage[self.oldest] = item
            else:
                self.storage[self.oldest] = item

            self.oldest += 1
        else:
            # otherwise add the item to the list
            self.storage.append(item)

    def get(self):
        return self.storage
