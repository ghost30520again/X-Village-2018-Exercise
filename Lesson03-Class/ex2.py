class Map():
    
    matrix = []
    
    def set_map(self,n):
        self.map = n+1
               
    def set_pattern(self,p):
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
                    
my_map = Map()

my_map.set_map(5)

my_map.set_pattern(1)

my_map.display()