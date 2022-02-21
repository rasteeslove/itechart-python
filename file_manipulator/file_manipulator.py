import os


class FileManipulator:
    """
    This class wraps around the built-in 'open', 'write',
    and 'read' functions.
    """

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    @staticmethod
    def open(filename, mode='r'):
        if mode != 'r' and mode != 'w' and mode != 'a':
            raise ValueError('The mode is not valid.')

        return FileManipulator(filename, mode)

    def __enter__(self):
        self.stream = open(self.filename, self.mode)
        return self

    def read(self):
        if self.mode != 'r':
            raise ValueError('The action is not valid '
                             'for the selected mode')
        
        return self.stream.read()

    def write(self, text: str):
        if self.mode != 'w' and self.mode != 'a':
            raise ValueError('The action is not valid '
                             'for the selected mode')

        self.stream.write(text)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stream.close()
