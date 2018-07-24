from lib.stack import Stack

s = Stack()

def dec_to_bin(dec):
    while dec >0 :
        s.push(dec%2)
        dec = (dec//2)
    
    for i in range(s.size()):   
        print(s.pop(),end="")
    
#dec_to_bin(41)  # 回傳 101001
dec_to_bin(100)  # 回傳 1100100
