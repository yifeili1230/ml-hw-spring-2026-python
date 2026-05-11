class DataProcessor:
    def __init__(self):
        self.data = []

    def insert(self, number):
        self.data.append(number)

    def search(self, x):
        if x in self.data:
            return self.data.index(x) + 1
        return -1