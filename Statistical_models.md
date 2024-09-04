## EMBL-EBI training webinars

#### Statical models
* The model is our view of the process
* It aims at representing the data generating process
* Summarizeds a set of assumptions
* Specifies relations between varibales
* Help to calculate the probability of the data under some assumptions.

#### Binomial model
|"All models are wrong, but some are useful." 
                                  -George Box
* The model is over-simplifying
* Factors like age, region, other preconditions are neglected
* The assumed n% are subject to uncertainfy

But ...
* Can be a starting point of further investigation
* A straight-forward estimate of how unsual the data are

#### Example
When the true prevalence is 4%, the probability of observing an event of 9/100 (or more extreme) is **p=0.02**.
* Use Python to caculate the p value/ probability of observing k=9 events out of 100,
```{Python}
from scipy.stats import binom
n=100 # the total number of trails or observations
p=0.04 # the true prevalence, or the probability of success
k=9 # the number of observed events
#calculate the p-value
p_value=1-binom.cdf(k-1,n,p)
print(f"The p-value is :{p_value}")
```
It returns 0.01899 

* Binomial probability formula to caculate the p value/ probability of observing k=9 events out of 100,

To calculate the p-value or probability of observing \( k = 9 \) events out of 100 using the binomial probability formula:

**p(X = k) = (n choose k) * p^k * (1 - p)^(n - k)**

Where:

- \( \binom{n}{k} \) is the binomial coefficient, calculated as \( \frac{n!}{k!(n-k)!} \).
- \( p \) is the probability of success.
- \( (1-p) \) is the probability of failure.

Since we are asking about the k=9 or more extreme
the fumula should be:
**p(X>=k)=1-p(X<k) => p(X>=k)=1-p(x<=k-1)**

