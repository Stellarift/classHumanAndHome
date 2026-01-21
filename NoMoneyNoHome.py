# Часть 1: Класс Human
class Human:
    default_name = "Иван"
    default_age = 25

    def default_info(self):
        print(f"Имя по умолчанию: {Human.default_name}")
        print(f"Возраст по умолчанию: {Human.default_age}")

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"\n--- Информация о {self.name} ---")
        print(f"Возраст: {self.age}")
        print(f"Деньги: {self.__money} руб.")
        if self.__house:
            print(f"Дом: {self.__house.area} м² (куплен за {self.__house.price} руб.)")
        else:
            print("Дом: нет")

    def earn_money(self, amount):
        self.__money += amount
        print(f"{self.name} заработал {amount} руб.")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print(f"Покупка совершена! Куплен дом за {price} руб.")

    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            return True
        else:
            needed = final_price - self.__money
            print(f"Недостаточно денег! Нужно еще {needed:.2f} руб.")
            return False


# Часть 2: Класс House
class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount):
        return self.price * (100 - discount) / 100


# Часть 3: Класс SmallHouse
class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


# Часть 4: Выполнение
if __name__ == "__main__":
    print("Информация по умолчанию для класса Human:")
    Human().default_info()
    
    person = Human("Алексей", 30)
    print(f"\nСоздан человек: {person.name}")
    
    person.info()
    
    small_house = SmallHouse(5000000) 
    print(f"\nСоздан дом площадью {small_house.area} м² за {small_house.price:,} руб.".replace(",", " "))
    
    print(f"\n{person.name} пытается купить дом со скидкой 10%:")
    if not person.buy_house(small_house, 10):
        print(f"\n{person.name} решает заработать денег...")
        person.earn_money(10000000)
        
        print(f"\n{person.name} снова пытается купить дом:")
        person.buy_house(small_house, 10)
    

    person.info()