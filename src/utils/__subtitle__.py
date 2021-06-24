"""
This script will do all subtitle corrections

"""

import pandas
from pathlib import Path
import re

from __utils__ import replace_word


def remove_legend(audio_name):
    # Example: audio_name = [A1_M0401_RIP_8660]
    string = '\[' + audio_name + '\]'

    regex_expression = rf"(?<={string})[\n]+([^\n]+)"

    for file in Path('src/content/legend').glob('*.TXT'):

        # Read file
        with open(f'{file}', 'r') as f:
            filedata = f.read()

            # If the readed file have the `audio_name`
            # then apply the regex replace and rewrite file
            if audio_name in filedata:
                filedata = re.sub(pattern = regex_expression,
                                  repl = '\n{}',
                                  string = filedata)

                with open(f'{file}', 'w') as f:
                    f.write(filedata)

#dataframe = pandas.read_csv('src/legend_changes.csv', sep = ',')
#dataframe = dataframe.query("modified_text == '*remover*'")
#audio_name_list = dataframe['audio_name'].tolist()
#for audio_name in audio_name_list:
#    remove_legend(legend_code = audio_name)
