#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23608428"))
API_HASH = environ.get("API_HASH", "ff78b5440b4cd922b7810fe28abadb73")
BOT_TOKEN = environ.get("BOT_TOKEN", "7991080001:AAEhU1qRwQMLDoxObHnIps0DITZSoOoNdgE")

OWNER = int(environ.get("OWNER", "7435785216"))
CREDIT = environ.get("CREDIT", "FLAME X MASTER")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7435785216').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7435785216').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
