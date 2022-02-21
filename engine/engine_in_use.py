from random import randint

from engine.engine import Engine


class EngineInUse(Engine):

    def __init__(self, model_name, number_of_cylinders,
            engine_displacement, engine_resource, fuel_type,
            current_engine_mileage=0, unique_number=randint(0, 999999)):
        super().__init__(model_name, number_of_cylinders,
            engine_displacement, engine_resource, fuel_type)
        self.current_engine_mileage = current_engine_mileage
        self.unique_number = unique_number

    def increase_mileage(self, km_number):
        self.current_engine_mileage += km_number

    @property
    def resource_mileage_diff(self):
        return self.engine_resource - self.current_engine_mileage
