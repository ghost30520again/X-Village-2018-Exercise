class Shape:
   
    def set_edge(self, long):
        self.edge = long    
    def display(self):
        for i in range(self.edge+1):
            print('*'*i)     
            
        
x = Shape()
x.set_edge(6)
x.display()
