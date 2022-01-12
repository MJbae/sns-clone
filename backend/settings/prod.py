import os
from dotenv import load_dotenv
from .common import *

load_dotenv(verbose=True)

STATICFILES_STORAGE = "backend.storages.StaticAzureStorage"
DEFAULT_FILE_STORAGE = "backend.storages.MediaAzureStorage"

DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

AZURE_ACCOUNT_NAME = os.getenv("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_ACCOUNT_KEY")
