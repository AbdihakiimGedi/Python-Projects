#Practicing dictionary
person={
    "Name":"Abdihakiin gedi mohamed",
    "Tell":"613936588",
    "Address":"Heliwaa alcadaala",
    "Status":"Single",
    "Job":"Student in university",
    "University":"Jamhuuriya university technolgy and science",
    "Faculty":"IT department of computer application",
    "Semester":"Semester five",
    "Campus":"Campus two"
    }
#Printing values in dictionary
#for a in person.values():
 #   print(a)
 
#Printing keys in dictionary
#for b in person.keys():
 #   print(b)
# printing any value that we need in dictionar
#print(person["Name"])
#print(person["Tell"])
#print(person["Campus"])

#Updating our object values
#person.update({"Name":"Maryan daahir santuur"})
#person.update({"Tell":"615148393"})
#person.update({"Address":"Beledweyne Somalia"})
#for a in person.values():
 #   print(a)



#Example of dictionary
people={
"person1":{"Name":"Xamdi","Tell":"514231","Address":"Madiina"},
"person2":{"Name":"Cali","Tell":"51423","Address":"Kaxda"},
"person3":{"Name":"Maxamud","Tell":"51423","Address":"Karan"},
"person4":{"Name":"Muniiro","Tell":"51423","Address":"Waaberi"},
"person5":{"Name":"Najmo","Tell":"51423","Address":"Cabdicasiis"}
}
print("Name \t Tell \t Address ",end="\n")
for  x in people:
    vals=people[x].values()
    for y in vals:
        print(y,end="\t")
    print()
    
   
     
     
    
