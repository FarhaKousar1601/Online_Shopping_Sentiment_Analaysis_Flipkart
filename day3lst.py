list1 =[1,2,3,4,5,6,7,8,9]
list2 = ["Zubida","Ismail","Zainba","Muhammed","Almas","Ayesha","Misba","Farha"]
print(list1)
print(list2)      #print list1&list2

print(len(list1))
print(len(list2)) #length of list 1 and list2

print(list1[-1])
print(list2[-1])  #last element of list1 & list2

print(list1[0])
print(list2[0])   #Access the first element of list1 & list2

print(list2[-5:-4]) #negative indexing middle word of the list2

list2[3] = "uppa"
print(list2)        #change the middle value of the list2

list1.insert(5,12)
list2.insert(5,"Syed")
print("Updated list1:", list1)  
print("Updated list2:", list2)  #Insert value at the 5th index of the lists


list1.append(14)
list2.append("Family")
print(list1)
print(list2)    #Append function add value at end of lists

list1.remove(6)
list2.remove("Syed")
print(list1)
print(list2)     #remove functionof any value


