import os
from dotenv import load_dotenv
from os.path import join, dirname
from pathlib import Path  # python3 only

# load enviorment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    """
    Set configuration vars from .env file
    """

    # Load in environment variables
    # These fields are associated with logger
    LOG_DIR = os.getenv('LOG_DIR')
    LOG_FILE_PREFIX = os.getenv('LOG_FILE_PREFIX')
    LOG_FILE_SUFFIX = os.getenv('LOG_FILE_SUFFIX')
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
    TIMES_FILE_PREFIX = os.getenv('TIMES_FILE_PREFIX')
    TIMES_FILE_SUFFIX = os.getenv('TIMES_FILE_SUFFIX')