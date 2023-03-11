import array
import ctypes
import time
import random


class Storage:
    def __init__(self, size):
        self.length = 0
        self.capacity = size
        self.array = (self.capacity * ctypes.py_object)()

    def check_size(self):
        if self.length == self.capacity:
            self._resize(self.capacity * 2)

    def append_on_beginning(self, data):
        self.check_size()
        new_arr = ((self.capacity + 1) * ctypes.py_object)()
        for idx in range(self.length):
            new_arr[idx + 1] = self.array[idx]
        new_arr[0] = data
        self.array = new_arr
        self.length += 1

    def append_on_end(self, data):
        self.check_size()
        self.array[self.length] = data
        self.length += 1

    def append_index(self, index, data):
        if 0 <= index <= self.length - 1:
            self.check_size()
            self.array[index] = data
            self.length += 1
        else:
            print("Error index (index must be > 0 and < length -1")

    def _resize(self, new_size):
        new_arr = (new_size * ctypes.py_object)()
        for idx in range(self.length):
            new_arr[idx] = self.array[idx]
        self.array = new_arr
        self.capacity = new_size

    def index(self, data):
        for iterator in range(0, self.length):
            if self[iterator] == data:
                return iterator
        print("Can't find")

    # index > 0 and index < self.length - 1

    def get_with_delete(self, index):
        if 0 <= index <= self.length - 1:
            tmp = self.array[index]
            self.remove_ind(index)
            return tmp
        else:
            print("Can't find")

#    def get_last_with_delete(self):
#        tmp = self.array[self.length - 1]
#        self.remove_ind(self.length - 1)
#        self.length -= 1
#        return tmp

    def remove_val(self, data):
        if self.index(data):
            self[self.index(data)] = "None"
            #print("\nwork")
        else:
            print("Can't find")

    def remove_ind(self, index):
        if 0 <= index <= self.length - 1:
            self.array[index] = "None"
            #print("\nwork")
        else:
            print("Can't find")

    def get_length(self):
        return self.length

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return self.array[idx]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __repr__(self):
        result = f""
        for iterator in range(0, self.length):
            result += f" {iterator} - {str(self[iterator])} \n"
        return f"{result}"


def rand_func(storage, numbers):
    random_choice = random.randint(0, 4)
    match random_choice:
        case 0:
            storage.append_on_beginning(random.randint(0, 50))
            numbers[0] += 1
        case 1:
            storage.append_on_end(random.randint(0, 50))
            numbers[1] += 1
        case 2:
            storage.remove_ind(random.randint(0, storage.get_length()))
            numbers[2] += 1
        case 3:
            tmp = random.randint(0, 50)
            if storage.index(tmp):
                storage.remove_val(tmp)
            numbers[3] += 1
        case 4:
            storage.get_with_delete((random.randint(0, storage.get_length())))
            numbers[4] += 1


def print_res(numbers):
    print("c0 =", numbers[0])
    print("c1 =", numbers[1])
    print("c2 =", numbers[2])
    print("c3 =", numbers[3])
    print("c4 =", numbers[4])


def menu1(storage, numbers):
    for iterator in range(100):
        rand_func(storage, numbers)
    print_res(numbers)


def menu2(storage, numbers):
    for iterator in range(1000):
        rand_func(storage, numbers)
    print_res(numbers)


def menu3(storage, numbers):
    for iterator in range(10000):
        rand_func(storage, numbers)
    print_res(numbers)


def menu(storage, numbers):
    print("Сколько итераций выполнить?\n1.100\n2.1000\n3.10000\n4.Вывести данные\nTo exit the program press Ctrl+D\n")
    choice = int(input())
    if 0 < choice < 5:
        match choice:
            case 1:
                start = time.time()
                menu1(storage, numbers)
                end = time.time() - start
                print(end)
            case 2:
                start = time.time()
                menu2(storage, numbers)
                end = time.time() - start
                print(end)
            case 3:
                start = time.time()
                menu3(storage, numbers)
                end = time.time() - start
                print(end)
            case 4:
                print(storage)


def main():
    numbers = array.array('i', [0, 0, 0, 0, 0, 0])
    storage = Storage(100)
    for iterator in range(0, 100):
        storage.append_on_end(random.randint(0, 1000))
    while True:
        menu(storage, numbers)


def test(storage):
    choice = int(input("1.append on begin\n2.append on ending\n3.remove index\n4.remove val\n5.get with del\n6.print\n7.index"))
    match choice:
        case 1:
            storage.append_on_beginning(int(input()))
        case 2:
            storage.append_on_end(int(input()))
        case 3:
            storage.remove_ind(int(input()))
        case 4:
            storage.remove_val(int(input()))
        case 5:
            storage.get_with_delete(int(input()))
        case 6:
            print(storage)
        case 7:
            print(storage.index(int(input())))


if __name__ == '__main__':
    storage = Storage(100)
    while True:
        test(storage)
