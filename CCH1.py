from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.engine = None
        self.seats = None
        self.trip_computer = None
        self.gps = None

    def __str__(self):
        return (f"Car(engine={self.engine}, seats={self.seats}, "
                f"trip_computer={self.trip_computer}, gps={self.gps})")

class CarBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_seats(self, seats):
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer):
        pass

    @abstractmethod
    def set_gps(self, gps):
        pass

    @abstractmethod
    def get_result(self):
        pass

# ConcreteBuilder
class ConcreteCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()

    def set_engine(self, engine="V8"):
        self._car.engine = engine
        return self  # Permite chamadas encadeadas

    def set_seats(self, seats=5):
        self._car.seats = seats
        return self

    def set_trip_computer(self, trip_computer=True):
        self._car.trip_computer = trip_computer
        return self

    def set_gps(self, gps=True):
        self._car.gps = gps
        return self

    def get_result(self):
        car = self._car
        self.reset()  
        return car

class Director:
    def __init__(self, builder: CarBuilder):
        self._builder = builder

    def construct_sports_car(self):
        self._builder.reset()
        self._builder.set_engine("V12").set_seats(2).set_trip_computer(True).set_gps(True)
        return self._builder.get_result()

    def construct_family_car(self):
        self._builder.reset()
        self._builder.set_engine("V6").set_seats(7).set_trip_computer(False).set_gps(True)
        return self._builder.get_result()

if __name__ == '__main__':
    builder = ConcreteCarBuilder()
    director = Director(builder)

    sports_car = director.construct_sports_car()
    family_car = director.construct_family_car()

    print("Carro Esportivo:", sports_car)
    print("Carro Familiar:", family_car)
