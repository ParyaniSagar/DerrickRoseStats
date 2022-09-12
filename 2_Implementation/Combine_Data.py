# To combine all the stats in Career Season.


import pandas as pd
derrick_rose_tenure = list(range(2009,2023))
dtype_dict = {'FG':'int', 'FGA':'int','FG%':'float', '3P':'int', '3PA':'int', '3P%':'float', 'FT':'int', 'FTA':'int', 'FT%':'float',
    'ORB':'int', 'DRB':'int', 'TRB':'int','AST':'int', 'STL':'int', 'BLK':'int', 'TOV':'int', 'PF':'int', 'PTS':'int', 'Minutes Played':'int'}

final_df = pd.DataFrame()
for year in derrick_rose_tenure:
    raw_df = pd.read_csv("2_Implementation/2_Season_DF/Filtered_Season_{}.csv".format(year))
    final_df = pd.concat([final_df,raw_df])

final_df.to_csv("2_Implementation/2_Season_DF/Derrick_Rose_All_Time_Stats.csv")

raw_df = pd.read_csv("2_Implementation/2_Season_DF/Derrick_Rose_All_Time_Stats.csv")
played_df = raw_df[raw_df['Game Played'] == "Yes"]
played_df.astype(dtype_dict)
played_df.to_csv("2_Implementation/2_Season_DF/Derrick_Rose_Playing_Time_Stats.csv")

