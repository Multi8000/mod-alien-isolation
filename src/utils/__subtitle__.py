"""
This script will do all subtitle corrections

"""

from typing import Union, List
from pathlib import Path
import re


def replace_word(replacements: dict[str, str]) -> None:
    """
    Input:
    ------
    dict = {
        'old_word': 'new_word'
    }

    Example:
    --------
    dict = {
        'cat': 'CAT'
    }
    """

    for file in Path('src/content/legend').glob('*.TXT'):
        # Read file
        with open(f'{file}', 'r', encoding = 'utf-16') as f:
            filedata = f.read()

            # Replacements
            for replacement in replacements.items():
                regex_expression = re.compile(pattern = rf"\b{replacement[0]}\b")

                filedata = re.sub(pattern = regex_expression,
                                  repl = replacement[1],
                                  string = filedata)

                # Rewrites file with the changes
                with open(f'{file}', 'w', encoding = 'utf-16') as f:
                    f.write(filedata)


def replace_sentence(audio_name: Union[List[str], str], new_sentence: str) -> None:

    if isinstance(audio_name, str):
        audio_name_list = list()
        audio_name_list.append(audio_name)

    if isinstance(audio_name, list):
        audio_name_list = list(audio_name)

    for audio_name in audio_name_list:
        audio_name_string = '\[' + audio_name + '\]'
        regex_expression = rf"(?<={audio_name_string})[\n]+([^\n]+)"

        for file in Path('src/content/legend').glob('*.TXT'):
            # Read file
            with open(f'{file}', 'r', encoding = 'utf-16') as f:
                filedata = f.read()

                # If the readed file have the `audio_name`
                # then apply the regex replace and rewrite file
                if audio_name in filedata:
                    new_filedata = re.sub(pattern = regex_expression,
                                          repl = f'\n{{{new_sentence}}}',
                                          string = filedata)

                    # Rewrites file with the changes
                    with open(f'{file}', 'w', encoding = 'utf-16') as f:
                        f.write(new_filedata)


def remove_subtitle(audio_name: Union[List[str], str]) -> None:

    if isinstance(audio_name, str):
        audio_name_list = list()
        audio_name_list.append(audio_name)

    if isinstance(audio_name, list):
        audio_name_list = list(audio_name)

    for audio_name in audio_name_list:
        audio_name_string = '\[' + audio_name + '\]'
        regex_expression = rf"(?<={audio_name_string})[\n]+([^\n]+)"

        for file in Path('src/content/legend').glob('*.TXT'):
            # Read file
            with open(f'{file}', 'r', encoding = 'utf-16') as f:
                filedata = f.read()

                # If the readed file have the `audio_name`
                # then apply the regex replace and rewrite file
                if audio_name in filedata:
                    filedata = re.sub(pattern = regex_expression,
                                      repl = '\n{}',
                                      string = filedata)

                    # Rewrites file with the changes
                    with open(f'{file}', 'w', encoding = 'utf-16') as f:
                        f.write(filedata)


def punctuation_full_stop():
    regex_expression = r"\{([^\{\}]*)\}"

    for file in Path('src/content/legend').glob('*.TXT'):

        if Path(file).stem != 'UI':
            # Read file
            with open(f'{file}', 'r', encoding = 'utf-16') as f:
                filedata = f.read()

                matches = re.finditer(pattern = regex_expression, string = filedata)

                for match in matches:
                    print(match)

                    filedata = re.sub(pattern = regex_expression,
                                      repl = f'{{{match.group(1)}.}}',
                                      string = filedata)

                # Rewrites file with the changes
                with open(f'{file}', 'w', encoding = 'utf-16') as f:
                    f.write(filedata)
