print("enter time :",end="")
T=int(input())

#------------------------
sb1=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - 1.html")

line= sb1.readline()
while(line):
    if("var rows " in line):
        var_list=line
    line = sb1.readline() 
L=var_list[14:len(var_list)-2]
List1=eval(L)

#----------------------------------------
sb2=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - 2.html")
line= sb2.readline()
while(line):
    if("var rows " in line):
        var_list=line
    line = sb2.readline() 
L=var_list[14:len(var_list)-2]
 
List2=eval(L)
#-------------------------------------------
combined_list=List1+List2
#---------------------if not in time--------------
for i in range(5,17):
    for j in range(len(combined_list)):
            if(type(combined_list[j][i])==list):
                s=combined_list[j][i][0].split('/')
                if(s[1]!='--' and int(s[1])>T):
                    s[1]='--'
                    combined_list[j][i][0]=s[0]+'/'+s[1]
                    combined_list[j][i][1]='no'
#-------------set yes first------------------------
for i in range(5,17):

    yes_first=T
    index=0
    l=[]
    
    for j in range(len(combined_list)):
        if(type(combined_list[j][i])==list):
            s=combined_list[j][i][0].split('/')
            if(combined_list[j][i][1]=='yes first' and int(s[1])<yes_first):
                yes_first=int(s[1])
                index=j
    combined_list[index][i][1]='yes first'
    for j in range(len(combined_list)):
        if(type(combined_list[j][i])==list):
            s=combined_list[j][i][0].split('/')
            if(combined_list[j][i][1]=='yes first' and int(s[1])>yes_first):
                combined_list[j][i][1]='yes'
#---------------------------penalti------------------------------
for i in range(len(combined_list)):
    p=0
    for j in range(5,17):
        if(type(combined_list[i][j])==list ):
            s=combined_list[i][j][0].split('/')
            if(s[1]!="--"):
                a=int(s[0])
                t=int(s[1])
                p+=t+(a-1)*20
    combined_list[i][3]=p

#------------------------set rank-----------------------
for i in range(len(combined_list)):
    for j in range(i,len(combined_list)):
        if(int(combined_list[i][2])<int(combined_list[j][2])):
            #--------------------
            temp_rank=combined_list[i][0]
            combined_list[i][0]=combined_list[j][0]
            combined_list[j][0]=temp_rank
            #---------------------
            temp=combined_list[i]
            combined_list[i]=combined_list[j]
            combined_list[j]=temp
        if(int(combined_list[i][2])==int(combined_list[j][2])):
            if(int(combined_list[i][3])>int(combined_list[j][3])):
                
                temp=combined_list[i]
                combined_list[i]=combined_list[j]
                combined_list[j]=temp
            elif(int(combined_list[i][3])==int(combined_list[j][3])): 
                 
                if(ord(combined_list[i][1][0])>ord(combined_list[j][1][0])):
                    
                    temp=combined_list[j]
                    combined_list[j]=combined_list[i]
                    combined_list[i]=temp
                   
for i in range(len(combined_list)):
    combined_list[i][0]=i+1

for i in range(len(combined_list)):
    for j in range(i,len(combined_list)):
        if(combined_list[i][2]==combined_list[j][2] and combined_list[i][3]==combined_list[j][3]):
            combined_list[j][0]=combined_list[i][0]
            

combined_file=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - Combined.html","w")
sb1=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - 1.html")
line=sb1.readline()
while(line):
    if("var rows" in line):
        combined_file.write("var rows  ="+str(combined_list)+";\n")
    else:
        combined_file.write(line)
    line=sb1.readline()


        
        



    