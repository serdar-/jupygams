from .jupygams import GamsRunner


def load_ipython_extension(ipython):
    ipython.register_magics(GamsRunner)