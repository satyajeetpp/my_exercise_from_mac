class deque:
    def __init__(self) -> None:
        self.l=[]
    def inserte(self,data):
        self.l.insert(0,data)
    def inseite(self,data):
        self.l.append(data)
    def delrer(self):
        self.l.pop(0)
    def delfront(self):
        self.l.pop()

    def view(self):
        m=[]
        for e in self.l:
            m.append(e)
        print(m) 
    

c=deque()
c.inserte(15)
c.inserte(150)
c.inserte(1)
c.inseite(35)
c.inseite(350)
c.inseite(3)
c.delfront()
#c.delrer()
c.view()