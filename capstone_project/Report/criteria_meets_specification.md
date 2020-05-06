## Data Preprocessing

The data does not have any missing or unphysical values. For modeling purposes, the age column (feature vector) was standardize. Standardization typically means rescaling data to have a mean of 0 and a standard deviation of 1 (unit variance). THe formula for standardization is:

$ X' = \frac{X - \mu}{\sigma}$


## Implementation

The following polynomial models were fitted to the data using the probabilisic programming package PyMC3.

$$
\begin{equation} \label{eq1}
\begin{split}
\cal{M}_p: h_i &\approx \text{Normal}(\mu_i, \sigma) \\
 \mu_i &= \alpha + \beta_1 x_i + \beta_2 x_i^2 ..... + \beta_p x_i^p
\end{split}
\end{equation}
$$ 

### Evaluation metrics: Information Criteria

A good model is one that 



We will compare different models based on their WAIC scores(Watanabe–Akaike information criterion). We will rank the model based on their WAIC score and the model with lowest WAIC score is our best model.

**Widely Applicable Information Criterion (WAIC):** It does not require a multivariate Gaussian posterior, and it is often more accurate than DIC. The distinguishing feature of WAIC is that it is pointwise. It access flexibility of a model with respect to fitting each observation, and then sumps up across all observations.

$WAIC = -2 (\sum_{i=1}^N \log Pr(y_i) - \sum_{i=1}^N V(y_i))$

Where $V(y_i)$ is the variance in the log-likelihood for observation $i$ in the training sample.

http://www.stat.columbia.edu/~gelman/research/published/waic_understand3.pdf

logpdf will be imported from stats package. </br>

$p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }} e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} }$

$log(p(x)) = -0.5*log{2 \pi \sigma^2} - \frac{ (x - \mu)^2 } {2 \sigma^2}$

From WAIC definition (compute for each $y_i$ or weigth data):

$\log Pr(y_i) = -0.5*log{2 \pi \sigma^2} - \frac{ (y_i - \mu_i)^2 } {2 \sigma^2}$

Refinement

The process of improving upon the algorithms and techniques used is clearly documented. Both the initial and final solutions are reported, along with intermediate solutions, if necessary.
