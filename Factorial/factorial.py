# Factorial  recursive function
def recur_factorial(n):
  return 1 if (n == 1 or n == 0) else n * recur_factorial(n - 1)
 