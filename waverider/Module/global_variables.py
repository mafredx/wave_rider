"""
Wave Rider -- global_variables.py

    Module to store global variables across all modules.

Author: Mike Fredricks
Genesis: 2/13/22
"""
import os
import waverider.main as main


# Define global directories
main_directory = main.main_directory
resource_directory = os.path.join(main_directory, 'Resources')
log_directory = os.path.join(main_directory, 'Log')

# Global color codes
black = (0, 0, 0)
white = (255, 255, 255)
