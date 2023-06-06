from pathlib import Path
import tempfile
import traceback
import json
import sys
import os


try:
    port = 45
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = 27068247
    api_hash = "d63399ee39e1c901565fb85ef547c6e7"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = "{"index_all": false,"index_private": true,"index_group": false,"index_channel": true,"exclude_chats": [],"include_chats": []}"
    index_settings = json.loads(index_settings_str)
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = "AQGdB1cAtWMiirqlWECNDb7QpX9yGr6ztZAm0rYRTp0GpcQcOVj0ugl9J7VK3NHQnY2bqSY-hwoni_ZJBWQWk_Sy8EsQOXSnTAPVx2Wsxz3YrPVJO5cUSmtEOVQO2UADjwfHpnripLuYVSgMZS4bRioIupZuai1DOkAYsaSbf3UbtZq9k2jrVial-H-vAamAGAwEn0j_qPzkMj4jWbP-kxqzIzWcxqXzmKh5CRLvx-Eq0FA9SZP15XwG0cD1-EyB1ySHd7d78ctRJ8QNrZzPD7X3HZWcndjhvHp2PsrnyHM6Jr6Vb7P2hEMDMSuGZ9A_fNE9o7IA2paMeK82Y_b1CAMJwNVDqAAAAAE4EueVAA"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = False
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = os.environ.get("TGINDEX_USERNAME", "")
password = os.environ.get("PASSWORD", "")
SHORT_URL_LEN = int(os.environ.get("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.environ.get("SESSION_COOKIE_LIFETIME") or "60")
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""
