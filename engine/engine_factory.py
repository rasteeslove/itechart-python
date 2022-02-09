from engine.engine import Engine
from engine.engine_in_use import EngineInUse


class EngineFactory:
    def get_engine(self, type, *args):
        if type == 'as is':
            return Engine(*args)
        elif type == 'for use':
            return EngineInUse(*args)
        else:
            raise ValueError(type)
