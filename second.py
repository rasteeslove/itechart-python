from engine.engine_factory import EngineFactory
from car.car_factory import CarFactory


def demo():
    ef = EngineFactory()
    cf = CarFactory()

    e1 = ef.get_engine('as is', model_name='V8',
            number_of_cylinders=8, engine_displacement=5.5,
            engine_resource=150000, fuel_type='diesel')
    print(e1.info())
    print('\n\n')

    e2 = ef.get_engine('for use', model_name='840d xDrive MHT Auto',
            number_of_cylinders=6, engine_displacement=2.993,
            engine_resource=200000, fuel_type='diesel',
            current_engine_mileage=100)
    print(e2.info())
    print('\n\n')

    e2.increase_mileage(5000)
    print(e2.info())
    print(e2.resource_mileage_diff)
    print('\n\n')

    c1 = cf.get_car(type='Coupe', model='8 Series M Sport 4dr',
            color='Black', engine=e2)
    e3 = ef.get_engine('for use', model_name='Porsche 911 engine',
            number_of_cylinders=6, engine_displacement=2.981,
            engine_resource=200000, fuel_type='diesel',
            current_engine_mileage=2000)
    c2 = cf.get_car(type='Sports car', model='Porsche 911 Carrera',
            color='Black', engine=e3)

    print(CarFactory.Car.brand)
    print(CarFactory.Car.produced_cars_number)
    print('\n\n')

    print(CarFactory.Car.get_more_mileage_car(c1, c2).model)

if __name__ == '__main__':
    demo()
