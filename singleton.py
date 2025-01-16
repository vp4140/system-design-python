class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance :
            print("Here")
            cls.instance = super().__new__(cls)
        return cls.instance


    def __init__(self,value):
        self.value = value


singleton1 = Singleton("First Instance")
print(singleton1.value)  # Output: First Instance

singleton2 = Singleton("Second Instance")
print(singleton2.value)  # Output: First Instance (singleton2 is the same instance as singleton1)

# Verifying both are the same instance
print(singleton1 is singleton2)  # Output: True

