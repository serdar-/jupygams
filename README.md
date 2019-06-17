# jupygams
jupygams is a Python package for running GAMS scripts in Jupyter notebook. It allows user to see the logs in the output. Currenly it does not support syntax highlighting.

## Usage 
First, you need to have a valid GAMS installation and GAMS executable should be in your system path. To activate `%%gams` magic commmand you need to import jupygams first:

```python
import jupygams
```

Then you can run your GAMS script as follows:
```gams
%%gams

* My GAMS script
set i /1*10/;
parameter x(i);

```

Currently it is under development, please report the issues.

## TODO
- Add `setup.py` for allowing package to be installed.

