v1=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - 1.html")
s = v1.readline()
while(s):
    if("var rows " in s):
        List=s
    s = v1.readline() 
z=List[14:len(List)-2]
   
l=eval(z)
for i in l:
    print(i[1])
    print("-----------------")


    