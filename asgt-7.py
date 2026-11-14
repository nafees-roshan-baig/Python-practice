# 1.Create a list with 5 fruits and print it.
x=["apple","banana","kiwi","orange","grape"]
print(x)
# 2.From the list ["pen", "pencil", "eraser", "sharpener"], print the first and last items.
x=["pen", "pencil", "eraser", "sharpener"]
print(x[0],x[3])
# 3.Given colors = ["red", "green", "blue", "yellow"], print the last item using negative indexing.
colors = ["red", "green", "blue", "yellow"]
print(colors[-1])
# 4.Write a program to check if "apple" exists in the list fruits = ["mango", "banana", "apple"].
fruits = ["mango", "banana", "apple"]
print("apple" in fruits)
# 5.Replace "banana" with "grapes" in the list ["apple", "banana", "cherry"].
x=["apple", "banana", "cherry"]
x[1]="grapes"
print(x)
# 6.Replace the 2nd and 3rd items in ["dog", "cat", "rabbit", "parrot"] with "cow" and "goat".
x=["dog", "cat", "rabbit", "parrot"]
x[1:3]=["cow","goat"]
print(x)
# 7.Insert "pineapple" at index 1 in the list ["apple", "banana", "cherry"].
x=["apple", "banana", "cherry"]
x.insert(1,"pineapple")
print(x)
# 8.Extend the list fruits = ["apple", "banana"] with another list ["mango", "orange"].
fruits = ["apple", "banana"]
x=["mango", "orange"]
fruits.append(x)
print(fruits)
# 9.Remove "carrot" from the list ["potato", "carrot", "onion"].
x=["potato", "carrot", "onion"]
x.pop(1)
print(x)
# 10.Pop the second element from ["apple", "banana", "cherry", "mango"].
x = ["apple", "banana", "cherry", "mango"]
x.pop(1)
# 11.Write a program to clear all items from a list of numbers.
x = ["apple", "banana", "cherry", "mango"]
x.clear()
print(x)
# 12.Using a for loop, print each element from the list ["java", "python", "c++"].
x=["java", "python", "c++"]
for i in x:
    print(i)
# 13.Print all elements from ["rose", "lotus", "lily"] using a while loop.
x=["rose", "lotus", "lily"]
i=0
while i < len(x):
    print(x[i])
# 14.Sort the list [45, 12, 89, 33, 5] in ascending and descending order.
x = [45, 12, 89, 33, 5]
x.sort()
print(x)
# 15.From the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], create a new list with only even
# numbers using list comprehension.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [i for i in x if i % 2 == 0]
print(even)
