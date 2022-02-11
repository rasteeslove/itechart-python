from engine.engine import Engine
from engine.engine_in_use import EngineInUse


class EngineFactory:
    def get_engine(self, type, *args, **kwargs):
        if type == 'as is':
            return Engine(*args, **kwargs)
        elif type == 'for use':
            return EngineInUse(*args, **kwargs)
        else:
            raise ValueError(type)
