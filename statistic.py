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
#from scipy import stats
#import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
#import matplotlib.pyplot as plt 
#from scipy.stats import bernoulli, binom, poisson, expon, norm, uniform

#p=0.3 #probability of sucess
#rv_bernoulli=bernoulli(p)
#outcome=rv_bernoulli.rvs(size=1000)
#print("bernoulli outcomes:", outcome)
#print("probability of sucess(p):",p)
#print("empirical probability of sucess:", np.mean(outcome))


#plotting the PMF of a Binomial Distribution
#n=10
#p=0.5
#rv_binomial=binom(n,p)
#x=np.arange(0,n+1)
#pmf_binomial=rv_binomial.pmf(x) #probability of mass function
#plt.bar(x,pmf_binomial)
#plt.title("Binomial Distribution (n=10, p=0.5)")
#plt.xlabel("Number of Sucess")
#plt.ylabel("Probability")
#plt.show()


#Stimulating a poission Process 
#lambda_=2
#rv_poisson=poisson(mu=lambda_)
#outcomes=rv_poisson.rvs(size=1000)
#print("poisson outcomes:", outcomes)
#print("probability of sucess(p):",lambda_)
#print("empirical probability of sucess:", np.mean(outcomes))

#a=0
#b=10
#rv_uniform = uniform(loc=a, scale=b-a)
#outcome=rv_uniform.rvs(size=1000)
#print("\nuniform outcomes:",outcome)
#print("lower bound (a):",a )
#print("upper bound (b):",b )
#print("emperical mean:", np.mean(outcome))

#x=np.linspace(a,b,100)
#pdf_uniform=rv_uniform.pdf(x)
#plt.plot(x, pdf_uniform)
#plt.title("unifrom distribution (a+0, b+10)")
#plt.xlabel("value")
#plt.ylabel("probability density")
#plt.show()




#hypothesis testing 
#heights=np.array([168,172,170,169,173,170,167,171,174,169])
#mu=170 #null hypothesis
#sample t-test
#t_stat,p_value=stats.ttest_1samp(heights,mu)
#print("T-statistics:",t_stat)
#print("p-value:",p_value)
#
#alpha=0.05
#if p_value <= alpha:
#    print("reject the null hypothyesis")
#    
#else:
#    print("fail to reject the null hypothesis ")



#confidence intervals and effect size
#data=np.array([168,172,170,169,173,170,167,171,174,169])
#mean=np.mean(data)
#print(mean)
#std_dev=np.std(data, ddof=1)
#n=len(data)
#print(n)
#print(n)
#confidence_level=0.95
#alpha=1-confidence_level
#t_critical=stats.t.ppf(1-alpha/2., df=n-1)
#print(t_critical)
#margin_of_error=t_critical*(std_dev/np.sqrt(n))
#print(margin_of_error)
#confidence_interval=(mean-margin_of_error, mean+margin_of_error)
#print(f"95% confidence_interval: {confidence_interval}")


#effect size 
#group1=np.array([168,172,170,169,173,170,167,171,174,169])
#group2=np.array([160,162,165,161,159,164,163,160,166,161])

#mean1=np.mean(group1)
#mean2=np.mean(group2)
#print(mean1)
#print(mean2)

#std_dev1=np.std(group1, ddof=1)
#std_dev2=np.std(group2, ddof=1)
#print(std_dev1, std_dev2)

#pooled_std_dev=np.sqrt(((len(group1)-1)* std_dev1**2+(len(group2)-1)* std_dev2**2)/(len(group1)+len(group2)-2))

#cohen_d=(mean1-mean2)/pooled_std_dev
#print(f"cohen's d:{cohen_d}")


#Liner regression
#x=np.array([1,2,3,4,5]).reshape(-1,1)
#y=np.array([2,3,5,7,11])
#model=LinearRegression()
#model.fit(x,y)

#intercept=model.intercept_
#slope=model.coef_

#y_pred=model.predict(x)
#plt.scatter(x,y, color='blue', label='data points')
#plt.plot(x,y_pred, color='red', label='regression line')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.legend()
#plt.title('simple linear regression')
#plt.show()

#print(f"intercept: {intercept}")
#print(f"slope:{slope}")


#logistic regression
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([0,0,0,1,1])
model=LogisticRegression()
model.fit(x,y)

probabilities=model.predict_proba(x)[:,1]
predictions=model.predict(x)

plt.scatter(x,y, color='blue', label='data points')
plt.plot(x,probabilities, color='red', label='logistic curve')
plt.xlabel('x')
plt.ylabel('probability of class 1')
plt.legend()
plt.title('simple logistic regression')
plt.show()

print(f"coefficients: {model.coef_(0)}")
print(f"intercept: {model.intercept_}")
print(f"predicted probabilities: {probabilities}")
print(f"predicted classes: {predictions}")