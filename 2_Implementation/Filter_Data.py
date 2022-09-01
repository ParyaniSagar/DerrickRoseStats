import pandas as pd
derrick_rose_tenure = list(range(2009,2023))

for year in derrick_rose_tenure:
    raw_df = pd.read_csv("2_Implementation/2_Season_DF/Season_{}.csv".format(year))
    raw_df.drop(raw_df.index[raw_df['Rk'] == 'Rk'], inplace=True) #To remove the unnecessary headers in the table
    raw_df[['Match Result','Points']] = raw_df['Unnamed: 7'].str.split('(', n=1, expand=True) # To split the match results and points in the columnm
    raw_df["Points"] = raw_df["Points"].str.strip(")")
    raw_df.head(5)
    raw_df.drop(['Unnamed: 0','Rk','G','Age','Unnamed: 5','Unnamed: 7'],axis=1,inplace=True) # Drop all unnecessry columns
    
    raw_df.to_csv("2_Implementation/2_Season_DF/Season_{}.csv".format(year))

