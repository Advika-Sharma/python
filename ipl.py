import pandas as pd 
cricket_data=pd.read_csv('matches.csv')


#print(cricket_data)
#print(cricket_data.head())
#Aggregation
#total_run_per_match=cricket_data.groupby('id')['target_runs'].agg(['sum','mean','max','min'])
#print(total_run_per_match)

#Grouping
#avg_win_per_city=cricket_data.groupby('city')['target_runs'].max()
#print(avg_win_per_city)

#aggregation with multiple columns 
#total runs and overs summary
#runs_overs_summary=cricket_data.groupby('id').agg({'target_runs':'sum','target_overs':'max'})
#print(runs_overs_summary)

#grouping with the multiple colums 
#avg_target_runs_season_city=cricket_data.groupby(['season','city'])['target_runs'].mean()
#print(avg_target_runs_season_city)

#boolean indexing -> filter rows based on conditions
#filter matches where the target runs was greater than >200
#high_runs_match=cricket_data[cricket_data['target_runs']<200]
#print(high_runs_match)

#find matches where the toss winner and the match winner were the same team 

#same_winner=cricket_data.query('toss_winner == winner')
#print(same_winner)
#same_winner.to_csv("same_winner.csv")
#print("data saved sucessfully")


#query -> find the matches where the win margin was grerater than 200 and the toss decision was to bat 

#match_sol=cricket_data[(cricket_data['target_runs']>20) & (cricket_data['toss_decision'] == 'bat')]
#print(match_sol)

pivot_table_runs=cricket_data.pivot_table(index='id',columns='team1',values='target_runs',aggfunc='sum')
print(pivot_table_runs)