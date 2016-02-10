# Valuation of European call options in Black-Scholes-Merton model
# incl. Vega function and implied volatility estimation

# Analytical Black-Scholes-Merton (BSM) Formula
def bsm_call_value(S0, K, T, r, sigma):
    """
    Valuation of European call option in BSM model.

    :param S0: initial stock/index level
    :type S0: float
    :param K: strike price
    :type K: float
    :param T: maturity date (in year fractions)
    :type T: float
    :param r: constant risk-free short rate
    :type r: float
    :param sigma: volatility factor in diffusion term
    :type sigma: float

    :return: present value of the European call option
    :rtype: float
    """
    from math import log, sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)
            - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
      # stats.norm.cdf --> cumulative distribution function
      #                    for normal distribution
    return value

def bsm_mcs_valuation(strike):
    """
    Dynamic Black-Scholes-Merton Monte Carlo estimator
    for European calls.

    :param strike: strike price of the option
    :type strike: float

    :return value: estimate for present value of call option
    :rtype: float
    """
    import numpy as np

    S0 = 100.; T = 1.0; r = 0.05; vola = 0.2
    M = 50; I = 20000
    dt = T / M
    rand = np.random.standard_normal((M + 1, I))
    S = np.zeros((M + 1, I)); S[0] = S0
    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - 0.5 * vola ** 2) * dt + vola * np.sqrt(dt) * rand[t])
    value = (np.exp(-r * T) * np.sum(np.maximum(S[-1] - strike, 0)) / I)
    return value

def par_value(n):
    """
    Parallel option valuation.

    :param n: number of option valuations/strikes
    :type n: int

    :rtype: tuple
    """
    strikes = np.linspace(80, 120, n)
    option_values = []
    for strike in strikes:
       value = view.apply_async(bsm_mcs_valuation, strike)
       option_values.append(value)
    c.wait(option_values)
    return strikes, option_values

# Vega function
def bsm_vega(S0, K, T, r, sigma):
    """
    Vega of European option in BSM model.

    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date (in year fractions)
    r : float
        constant risk-free short rate
    sigma : float
        volatility factor in diffusion term

    :return vega: partial derivative of BSM formula with respect to sigma, i.e. Vega
    :rtype: float
    """
    from math import log, sqrt
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T / (sigma * sqrt(T))

    vega = (S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T))
    return vega

# Implied volatility function
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    """
    Implied volatility of European call option in BSM model.

    Parameters
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date (in year fractions)
    r : float
        constant risk-free short rate
    sigma_est : float
        estimate of impl. volatility
    it : integer
        number of iterations

    Returns
    simga_est : float
        numerically estimated implied volatility
    """

    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0)
                        / bsm_vega(S0, K, T, r, sigma_est))
    return sigma_est