# start = 1
# end = 20  # Change this range as needed

# print("Even numbers:")
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num, end=" ")

# print("\nOdd numbers:")
# for num in range(start, end + 1):
#     if num % 2 != 0:
#         print(num, end=" ")

def factorial(n):
  if n<0:
    return "Error: n must be +ve "
  elif n==1:
    return 1
  else:
    return n*factorial(n)