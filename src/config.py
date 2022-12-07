import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

# load enviorment variables
env_path = 'src/.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """
    Set configuration vars from .env file
    """

    # Load in environment variables
    # These fields are associated with logger
    LOG_DIR = os.getenv('LOG_DIR')
    LOG_FILE = os.getenv('LOG_FILE')
    LOG_FORMAT = os.getenv('LOG_FORMAT')
    # These fields are associated with redmine
    PROJECTS = os.getenv('PROJECTS').split(',')
    YEAR = os.getenv('YEAR')
    MONTH = os.getenv('MONTH')
    DAY = os.getenv('DAY')
    URL = os.getenv('URL')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    START_DATE = os.getenv('START_DATE')
    TIMES_FILE = os.getenv('TIMES_FILE')