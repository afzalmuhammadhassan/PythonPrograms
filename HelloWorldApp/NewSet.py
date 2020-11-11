from _ast import Raise


class NewSet(object):
    def __init__(self):
        self.val = []

    def insert(self, e):
        if e not in self.val:
            self.val.append(e)

    def remove(self, e):
        try:
            self.val.remove(e)
        except:
            raise ValueError('Not Found')

    def member(self, e):
        return e in self.val

    def intersect(self, other):
        result = NewSet()
        for e in self.val:
            if other.member(e):
                result.insert(e)
        return result

    def __str__(self):
        self.val.sort()
        return '{ ' + ','.join(str(e) for e in self.val) + ' }'

    def __len__(self):
        return len(self.val)
