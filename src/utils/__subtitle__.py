"""
This script will do all subtitle corrections

"""

import pandas
from pathlib import Path
import re

from __utils__ import replace_word

def remove_legend(legend_code):
    files = list()

    for file in Path('src/content/legend').glob('*.TXT'):

        # Read file
        with open(f'{file}', 'r', encoding = 'utf-16') as f:
            if legend_code in f.read():
                files.append(file)

    return files

with open(f'src/content/legend/CUTSCENES.TXT', 'r', encoding = 'utf-16') as f:
    string = '\[A1_CUTSCENES_SAM_C0100_0004\]'
    exp = rf"{string}[\r\n]+([^\r\n]+)"
    print(exp)

    filedata = f.read()
    #print(filedata)

    print(re.search(exp, filedata).group())

