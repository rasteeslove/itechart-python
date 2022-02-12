from file_manipulator.file_manipulator import FileManipulator
import os


def demo_write():
    # 1: getting the filename:
    print('Note: if file doesn\'t exist \'.demo\' '
          'will be appended to the name.')
    filename = input('Enter filename/full path '
                     'of the file to write to: ')

    if not os.path.isfile(filename):
        filename += '.demo'

    # 2: asking whether to overwrite or to append:
    mode = None
    while mode != 'w' and mode != 'a':
        mode = input('Overwrite/append? [w/a]: ')

    # 3: getting the input:
    print('Enter the text (Ctrl-D to stop the input): ')
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    text = '\n'.join(lines)

    # 4: writing:
    with FileManipulator.open(filename, mode) as f:
        f.write(text)


def demo_read():
    # 1: getting the filename:
    filename = input('Enter filename/full path '
                     'of the file to read from: ')

    # 2: reading:
    with FileManipulator.open(filename, 'r') as f:
        contents = f.read()

    # 3: printing:
    print(contents)


def demo():
    choice = None
    while choice != 'r' and choice != 'w':
        choice = input('Read/write? [r/w]: ')

    if choice == 'r':
        demo_read()
    else:
        demo_write()


if __name__ == '__main__':
    demo()
