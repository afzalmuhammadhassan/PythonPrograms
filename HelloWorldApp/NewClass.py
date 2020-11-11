class Cooardinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '< ' + str(self.x) + ', ' + str(self.y) + ' >'

    def __sub__(self, other):
        s_dic_x = (self.x - other.x) ** 2
        s_dic_y = (self.y - other.y) ** 2
        return (s_dic_x - s_dic_y) ** 0.5