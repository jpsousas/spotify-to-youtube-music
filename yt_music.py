import json
import os
from dotenv import load_dotenv

load_dotenv()

# Get .json snippet
with open('browser.base.json', 'r') as f:
    data = json.load(f)

# Acess the cookie property
data['cookie'] = os.getenv("YOUTUBE_COOKIE")
with open('browser.json', 'w') as file:
    json.dump(data, file)
