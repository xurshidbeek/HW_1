# __iter__, __next__, __add__, __sub__, __eq__


# range(x) => start = 0, stop = x lekin x kirmaydi, step = 1   => range(1, 20)
# range(x, y) => start = x, stop = y lekin y kirmaydi, step = 1
# range(x, y, z) => start = x, stop = y lekin y kirmaydi, step = z

class CloneRange:
    def __init__(self, start, stop= None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step

        else:
            self.stop = stop
            self.start = start - step
            self.step = step

    def __iter__(self):
        print("Call iter")
        return self

    def __next__(self):
        print("call next item")
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration
        return self.start

for i in CloneRange(5, 20):
    print(i)
