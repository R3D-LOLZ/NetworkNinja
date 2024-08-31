# run.py
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import and run the main function from NetworkNinja.py
from NetworkNinja import main_function

if __name__ == "__main__":
    main_function()
