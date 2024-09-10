import multiprocessing as mp
import time
import math

a = []
b = []
c = []

def make_calc_one(numbers):
  for number in numbers:
    a.append(math.sqrt(number **3))

def make_calc_two(numbers):
  for number in numbers:
    b.append(math.sqrt(number **4))

def make_calc_three(numbers):
  for number in numbers:
    c.append(math.sqrt(number **5))

# ya que las funciones son independientes, se pueden realizar por separado

if __name__ == '__main__':
  lista = list(range(5000000))

  p1 = mp.Process(target=make_calc_one, args=(lista,))
  p2 = mp.Process(target=make_calc_two, args=(lista,))
  p3 = mp.Process(target=make_calc_three, args=(lista,))

  start = time.time()

  p1.start()
  p2.start()
  p3.start()

  end = time.time()

  print(end-start)

  start = time.time()

  make_calc_one(lista)
  make_calc_two(lista)
  make_calc_three(lista)

  end = time.time()

  print(end-start)

