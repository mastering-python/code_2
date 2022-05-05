import sys
import pathlib

# Little hack to add the current directory to sys.path so we can
# find the imports
path = pathlib.Path(__file__).parent
sys.path.append(str(path.resolve()))
