
# Првое задание
import math

def get_triangle_type(a, b, c):
 """Определяет вид треугольника по длинам сторон.

 Args:
  a: Длина первой стороны.
  b: Длина второй стороны.
  c: Длина третьей стороны.

 Returns:
  Строку, содержащую тип треугольника:
   "Равносторонний"
   "Равнобедренный"
   "Разносторонний"
 """

 if a == b == c:
  return "Равносторонний"
 elif (a == b) or (a == c) or (b == c):
  return "Равнобедренный"
 else:
  return "Разносторонний"

def calculate_area(a, b, c):
 """Вычисляет площадь треугольника по формуле Герона.

 Args:
  a: Длина первой стороны.
  b: Длина второй стороны.
  c: Длина третьей стороны.

 Returns:
  Площадь треугольника.
 """

 # Полупериметр треугольника
 s = (a + b + c) / 2
 # Формула Герона
 area = math.sqrt(s * (s - a) * (s - b) * (s - c))
 return area

def main():
 """Ввод данных и вывод результата."""

 while True:
  try:
   a = float(input("Введите длину первой стороны: "))
   b = float(input("Введите длину второй стороны: "))
   c = float(input("Введите длину третьей стороны: "))

   # Проверка возможности построения треугольника
   if not (a + b > c and a + c > b and b + c > a):
    print("Невозможно построить треугольник с такими сторонами!")
    continue

   triangle_type = get_triangle_type(a, b, c)
   area = calculate_area(a, b, c)

   print(f"Тип треугольника: {triangle_type}")
   print(f"Площадь треугольника: {area:.2f}")

   break # Выход из цикла после успешного ввода
  except ValueError:
   print("Некорректный ввод. Введите числовые значения.")

if __name__ == "__main__":
 main()






# Второе задание
 
 import math

def get_triangle_type(a, b, c):
 """Определяет вид треугольника по длинам сторон.

 Args:
  a: Длина первой стороны.
  b: Длина второй стороны.
  c: Длина третьей стороны.

 Returns:
  Строку, содержащую тип треугольника:
   "Остроугольный"
   "Тупоугольный"
   "Прямоугольный"
 """

 # Сортировка сторон по возрастанию
 a, b, c = sorted([a, b, c])

 # Проверка на прямоугольный треугольник
 if a**2 + b**2 == c**2:
  return "Прямоугольный"

 # Проверка на остроугольный треугольник
 if a**2 + b**2 > c**2:
  return "Остроугольный"

 # Если не прямоугольный и не остроугольный, то тупоугольный
 return "Тупоугольный"

def calculate_area(a, b, c):
 """Вычисляет площадь треугольника по формуле Герона.

 Args:
  a: Длина первой стороны.
  b: Длина второй стороны.
  c: Длина третьей стороны.

 Returns:
  Площадь треугольника.
 """

 s = (a + b + c) / 2
 area = math.sqrt(s * (s - a) * (s - b) * (s - c))
 return area

def main():
 """Ввод данных и вывод результата."""

 while True:
  try:
   a = float(input("Введите длину первой стороны: "))
   b = float(input("Введите длину второй стороны: "))
   c = float(input("Введите длину третьей стороны: "))

   # Проверка возможности построения треугольника
   if not (a + b > c and a + c > b and b + c > a):
    print("Невозможно построить треугольник с такими сторонами!")
    continue

   triangle_type = get_triangle_type(a, b, c)
   area = calculate_area(a, b, c)

   print(f"Тип треугольника: {triangle_type}")
   print(f"Площадь треугольника: {area:.2f}")

   break # Выход из цикла после успешного ввода
  except ValueError:
   print("Некорректный ввод. Введите числовые значения.")

if __name__ == "__main__":
 main()
