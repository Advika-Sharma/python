#import pandas as pd

#data=pd.read_csv('matches.csv')
#print(data.head())
#which team has won the most matches
#won_count=data['winner'].value_counts()
#won_count=data['winner'].value_counts()
#won_count=data['winner'].value_counts()
#print("team with the most wins:")
#print(won_count.head(1))

#calculating the avg winner for matches with a result 
#result_matches=data[data['result'] == 'normal']
#avg_win_margin=result_matches['result_margin'].mean()
#print("The average margin by runs for matches with a result:",avg_win_margin)

#print("Descriptive Statistics:")
#print(data.describe())

#winner_count=data['winner'].value_counts()
#print(winner_count.head(1))



import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli, binom, poisson, expon, norm, uniform

p=0.3 #probability of sucess
rv_bernoulli=bernoulli(p)
outcome=rv_bernoulli.rvs(size=1000)
print("bernoulli outcomes:", outcome)
print("probability of sucess(p):",p)
print("empirical probability of sucess:", np.mean(outcome))


#plotting the PMF of a Binomial Distribution
n=10
p=0.5
rv_binomial=binom(n,p)
x=np.arange(0,n+1)
pmf_binomial=rv_binomial.pmf(x) #probability of mass function
plt.bar(x,pmf_binomial)
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Sucess")
plt.ylabel("Probability")
#plt.show()


#Stimulating a poission Process 
lambda_=2
rv_poisson=poisson(mu=lambda_)
outcomes=rv_poisson.rvs(size=1000)
print("poisson outcomes:", outcomes)
print("probability of sucess(p):",lambda_)
print("empirical probability of sucess:", np.mean(outcomes))
