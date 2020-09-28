import py2plpy
import re
import sys

def main():
    if len(sys.argv) > 2:
        of = sys.argv[2]
    else:
        of = re.sub(r'\.py$', r'.sql', sys.argv[1])
    with open(of, 'w') as file:
        file.write(py2plpy.transform(sys.argv[1]))