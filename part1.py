
# Online Python - IDE, Editor, Compiler, Interpreter

f = open("input.txt", "r")
big=0;
sum=0;
while True :
    l = f.readline();
    if (l not in ['\n', '\r\n']) :
        print ("number ", l);
        sum=sum+ int(l);
        print ("sum ", sum);
    else :
        big = big if big>sum else sum;
        sum = 0;
    print ("big ", big);
