import bf_library

class BFCompilerWithOptimizedLibrary(bf_library.BFCompilerWithLibary):
    def __init__(self, memory_size):
        self.free_list = FreeList(memory_size)
        
    def malloc(self, size):
        return self.free_list.malloc(size)
    
    def free(self, pointer):
        self.free_list.free(pointer)
    
    def output_string(string):
        if string:
            last_char = string[0]
            self.add(ord(last_char))
            self.output_char()
            for char in string[1:]:
                diff = abs(ord(char) - ord(last_char))
                func = self.add if ord(char) > ord(last_char) else self.sub
                func(diff)
                self.output_char()
                last_char = char

class FreeList(dict):
    def __init__(self, size):
        entry = FreeListEntry(0,size,0,None,None)
        self[0] = entry
    def malloc(self, size):
        for index, entry in self.items():
            freeSize = entry.size()
            if (not entry.allocated() and freeSize >= size):
                prev = entry.prev()
                next = entry.next()
                if prev:
                    prev.setNext(entry)
                if next:
                    next.setPrev(entry)
                newAllocatedBlock = FreeListEntry(index, size, 1, prev, next)
                self[index] = newAllocatedBlock
                if (freeSize > size):
                    freeIndex = index + size
                    newFreeBlock = FreeListEntry(freeIndex, freeSize - size, 0, newAllocatedBlock, next)
                    newAllocatedBlock.setNext(newFreeBlock)
                    if next: next.setPrev(newFreeBlock)
                    self[freeIndex] = newFreeBlock
                return index
        raise Exception("malloc() failed, no more memory")
    def free(self, index):
        i, size, allocated, prev, next = self[index]
        if not(allocated):
            raise Exception("trying to free unallocated space")
        if prev and not prev.allocated():
            self.pop(index)
            index = prev.index()
            size += prev.size()
            prev = prev.prev()
        if next and not next.allocated():
            size += next.size()
            self.pop(next.index())
            next = next.next()
        newEntry = FreeListEntry(index, size, 0, prev, next)
        if prev: prev.setNext(newEntry)
        if next: next.setPrev(newEntry)
        self[index] = newEntry

class FreeListEntry(list):
    def __init__(self, index, size, allocated, prev, next):
        for arg in (index, size, allocated, prev, next):
            self.append(arg)
    def index(self):
        return self[0]
    def size(self):
        return self[1]
    def allocated(self):
        return self[2]
    def prev(self):
        return self[3]
    def setPrev(self, prevEntry):
        self[3] = prevEntry
    def next(self):
        return self[4]
    def setNext(self, nextEntry):
        self[4] = nextEntry