from datetime import date
from engine.engine_in_use import EngineInUse


class CarFactory:
    _brand = 'BMW'
    _produced_cars_number = 0

    class Car:
        def __init__(self, type, model, color, engine: EngineInUse):
            self.type = type
            self.model = model
            self.color = color
            self.engine = engine
            self.win_code = self._generate_win_code()
            self._new_car_produced()

        def _generate_win_code(self):
            """
            Win code is generated as a "A-B-CCCC-DD-EEEEEEE"-string, where
            A is the first letter of type,
            B - first letter of the color,
            CCCC - year,
            DD - month,
            EEEEEEE - unique number.
            """
            today = date.today()
            return f'''{self.type[0]}-
                    {self.color[0]}-
                    {today.year}-
                    {f'0{today.month}'[-2:]}-
                    {f'00000{self.engine.unique_number}'[-6:]}'''

        @property
        @classmethod
        def brand(cls):
            return cls._brand

        @classmethod
        def _new_car_produced(cls):
            cls._produced_cars_number += 1

        @staticmethod
        def get_more_mileage_car(car1, car2):
            if (car1.engine.current_engine_mileage
                    >= car2.engine.current_engine_mileage):
                return car1
            else:
                return car2
