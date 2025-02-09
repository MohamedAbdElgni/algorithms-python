# Pearson correlation algorithm design
### Formulas
- Check [link](https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/)

### Algorithm
#### Input
- Two lists of numbers x[], y[] to calculate the correlation coefficient between them.
- Constraints:
  - length of n = len(x) = len(y) = r > 0

#### Process `naieve`
1. n
2. sum(x*y)
3. sum(x) 
4. sum(y)
5. sum(x^2)
6. sum(y^2)
7. sum(x)^2
8. sum(y)^2
9. Calculate the correlation coefficient using the formula:
      - r = (n * sum(x*y) - sum(x) * sum(y)) / sqrt((n * sum(x^2) - sum(x)^2) * (n * sum(y^2) - sum(y)^2))

#### Process `optimized`
... **TODO**

#### Output
r