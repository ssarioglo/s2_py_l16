import math
class Cherepashka(object):
    s = 1
    x = 0
    y = 0

    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def go_up(self):                        #go_up() - увеличивает y на s
        self.y += self.s
    def go_down(self):                      #go_down() - уменьшает y на s
        self.y -= self.s
    def go_left(self):                      #go_left() - уменьшает x на s
        self.x -= self.s
    def go_right(self):                     #go_right() - увеличивает x на s
        self.x += self.s
    def evolve(self):                       #evolve() - увеличивает s на 1
        self.s += 1
    def degrade(self):                      #degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if (self.s - 1) <= 0:
            print("Длина хода не может быть = 0.")
        else:
            self.s -= 1

#count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
    def count_moves(self, x2, y2):          
        dist = math.ceil((x2 - self.x)+(y2 - self.y) / self.s) # Расстояние до новой точки это разность между новыми и старыми координатами / S.
                                                               # округляю в большую сторону (если надо 4.1 хода то логично, что это 5)
        print(f"До точки {x2}:{y2} минимальное количество ходов - {dist}")

#Создаем объект Чарли
charley = Cherepashka(2,1)

print()


#Функции для проверки задания :)

#charley.evolve()
#charley.go_up()
#charley.go_down()
#charley.go_left()
#charley.go_right()
#charley.degrade()


print("x y s")
print(charley.x, charley.y, charley.s)

charley.count_moves(7,10)