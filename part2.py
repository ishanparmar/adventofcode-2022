
# Online Python - IDE, Editor, Compiler, Interpreter
import time

start = time.time();
f = open("input.txt", "r")
big=[];
sum=0;
for l in f:
    if (l not in ['\n', '\r\n']) :
        print ("number ", l);
        sum=sum + int(l);
        #print ("sum ", sum);
    else :
        big.append(sum);
        sum = 0;
big.sort();    
big.reverse();
print("ans ", big[0]+big[1]+big[2]);
print (time.time()-start);
    
    
