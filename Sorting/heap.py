class heap:
    def __init__(self,hlist = []):
        self.hlist = hlist
    def insert(self,ele):
        if self.hlist is None:
            self.hlist.append(ele)
        for i in self.hlist:
            if i > ele: