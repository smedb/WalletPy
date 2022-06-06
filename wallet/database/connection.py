global memory_db
memory_db = {}


class Database:
    def __init__(self, model):
        global memory_db

        if model not in memory_db.keys():
            memory_db[model] = []

        self.objects = memory_db[model]

    def getAll(self):
        return self.objects

    def create(self, obj):
        self.objects.append(obj)

    def search(self, key, value):
        for i in self.objects:
            if (getattr(i, key) == value):
                return i

        return None

    def delete(self, obj):
        for i in self.objects:
            if (i == obj):
                self.objects.remove(i)
