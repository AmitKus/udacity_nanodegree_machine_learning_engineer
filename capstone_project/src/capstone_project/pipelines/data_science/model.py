from sklearn.preprocessing import PolynomialFeatures
import theano.tensor as tt
import pymc3 as pm

class PolynomialModel:
    def __init__(self, degree):
        self.degree = degree
        
    def fit(self, X_train, y_train, prior_b_sigma=1):
        yval = y_train
        # Polynomial features
        polynomial_features = PolynomialFeatures(degree=self.degree,
                                                 include_bias=False)
        xval = polynomial_features.fit_transform(
            X_train.reshape(-1, 1))

        with pm.Model() as model:
            a = pm.Normal('a', mu=10, sigma=10)
            b = pm.Normal('b', mu=0, sigma=prior_b_sigma, shape=(self.degree))
            sigma = pm.Uniform('sigma', lower=0, upper=10)
            mu = pm.Deterministic('mu', a + tt.dot(xval, b))
            h = pm.Normal('h', mu=mu, sigma=sigma, observed=yval)
            trace = pm.sample(cores=2)

        return [model, trace]