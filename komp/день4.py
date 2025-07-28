import random
угадайка=random.randint(1,100)
попытки=5
for i in range(попытки):
 чешка=int(input('угадай'))
 if чешка==угадайка:
  print('молодец')
  exit()
 elif чешка>угадайка:
  print('меньше')
 if чешка<угадайка:
  print('больше')
print('хаха ты проиграл')
