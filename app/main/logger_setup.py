#Created pn 08-Aug-2024
# Author Bharath Shanmugasundaram

import logging
import sys

def setup_logger():
    
    # Create a custom logger
    logger = logging.getLogger('AppLogger')
    # Create handlers
    file_handler = logging.FileHandler('app.log', mode='a')
    stdout_handler = logging.StreamHandler(sys.stdout)

    # Set logging level for handlers
    file_handler.setLevel(logging.DEBUG)
    stdout_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    
    return logger

# Initialize the logger
logger = setup_logger()


