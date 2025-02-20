# The Target Interface (Expected by the client)
class AmericanSocket:
    def provide_power(self):
        return "Providing 110V power"


# The Adaptee (Incompatible interface)
class EuropeanPlug:
    def provide_eu_power(self):
        return "Providing 220V power"


# The Adapter (Converts EuropeanPlug to work with AmericanSocket)
class Adapter(AmericanSocket):
    def __init__(self, european_plug):
        self.european_plug = european_plug

    def provide_power(self):
        return f"Adapter converts: {self.european_plug.provide_eu_power()} to 110V"


# Client Code
if __name__ == "__main__":
    eu_plug = EuropeanPlug()
    adapter = Adapter(eu_plug)

    print(adapter.provide_power())  # Output: Adapter converts: Providing 220V power to 110V
