import random

N = 4


def show(pole):
  for i in range(N):
    for j in range(N):
      print(str(pole[i * N + j]).rjust(N), end="")
    print()


def goPlayer(pole):
  flLoopInput = True
  while flLoopInput:
    x, y = input("Введите координату через пробел: ").split()
    if not x.isdigit() or not y.isdigit():
      print("Координаты введены неверно")
      continue

    x = int(x) - 1
    y = int(y) - 1

    if x < 0 or x >= N or y < 0 or y >= N:
      print("Координаты выходят за пределы поля")
      continue
    if pole[x * N + y] == 1 or pole[x * N + y] == 0:
      print("Клетка уже занята")
      continue

    flLoopInput = False
  return (x, y)


def goComputer(pole):
  rng = random.Random()
  flloopInput = True

  while flloopInput:
    x2 = rng.randrange(N)
    y2 = rng.randrange(N)
    if pole[x2 * N + y2] == 1 or pole[x2 * N + y2] == 0:
      continue
    flloopInput = False

  return (x2, y2)


def isStatus(pole):
  k = 1
  s = 0
  # Проверяет по всем строкам наличие 1 или 0
  for i in range(N):
    lst = pole[s:N * k]
    if 1 in lst and 0 in lst: continue
    if lst.count(1) == N: return N
    if lst.count(0) == N: return -N
    s = s + N
    k += 1

  # Проверяет по всем столбцам наличие 1 или 0
  k = 1
  for i in range(N):
    # lst = pole[i::N]
    lst = pole[i:N * k:N]
    if lst.count(1) == N: return N
    if lst.count(0) == N: return -N
    k += 1

  # Формируется список по главной диагонали элементов
  lst = pole[::N + 1]
  l = (N - 1) * N + 1
  # Формируется список по побочной диагонали элементов
  lstRe = pole[N - 1:l:N - 1]
  # Проверяется наличие 1 или 0 по главной диагонале
  if lst.count(1) == N: return N
  if lst.count(0) == N: return -N

  # Проверяется наличие 1 или 0 по побочной диагонале
  if lstRe.count(1) == N: return N
  if lstRe.count(0) == N: return -N

  # игра продолжается
  return -2


def isFinish(status):
  pass


def startGame():
  pole = [-2] * N * N
  finishState = isStatus(pole)
  while finishState == -2:
    show(pole)
    x, y = goPlayer(pole)
    pole[x * N + y] = 1
    # print((x, N, y), end=",")
    x2, y2 = goComputer(pole)
    pole[x2 * N + y2] = 0
    finishState = isStatus(pole)

  return finishState


res = startGame()
if res == N:
  print("Вы выиграли")
if res == -N:
  print("Вы проиграли")
print("Игра окончена")
