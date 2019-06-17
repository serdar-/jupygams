import os
from subprocess import Popen, PIPE
import logging
from distutils.spawn import find_executable
from IPython.core.magic import Magics, magics_class, line_cell_magic
import time


logging.basicConfig(format='@> %(levelname)s - %(message)s')

@magics_class
class GamsRunner(Magics):

    def __init__(self, shell):
        # You must call the parent constructor
        super(GamsRunner, self).__init__(shell)
        self._logger = logging.getLogger("GamsRunner")
        self.gams_path = None

    def find_gams_path(self):

        self.gams_path = find_executable("gams")
        if self.gams_path is None:
            self._logger.error("Cannot find GAMS in the path!")
            return False
        else:
            return True

    @line_cell_magic
    def gams(self, line, cell=None):
        if self.find_gams_path():
            if cell is not None:
                path = 'tmp.gms'
                with open(path, 'w') as f:
                    f.write(cell)
                arguments = line.split()
                print(arguments)
                print(self.gams_path)
                p = Popen([self.gams_path, path] + arguments, stdout=PIPE,stderr=PIPE,shell=False)
                (output, err) = p.communicate()
                p_status = p.wait()
                print(output)
                print(err)
                os.unlink(path)
                # return line,cell
            else:
                self._logger.warning("Empty GAMS program.")
        # return line, cell
