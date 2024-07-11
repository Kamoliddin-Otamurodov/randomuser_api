from requests import get
from pprint import pprint

url = "https://randomuser.me/api/"
pprint(get(url).status_code)