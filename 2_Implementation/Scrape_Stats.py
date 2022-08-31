import requests
from bs4 import BeautifulSoup
import pandas as pd

derrick_rose_tenure = list(range(2009,2023))
start_url = "https://www.basketball-reference.com/players/r/rosede01/gamelog/{}"

for year in derrick_rose_tenure:
    url = start_url.format(year)
    data = requests.get(url)
    with open("2_Implementation/1_Season_HTML/Season_{}.html".format(year),"w+",encoding="utf-8") as f:
        f.write(data.text)

for year in derrick_rose_tenure:
    with open("2_Implementation/1_Season_HTML/Season_{}.html".format(year),encoding="utf-8") as f:
        page = f.read()
        soup = BeautifulSoup(page,"html.parser")
        season_stats = soup.find(id="pgl_basic")

    season_stats_df = pd.read_html(str(season_stats))[0]
    season_stats_df.to_csv("2_Implementation/2_Season_DF/Season_{}.csv".format(year))