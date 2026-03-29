#Lists are mutable (can be changed)

myl  = ["Mohamed" , "Ahmed" , "Ali"]
l = ["a","test","zahwa"]

#any function modify in the list (deep copy)

l.extend(myl) #add myl to l
print(l)

z=myl+l  #concatenation
print(z)

print("zahwa" in myl)  #is that value exists in myl
print("zahwa" in l)

x = enumerate(l) #generate index for every element
print(x)
# for i , t in x:
#     print(f`{i} - {t}`)

items=["python","course","iti"]
newm = "_".join(items) #add separators between list items
print(newm)

message="Welcome to Python"
print(tuple(message)) # word -> separated characters

#tuples are immutable (can not be changed)
#Can not insert, append , pop , remove , reverse

unit=("item")
print(type(unit))


#ranges
r = range(5)
print(r)

for i in r:
    print(i)

rr = range(1, 10 , 2) #from 1 to 10 with 2 steps every iteration
print(list(rr)) # save in list

for i in rr:
    print(i)

#sets
#removing duplicates


#dictinories
# based on set , kwyword --> unique
#comma separated key value pair
#mutable data type

d={}
myd=dict()

info = {
    "name":"noha",
    "track":"python",
    "name":"zahwa"  #take last data as its interpreted language
}

print(info)

info['track']='.net'
print(info)

info['salary']=1000  #new info added to the dictionary
print(info)

# for item in info:
#     print(f`{item})

#get keys of dicts
info_keys = info.keys()
print(info_keys)

info_vals = info.values()
print(info_vals, type(info_vals))

#concatination in dicts
info1 = {
    "name":"noha",
    "track":"python",
}
info2 = {
    "course":"iti"
}

info1.update(info2)
print(info1)

print("noha" in info1) # default --> search for given value in keys
# how to search in values ?


