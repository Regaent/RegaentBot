import os
from dotenv import load_dotenv
load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN")
gis_token = os.getenv("gis_token")
gis_project_cx = os.getenv("gis_cx")
Bot_Version = '1.1.0.0' # Major.Minor.Release.Build