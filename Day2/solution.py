file = open("Day2/input.txt",'r')
lines=file.readlines()
safeLevel=0
for line in lines:
    list=line.split()
    int_list  = [int(x) for x in list]
    for i in range(len(int_list)-1):
        if int_list[1]>int_list[0]:
            while i<len(int_list)-1:
                if abs(int_list[i+1]-int_list[i]<1) or abs(int_list[i+1]-int_list[i]>3):
                    break
                i+=1
        if int_list[1]<int_list[0]:
            while i<len(int_list)-1:
                if abs(int_list[i+1]-int_list[i]<1) or abs(int_list[i+1]-int_list[i]>3):
                    break
                i+=1
        if int_list[0] == int_list[1]:
            break
        safeLevel+=1
    print (safeLevel)