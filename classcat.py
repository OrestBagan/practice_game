class Cat:
    def __init__(self, age):
        self.age = age
        self.value_speed = self._set_average_speed()
        self.saturation_level = 30

    def _increase_saturation_level(self, value):
        self.saturation_level = self.saturation_level + value
        if self.saturation_level > 100:
            self.saturation_level = 100
        return self.saturation_level

    def _reduce_saturation_level(self, value):
        self.saturation_level = self.saturation_level - value
        if self.saturation_level < 0:
            self.saturation_level = 0
        return self.saturation_level

    def eat(self, product):
        if product == "корм":
            self._increase_saturation_level(10)
        elif product == "apple":
            self._increase_saturation_level(5)
        elif product == "молоко":
            self._increase_saturation_level(2)

    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        elif 7 < self.age <= 10:
            return 9
        elif self.age > 10:
            return 6

    def implementation(self, hours):
        kmhours = self.value_speed * hours
        if hours <= 25:
            self._reduce_saturation_level(2)
        elif 25 < hours <= 50:
            self._reduce_saturation_level(5)
        elif 50 < hours <= 100:
            self._reduce_saturation_level(15)
        elif 100 < hours <= 200:
            self._reduce_saturation_level(25)
        elif hours > 200:
            self._reduce_saturation_level(50)

        return f"Ваша кішка пробігла {kmhours} кілометрів"

    def get_saturation_level(self):
        if self.saturation_level == 0:
            return "Ваша кішка мертва :("
        return self.saturation_level

    def get_average_speed(self):
        return self.value_speed

Class = Cat(4)

print(f"Середня швидкість кішки: {Class.get_average_speed()} км/год")
print(f"Початковий рівень насичення: {Class.get_saturation_level()}")

Class.eat("корм")
print(f"Рівень насичення після їжі корму: {Class.get_saturation_level()}")

Class.eat("apple")
print(f"Рівень насичення після їжі яблука: {Class.get_saturation_level()}")

Class.eat("молоко")
print(f"Рівень насичення після їжі молока: {Class.get_saturation_level()}")

print(Class.implementation(10))
print(f"Рівень насичення після бігу: {Class.get_saturation_level()}")

