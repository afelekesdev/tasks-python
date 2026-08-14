
num = int(input('digite um numero: '))
tot = 0
for i in range(1, num + 1):   
   if num % i == 0:
      print("\033[32m", end="")
      tot += 1  
   else:
      print("\033[91m", end="")     
   print('{} '.format(i), end='')
print("\n\033[mO numero {} foi divisivel {} vezes.".format(num, tot))
if tot == 2:
   print('o numero é primo')
else:
   print("ele não é primo!!!")
   
 