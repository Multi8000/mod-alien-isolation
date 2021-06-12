from subprocess import (run, PIPE)
from pathlib import Path

from __utils__ import make_directory


help = '''
This script will be used to rebuild .PCK or .BNK

- Extract the content (.WEM and .DAT) from .PCK and .BNK
- Generate a .TXT file with:
    . internal file name
    . offset
    . size in bytes

Input example: input_path = 'src/temp/original/banks'
'''


class Extract():

    def __init__(self):
        self.rscanner_path = 'src/tools/RavioliGameTools/RScannerConsole.exe'
        self.input_path = 'src/temp/original/banks'
        self.output_path = 'src/temp/extracted'


    def generate_internal_file_name_list(self, input_path):

        files_list = [file for file in Path(input_path).glob('*') if file.is_file()]

        for file in files_list:
            if Path(file).suffix in ['.BNK', '.PCK']:

                self.file_name = Path(file).stem

                make_directory(path = f'{self.output_path}/{self.file_name}')

                output_path = Path(f'{self.output_path}/{self.file_name}/{self.file_name}.txt')

                script = f'''"{self.rscanner_path}" "{file}" /list > "{output_path}"'''
                script_output = run(args = script, stderr = PIPE, shell = True)


    def extract_from_pck_bnk(self, input_path):

        files_list = [file for file in Path(input_path).glob('*') if file.is_file()]

        for file in files_list:
            if Path(file).suffix in ['.BNK', '.PCK']:

                self.file_name = Path(file).stem
                output_path = Path(f'{self.output_path}/{self.file_name}')

                script = f'''"{self.rscanner_path}" "{file}" /extract:"{output_path}" /unknowns'''
                script_output = run(args = script, stderr = PIPE, shell = True)
