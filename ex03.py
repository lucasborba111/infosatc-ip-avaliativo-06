def rotation():
    number = int(input("posição"))
    list_1 = [1,2,3,4]
    list_2 = []
    if(number<0):
       list_2.append(list_1[number])
       del list_1[number]
       list_2 = list_2+list_1
       print(list_2)
    elif(number>=0):
       list_2.append(list_1[number])
       del list_1[number]
       list_2=list_1+list_2
       print(list_2)
rotation()
