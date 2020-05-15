#Append
# keep track of oldest - index of zero -- [0]
# if there's still space in the ring buffer I want to append to the array

#When it's full go to else
#pop the first number, index 0
#Then there's space and the next item is appended to the end

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def __len__(self):
        return self.capacity

    def print_items(self):
        return self.storage

    def append(self, item):
        # if ring is empty fill it
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            return item
        else:
            if self.oldest < self.capacity:
                oldest = self.storage[self.oldest]
                self.storage.pop(self.oldest)
                self.storage.insert(self.oldest, item)
                self.oldest += 1
            
            else:
                print('full, restart selfoldest again')
                self.oldest = 0
                self.append(item)
    def get(self):
        return self.storage

