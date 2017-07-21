"""
Author: Jonas Lundblad @ http://www.github.com/jolny

Converts a list of .xls files to .xlsx using Libre Office in headless mode
If no files are specified, the command is run on all xls files in the cwd.
Same applies to running the script stand-alone without arguments.

Prerequisites: Python, Libre Office
"""

import subprocess # To execute libreoffice conversion
import glob # To get a list of all xls files in cwd

class LibreOfficeCoverter:

    bash_command = "libreoffice --headless --convert-to "

    def to_xlsx(self, verbose = False, files=[]):
        if not files:
            files = glob.glob('*.xls')

        for xls in files:
            print(xls+" >>> "+xls+"x ...")
            current_command = self.bash_command+"xlsx "+xls
            process = subprocess.Popen(current_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if verbose:
                print(output)

if __name__ == "__main__":
    import sys
    loc = LibreOfficeCoverter()
    loc.to_xlsx(files=sys.argv[1:])
