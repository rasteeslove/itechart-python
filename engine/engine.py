class Engine:
    """
    This class describes an engine object.
    """
    def __init__(self, model_name, number_of_cylinders,
            engine_displacement, engine_resource, fuel_type):
        self.model_name=model_name
        self.number_of_cylinders=number_of_cylinders
        self.engine_displacement=engine_displacement
        self.engine_resource=engine_resource
        self.fuel_type=fuel_type

    def info(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('__') and not callable(k)}
