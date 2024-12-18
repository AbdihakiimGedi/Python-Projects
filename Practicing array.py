#Practicing array lists
name=["Abdihakiin","Socdaal","Maxamed","Cali"]
#print(name[0])

#print(len(name))

#for a in name:
  #  print(a)

#using for range
#for  b in range(len(name)):
 #   print("Waa ku salaamay",name[b])
    #print("---------------------------")
#Adding elemnt lists we use two metods
#Method1 append
#name.append("Saabir")
#for c in range(len(name)):
   # print(name[c])

#We can use insert method that we add every position we want to add new elemnt
    #print("---------------------")
#name.insert(0,"Maxamed daahir")
#for d in range(len(name)):
    #print(name[d])
#We use two different method to remove elemnt in our list
#Method 1 pop  it remove the elemnt in last and it take index that you want delete
#name.pop()
#for a in name:
   # print(a)
#Using pop with indx
#name.pop(1)
#for a in name:
 #   print(a)

#Using remove method it remove the value and it take ethe value#
#name.remove("Abdihakiin")
#name.remove("Socdaal")
#name.remove("Maxamed")
#for a in range(len(name)):
 #   print(name[a])
#Concatinating two arrays we use extend method
list1=[2,4,6,8,9,12,15,17,19,20]
list2=[1,3,5,7,8,6,4,12,13,45,67,87]
list1.extend(list2)
for a in list1:
    print(a,end="\t")

