class Stack:
    def __init__(self):
        self._data = list()

    def is_empty(self):
        return len(self) == 0
   
    def __len__(self):
        return len(self._data)  
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack kosong. tidak ada data top')
        else:
            return self._data[-1]
        
    def pop(self):
        if self.is_empty():
            raise Exception('Stack kosong. tidak ada data yang dapat di-pop')
        else:
            return self._data.pop()
    
    def push(self, data):
        self._data.append(data)

    def printdata(self):
        for item in self._data:
            print(item)

    def deleteall(self):
        while not self.is_empty():
            self._data.pop()

mystack = Stack()
mystack.push(10)
mystack.push(21)
mystack.push(32)

print(f'Total Data = {mystack.__len__()}')
print(f'Elemen TOP = {mystack.peek()}')
print()

print('Data dalam Stack: ')
mystack.printdata()

print()
print('Hapus Data')
mystack.pop()
print('Data dalam Stack')
mystack.printdata()

print('Hapus Seluruh Data')
mystack.deleteall()
if mystack.is_empty():
    print('Stack kosong')
else:
    print('Data dalam Stack: ')
    mystack.printdata()