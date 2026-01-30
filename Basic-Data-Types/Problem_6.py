-- Problem: Tuples
--Platform: HackerRank
--Difficulty: Easy

Question: Given an integer,n and n space-separated integers as input, create a tuple,n , of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))
