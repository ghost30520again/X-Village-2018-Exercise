class Map():
    
    matrix = []
    def __init__(self,n,p):
        self.map = n+1
               
        if  p !=1:
            for i in range(1,self.map):
                self.matrix.append([])
                for j in range(1,self.map):
                    self.matrix[i-1].append("*")
        else :
            for i in range(1,self.map):
                self.matrix.append([])
                for j in range(1,self.map):
                    self.matrix[i-1].append("*")
            c = int((self.map+1)/2)-1        
            
            self.matrix[c-1][c+1] = 0
            self.matrix[c-1][c] = 0
            self.matrix[c-1][c-1] = 0
            self.matrix[c][c-1] = 0
            self.matrix[c+1][c] = 0
                
    def display(self):
        for i in range(1,self.map):
            for j in range(1,self.map):
                print(self.matrix[i-1][j-1],end='')
            print("")
                    
my_map = Map(5,1)
my_map.display()