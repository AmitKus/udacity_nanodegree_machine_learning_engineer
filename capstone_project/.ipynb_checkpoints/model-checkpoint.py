from sklearn.preprocessing import PolynomialFeatures
import theano.tensor as tt
import pymc3 as pm


class Model:
    """
    Class defines and fits the pymc3 model
    
    """
    def __init__(self, degree, xcol, ycol):
        """
        degree: degree of polynomial to fit
        xcol: feature column in the dataframe
        ycol: predicted variable in the dataframe
        """
        self.degree = degree
        self.xcol = xcol
        self.ycol = ycol

    def fit(self, df_data, prior_b_sigma=1):
        """
        Defines and fits the pymc3 probabilistic model
        
        Inputs:
            df_data = Input dataframe with columns xcol and ycol
            prior_b_sigma: Standard deviation of the prior of linear coefficients
            
        Output:
            model: pymc3 model object
            trace: pymc3 trace object
        """
        yval = df_data[self.ycol].values
        # Polynomial features
        polynomial_features = PolynomialFeatures(degree=self.degree,
                                                 include_bias=False)
        xval = polynomial_features.fit_transform(
            df_data[self.xcol].values.reshape(-1, 1))

        with pm.Model() as model:
            a = pm.Normal('a', mu=10, sigma=10)
            b = pm.Normal('b', mu=0, sigma=prior_b_sigma, shape=(self.degree))
            sigma = pm.Uniform('sigma', lower=0, upper=10)
            mu = pm.Deterministic('mu', a + tt.dot(xval, b))
            h = pm.Normal('h', mu=mu, sigma=sigma, observed=yval)
            trace = pm.sample(cores=2)

        return model, trace