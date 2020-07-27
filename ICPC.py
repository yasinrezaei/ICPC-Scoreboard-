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
for i in range(len(combined_list)):
    for j in range(i,len(combined_list)):
        if(int(combined_list[i][2])<int(combined_list[j][2])):
            # #-----------------
            # temp_rank=combined_list[i][0]
            # combined_list[i][0]=combined_list[j][0]
            # combined_list[j][0]=temp_rank
            # #-------------------
            temp=combined_list[i]
            combined_list[i]=combined_list[j]
            combined_list[j]=temp
        if(int(combined_list[i][2])==int(combined_list[j][2])):
            if(int(combined_list[i][3])<int(combined_list[j][3])):
                
                temp=combined_list[i]
                combined_list[i]=combined_list[j]
                combined_list[j]=temp
            else:
                if(ord(combined_list[i][1][0])>ord(combined_list[j][1][0])):
                   
                    temp=combined_list[j]
                    combined_list[j]=combined_list[i]
                    combined_list[i]=temp
#set rank-----------------------                   
for i in range(len(combined_list)):
    combined_list[i][0]=i+1
#-----------------------
combined_file=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - Combined.html","w")
sb1=open("C:\\Users\\ROYAL_SYSTEM\\Desktop\\ICPC\\ICPC Scoreboard - 1.html")
line=sb1.readline()
while(line):
    if("var rows" in line):
        combined_file.write("var rows  ="+str(combined_list)+";\n")
    else:
        combined_file.write(line)
    line=sb1.readline()


        
        



    