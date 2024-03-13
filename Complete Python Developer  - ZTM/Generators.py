# Generators are a simple way to create iterators using functions. You can also create iterators using classes, but generators are much easier to work with.

range(100)
list(range(100))


def maek_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = maek_list(100)
print(my_list)


#

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


# Fibonancci Num

def fin(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fin(10):
    print(x)
