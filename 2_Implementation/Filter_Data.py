import pandas as pd
derrick_rose_tenure = list(range(2009,2023))

for year in derrick_rose_tenure:
    raw_df = pd.read_csv("2_Implementation/2_Season_DF/Season_{}.csv".format(year))

    raw_df.drop(raw_df.index[raw_df['Rk'] == 'Rk'], inplace=True) #To remove the unnecessary headers in the table

    # Remove instances of out of order values to make data more general
    def normalise_row(row):
        if row['MP'] == 'Did Not Play':
            return "No"
        if row['MP'] == 'Inactive':
            return "No"
        if row['MP'] == 'Did Not Dress':
            return "No"
        if row['MP'] == 'Not With Team':
            return "No"
        else:
            return "Yes"
    raw_df['Game Played'] = raw_df.apply(lambda row : normalise_row(row), axis=1) 
    
    raw_df.loc[raw_df["MP"] == "Did Not Play","MP"]= "00:00" # Replace with time related Minutes played
    raw_df.loc[raw_df["MP"] == "Inactive","MP"] = "00:00"
    raw_df.loc[raw_df["MP"] == "Did Not Dress","MP"] = "00:00"
    raw_df.loc[raw_df["MP"] == "Not With Team","MP"] = "00:00"
    

    raw_df[['Match Result','Points']] = raw_df['Unnamed: 7'].str.split('(', n=1, expand=True) # To split the match results and points in the columnm
    raw_df["Points"] = raw_df["Points"].str.strip(")")
    
    raw_df[["Minutes Played","Seconds Played"]] = raw_df["MP"].str.split(":",expand=True)
    

    raw_df.drop(['Unnamed: 0','Rk','G','Age','Unnamed: 5','Unnamed: 7','MP'],axis=1,inplace=True) # Drop all unnecessry columns

    

    raw_df.to_csv("2_Implementation/2_Season_DF/Filtered_Season_{}.csv".format(year))

