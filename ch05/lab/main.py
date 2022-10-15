import pygame

def sequence(n):
  count = 0
  while n != 1:
    print(n)
    if n % 2 == 1:
      n = n * 3 + 1
    else: 
      n = n//2
    count += 1

  print(n)
  print(f"The count is {count}")
  
def solution(n):
  while n != 1:
    if n % 2 == 0: 
      n = n / 2
    else: 
      n = n * 3 + 1

iter = {}
upper_limit = 20

for i in range(2, upper_limit + 1):
  iter[i] = solution(i)

sequence(101)
print(iter)

#part c to be done via resubmission (please)
