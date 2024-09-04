## EMBL-EBI Training Webinars

### Statistical Models

- **Purpose:** A statistical model represents our view of a process and aims to describe the data-generating process.
- **Function:** It summarizes a set of assumptions and specifies the relationships between variables.
- **Use:** Helps calculate the probability of the data under these assumptions.

### Binomial Model

> "All models are wrong, but some are useful."  
> — George Box

- **Simplification:** The binomial model simplifies reality by neglecting factors like age, region, or other preconditions. Assumed probabilities are subject to uncertainty.
- **Usefulness:** Despite its simplifications, the binomial model can serve as a starting point for further investigation and provides a straightforward estimate of how unusual the data might be.

### Example

When the true prevalence is 4%, the probability of observing 9 or more events out of 100 (or more extreme) is **p=0.02**.

#### Python Code for p-Value Calculation

To calculate the p-value for observing \( k = 9 \) events out of 100, you can use the following Python code:

```python
from scipy.stats import binom

n = 100  # Total number of trials or observations
p = 0.04  # True prevalence or probability of success
k = 9  # Number of observed events

# Calculate the p-value
p_value = 1 - binom.cdf(k - 1, n, p)
print(f"The p-value is: {p_value}")
```
It returns 0.01899 

* Binomial probability formula to caculate the p value/ probability of observing k=9 events out of 100,

To calculate the p-value or probability of observing \( k = 9 \) events out of 100 using the binomial probability formula:

**p(X = k) = (n choose k) * p^k * (1 - p)^(n - k)**
![binomial_probability_formula](images/binomial_probability_formula.png)

Since we are asking about the k=9 or more extreme
the fumula should be:

**p(X>=k)=1-p(X<k) or p(X>=k)=1-p(x<=k-1)**

