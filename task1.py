from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("vehicle.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


# Абстрактний клас Vehicle
class Vehicle(ABC):
    """Абстрактний базовий клас для всіх транспортних засобів."""

    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        """Запустити двигун транспортного засобу."""
        pass


# Конкретні класи транспортних засобів
class Car(Vehicle):
    """Клас для автомобілів."""

    def start_engine(self) -> None:
        """Запустити двигун автомобіля."""
        logger.info(
            "%s %s (%s): Двигун автомобіля запущено", self.make, self.model, self.spec
        )


class Motorcycle(Vehicle):
    """Клас для мотоциклів."""

    def start_engine(self) -> None:
        """Запустити мотор мотоцикла."""
        logger.info("%s %s (%s): Мотор мотоцикла заведено", self.make, self.model, self.spec)


# Абстрактна фабрика транспортних засобів
class VehicleFactory(ABC):
    """Абстрактна фабрика для створення транспортних засобів."""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        """Створити автомобіль."""
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Створити мотоцикл."""
        pass


# Фабрики для регіонів
class USVehicleFactory(VehicleFactory):
    """Фабрика для створення транспортних засобів для US."""

    def create_car(self, make: str, model: str) -> Car:
        """Створити автомобіль для US."""
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Створити мотоцикл для US."""
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    """Фабрика для створення транспортних засобів для EU."""

    def create_car(self, make: str, model: str) -> Car:
        """Створити автомобіль для EU."""
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Створити мотоцикл для EU."""
        return Motorcycle(make, model, "EU Spec")


if __name__ == "__main__":
    # Використання фабрик
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Створення американських транспортних засобів
    us_car = us_factory.create_car("Ford", "Mustang")
    us_car.start_engine()
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Street 750")
    us_motorcycle.start_engine()

    # Створення європейських транспортних засобів
    eu_car = eu_factory.create_car("BMW", "X5")
    eu_car.start_engine()
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1200")
    eu_motorcycle.start_engine()
