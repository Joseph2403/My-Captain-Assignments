nterms = int(input("How many terms of Fibonacci Series do you want? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci series upto",str(nterms)+":")
   print(n1)

else:
   print("Fibonacci series upto",str(nterms)+":")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
