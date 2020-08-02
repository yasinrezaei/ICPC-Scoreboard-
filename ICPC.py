#-----------------menu----------------
print("Enter first Scoreboard file name:",end="")
first_scoreboard=input()
print("Enter second Scoreboard file name:",end="")
second_scoreboard=input()
print("Enter Combined Scoreboard file name:",end="")
combined_scoreboard=input()
print("enter time :",end="")
T=int(input())

#----------------open scoreboards-----------------------
sb1=open(first_scoreboard,"r")
sb2=open(second_scoreboard,"r")
#-----------------read lines from first scoreboard------
line= sb1.readline()
while(line):
    if("var rows " in line):
        var_list=line
    line = sb1.readline() 
L=var_list[14:len(var_list)-2]
List1=eval(L)

#-----------------read lines from second scoreboard------
line= sb2.readline()
while(line):
    if("var rows " in line):
        var_list=line
    line = sb2.readline() 
L=var_list[14:len(var_list)-2]
 
List2=eval(L)
#--------------------------------------------------------
for i in range(5,17):
    for j in range(len(List1)):
        if(type(List1[j][i])==list):
            if(List1[j][i][1]=='no'):
                List1[j][i]=0
            else:
                s=List1[j][i][0].split('/')
                if(int(s[1])>T):
                    List1[j][i]=0
#-------------------create combined list of 2 scoreboards----
combined_list=List1+List2
#---------------------if not in time------------------------
for i in range(5,17):
    for j in range(len(combined_list)):
            if(type(combined_list[j][i])==list):
                s=combined_list[j][i][0].split('/')
                if(s[1]!='--' and int(s[1])>T):
                    s[1]='--'
                    combined_list[j][i][0]=s[0]+'/'+s[1]
                    combined_list[j][i][1]='no'
                   
#---------------------set yes first--------------------------
for i in range(5,17):
    yes_first=T
    index=0
    for j in range(len(combined_list)):
        if(type(combined_list[j][i])==list):
            s=combined_list[j][i][0].split('/')
            if(combined_list[j][i][1]=='yes first' and int(s[1])<yes_first):
                yes_first=int(s[1])
                index=j
    if(type(combined_list[index][i])==list):
        combined_list[index][i][1]='yes first'
    for j in range(len(combined_list)):
        if(type(combined_list[j][i])==list):
            s=combined_list[j][i][0].split('/')
            if(combined_list[j][i][1]=='yes first' and s[1]!="--" and int(s[1])>yes_first ):
                combined_list[j][i][1]='yes'
#---------------------------penalty------------------------------
for i in range(len(combined_list)):
    penalty=0
    for j in range(5,17):
        if(type(combined_list[i][j])==list ):
            s=combined_list[i][j][0].split('/')
            if(s[1]!="--" and (combined_list[i][j][1]=='yes' or combined_list[i][j][1]=='yes first')):
                a=int(s[0])
                t=int(s[1])
                penalty+=t+(a-1)*20
    combined_list[i][3]=penalty
#--------------------------------------solved----------------------
for i in range(len(combined_list)):
    solved=0
    for j in range(5,17):
        if(type(combined_list[i][j])==list ):
            s=combined_list[i][j][0].split('/')
            if(s[1]!="--" and (combined_list[i][j][1]=='yes' or combined_list[i][j][1]=='yes first')):
                solved+=1
        
    combined_list[i][2]=solved

#--------------------------------------------------------------------

#sort by count of solvedproblems --> penalty --> alphabet

for i in range(len(combined_list)):
    for j in range(i,len(combined_list)):
        if(int(combined_list[i][2])<int(combined_list[j][2])):

            temp_rank=combined_list[i][0]
            combined_list[i][0]=combined_list[j][0]
            combined_list[j][0]=temp_rank

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
#------------------------set rank------------------------------
for i in range(len(combined_list)):
    combined_list[i][0]=i+1

for i in range(len(combined_list)):
    for j in range(i,len(combined_list)):
        if(combined_list[i][2]==combined_list[j][2] and combined_list[i][3]==combined_list[j][3]):
            combined_list[j][0]=combined_list[i][0]
#------------------------create combined file --------------------

combined_file=open(combined_scoreboard,"w")
sb1=open(first_scoreboard,"r")
line=sb1.readline()
while(line):
    if("var rows" in line):
        combined_file.write("var rows  ="+str(combined_list)+";\n")
    else:
        combined_file.write(line)
    line=sb1.readline()