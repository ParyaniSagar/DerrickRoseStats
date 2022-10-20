import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://developers.google.com/public-data/docs/canonical/states_csv"

data = requests.get(url)
with open("2_Implementation/1_Season_HTML/LatLon.html","w+", encoding="utf-8") as f:
    f.write(data.text)

with open("2_Implementation/1_Season_HTML/LatLon.html", encoding="utf-8") as f:
    page = f.read()
    soup = BeautifulSoup(page,"html.parser")
    season_stats = soup.find("div", {"class": "devsite-table-wrapper"})

season_stats_df = pd.read_html(str(season_stats))
season_stats_df.to_csv("2_Implementation/3_Final_Dataset/LatLon.csv")