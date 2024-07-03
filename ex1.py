class Kassa(object):
    __cash = 0

    def __init__ (self, start_cash):    #Конструктор
        self.__cash = start_cash

    def count_1000(self):               #count_1000() - выводит сколько целых тысяч осталось в кассе
        print(f"{self.__cash // 1000} целых тысяч в кассе")

    def top_up(self,x):                 #top_up(X) - пополнить на X
        self.__cash += x

    def take_away(self, x):             #take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
        cash = self.__cash - x
        if cash <= 0:
            print("Недосаточно денег.")
            self.count_1000()
        else:
            self.__cash = cash

#Несколько примеров для проверки задания :)

kassa = Kassa(17800)
kassa.count_1000()

kassa.top_up(13900)
kassa.count_1000()

kassa.take_away(24900)
kassa.count_1000()