class team:
    def __init__(self, l = []):
        self.l = l
    def newMember(self,names):
        for i in names:
            self.l.append(i)
    def showMembers(self):
        return self.l
t1 = team(['x','y','z'])
t1.newMember(['as','fr','kr'])
print(t1.showMembers())