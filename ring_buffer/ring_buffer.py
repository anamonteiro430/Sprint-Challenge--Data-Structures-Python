#Append
# keep track of oldest - index of zero -- [0]
# if there's still space in the ring buffer I want to append to the array

#When it's full go to else
#pop the first number, index 0
#Then there's space and the next item is appended to the end

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity #number of slots in the array
        self.storage = [] #array with "capacity" number of slots
        self.oldest = 0 #store the oldest value's index at the moment

    def __len__(self):
        return self.capacity

    def print_items(self):
        return self.storage

    def append(self, item):
        # if ring is empty fill it
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            return item
        else: #when ring is full:
            if self.oldest < self.capacity: #if index is in range of list
                oldest = self.storage[self.oldest] #hold value at oldest, starts index 0
                self.storage.pop(self.oldest) #take out the number in that index
                self.storage.insert(self.oldest, item) #insert in that index the new item
                self.oldest += 1 #accumulator - plus one until it is the same value as tha capacity
            #index is out of range    
            else:
                self.oldest = 0 #restart the accumulator
                self.append(item) #recursion - call the function again
                #attribute oldest is zero again!
    def get(self):
        return self.storage

