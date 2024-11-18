import logging
from pathlib import Path

# Globals variables for the project
PROJECT_PATH = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_PATH / 'src'
APP_PATH = SRC_PATH / 'francophonia'

DOCS_PATH = PROJECT_PATH / 'docs'
BUILD_PATH = PROJECT_PATH / 'site'

# Set the logger for the project
logger = logging.getLogger("francophonia")
