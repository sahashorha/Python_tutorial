thislist = ["apple","banana","orange"]
# print(thislist)
# if you want find the type of list 
mylist = ["apple", " banana","rahul"]
# print(type(mylist));
# List is the collection which is ordered and changeable.Allows duplicate number 

# Tuple is the collection which is ordered and unchangeable 
#  Set is collection which is unordered and unchangeable and unindexed.No duplicate 
# Dictionary is collection which is ordered and changeable. No duplicate members

# Negative indexing give the element from the last 
thislist = ["apple","banana","cherry"];
# if "apple" in thislist:
      # print("Yes, 'apple' is in the fruits list");
# if "orange" not in thislist:
      # print("Yes 'Orange' is not in the list")

# Access item
anotherList = ["running", "pushups","plank"];
# print(anotherList[:])
# it changes the value 
anotherList[1] = "jogging";
# print(anotherList);
anotherList[1:2] =["exercise"];
# print(anotherList);

anotherList.insert(2,"yoga");
# print(anotherList);

# append items
anotherList.append("apple");
# print(anotherList);

# remove list -> remove particular element which passing throught parenthesis
anotherList.remove("apple");
# print(anotherList)

# pop -> pop the last element always 
anotherList.pop();
# print(anotherList);

# loop list 
# for x in anotherList:
      # print(x);
# for i in range(len(anotherList)):
      # print(anotherList[i])

i = 0;
while i < len(anotherList):
      # print(anotherList[i]);
      i+=1;
fruits = ["apple","banana","cherry","kiwi"]
newlist = []
for x in fruits :
      if "a" in x:
            newlist.append(x);
print(newlist);