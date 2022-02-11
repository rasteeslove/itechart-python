import os


def demo_write():
    mode = 'w'

    print('Note: if file doesn\'t exist \'.demo\' '
          'will be appended to the name.')
    filename = input('Enter filename/full path '
                     'of the file to write to: ')

    # 1: checking if the file exists:
    if os.path.isfile(filename):
        # a.1: checking if the os allows writing to it:
        if not os.access(filename, os.W_OK):
            print(f'Cannot write to {filename}. Permission denied.')
            return
        # a.2: asking whether to overwrite or to append
        # if the file is not empty:
        if os.path.getsize(filename) > 0:
            choice = None
            while choice != 'o' and choice != 'a':
                choice = input('Overwrite/append? [o/a]: ')
            if choice == 'a':
                mode = 'a'
    else:
        # b.1: checking if the os allows creating it:
        # (that means checking 'w' permission for its directory)
        dirpath = os.path.dirname(filename)
        if not dirpath:
            dirpath = './'
        if not os.access(dirpath, os.W_OK):
            print(f'Cannot create file in {dirpath}. Permission denied.')
            return
        filename += '.demo'

    # 2: getting the input to write to file:
    print('Enter the text (Ctrl-D to stop the input): ')
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    text = '\n'.join(lines)

    # 3: writing to file:
    try:
        with open(filename, mode) as f:
            f.write(text)
    except:
        print('Something went wrong while writing to file!')
    finally:
        print('Finished writing!')


def demo_read():
    filename = input('Enter filename/full path '
                     'of the file to read from: ')

    # 1: checking if the os allows reading the file:
    if not os.access(filename, os.R_OK):
        print(f'Cannot read {filename}. Permission denied.')
        return

    # 2: checking if the file exists:
    if not os.path.isfile(filename):
        print('The file doesn\'t exist!')
        return

    # 3: reading the file:
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except:
        print('Something went wrong while reading file!')
        return
    finally:
        print('Finished reading!')
    
    print(contents)


if __name__ == '__main__':
    demo_read()
