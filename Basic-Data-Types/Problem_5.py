-- Problem: Lists
--Platform: HackerRank
--Difficulty: Easy

Question: Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

N = int(input())
lst = []

for _ in range(N):
    command = input().split()

    if command[0] == "insert":
        lst.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(lst)
    elif command[0] == "remove":
        lst.remove(int(command[1]))
    elif command[0] == "append":
        lst.append(int(command[1]))
    elif command[0] == "sort":
        lst.sort()
    elif command[0] == "pop":
        lst.pop()
    elif command[0] == "reverse":
        lst.reverse()
