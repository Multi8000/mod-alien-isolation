from pathlib import Path


def make_directory(path):
    Path(path).mkdir(parents = True, exist_ok = True)


def replace_word(old_word, new_word):
    for file in Path('src/content/legend').glob('*.TXT'):

        # Read file
        with open(f'{file}', 'r') as f:
            filedata = f.read()

        # Replace word
        filedata = filedata.replace(old_word, new_word)

        # Write modified file
        with open(f'{file}', 'w') as f:
            f.write(filedata)
