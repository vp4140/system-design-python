class Car:
    def __init__(self, engine, wheels, sunroof=False, color="White"):
        self.engine = engine
        self.wheels = wheels
        self.sunroof = sunroof
        self.color = color

    def __str__(self):
        return f"Car(engine={self.engine}, wheels={self.wheels}, sunroof={self.sunroof}, color={self.color})"


class CarBuilder:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels
        self.sunroof = False
        self.color = "White"

    def set_sunroof(self, sunroof):
        self.sunroof = sunroof
        return self  # Enables method chaining

    def set_color(self, color):
        self.color = color
        return self  # Enables method chaining

    def build(self):
        return Car(self.engine, self.wheels, self.sunroof, self.color)


# Example usage
if __name__ == "__main__":
    car = CarBuilder("V8", 4).set_sunroof(True).set_color("Red").build()
    print(car)
