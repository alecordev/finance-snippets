def pe_ratio(current_share_price, EPS):
    """
    Computes the PE ratio given share price and EPS (earnings per share)
    """
    return current_share_price / EPS

def dividend_yield(annual_dividend_per_share, current_share_price):
    """
    Computes the dividend yield of an equity.
    
    dividend_per_share, share_price
    """
    return (annual_dividend_per_share / current_share_price) * 100

def bond_yield(coupon, purchase_price):
    """
    Returns the result of bond yield given the coupon and purchase price
    """
    return coupon / float(purchase_price)

def current_yield(face_value, coupon_rate, selling_price):
    """
    face_value * coupon_rate = Annual interest Payment
    Current yield = AIP / selling price
    """
    cur_yield = (face_value * coupon_rate) / float(selling_price)
    return cur_yield, '{:.4f}%'.format(cur_yield * 100)

def coupon_payment(principal,libor,spread):
    """
    Computes and returns the coupon payment given the principal, libor rate and spread
    """
    return principal * (libor - spread) * (180/360.0)

def number_of_new_shares(funds_to_be_raised, subscription_price):
    """
    Given the required funds (that need to be raised) and the subscription price, we determine the # of new shares
    
    funds_to_be_raised: amount needed
    subscription_price: value of the subscription
    """
    return funds_to_be_raised / subscription_price

def number_of_rights_required_to_purchase_one_new_share_of_stock(number_of_rights, number_of_new_shares):
    """
    Computes the # of rights required to have 1 unit of the new share
    
    number_of_rights: quantity of current stock outstanding
    number_of_new_shares: result of the number_of_new_shares() function
    """
    return number_of_rights / number_of_new_shares

def ex_rights_price(N, rights_on_price, subscription_price):
    """
    N: number of old shares required for one new (number_of_rights_required_to_purchase_one_new_share_of_stock)
    rights_on_price: current price of the outstanding shares
    subscription_price: the price in which the subscription will be done
    """
    return ((N*rights_on_price) + subscription_price) / (N + 1)

def fair_value_futures(interest_rate_between_now_and_maturity, spot_price, storage_cost=0):
    return (1+interest_rate_between_now_and_maturity+storage_cost)*spot_price

def fair_value_asset_futures(interest_rate_between_now_and_maturity, spot_price, dividends=0):
    return (1+interest_rate_between_now_and_maturity-dividends)*spot_price

def present_value(amount, periods, rate):
    """ Present value computation """
    if rate > 1:
        r = rate / 100
    else:
        r = rate
    return amount / (1 + r) ** periods

def present_value_of_k_payment(k):
    return 100 / (1 + 0.04)**k

def discount_factor(k, r, m):
    """ (periods, annual rate, times per year) 
    
    Discount factor d_k for a payment received after
    k periods, annual interest rate r, interest paid m times
    per year """
    return 1 / (1 + (r / m)) ** k

def annuity_value(A, r, n):
    """
    Value V of an annuity that pays an amount A annually,
    annual interest rate r, n total payments
    """
    return (A / r) * (1 - (1 / (1 + r) ** n))

def perpetual_annuity_value(A, r):
    """
    Value V of a perpetual annuity that pays an amount A
    annually, annual interest rate r
    """
    return A / r

# if __name__ == '__main__':
#     print 'Coupon Payment: {}'.format(coupon_payment(1000000, 0.0431, 0.0002))
#     print 'Current Yield: {}'.format(current_yield(1000, 0.08, 930))
#     print 'Dividend Yield: {}'.format(dividend_yield(0.44, 28.25))
#     print 'PE Ratio: {}'.format(pe_ratio(28.25, 1.72))
#     print 'Bond Yield: {}'.format(bond_yield(8, 930))
#     print 'Fair Value: {}'.format(fair_value_futures(0.05, 50, 0))
#     print 'Asset Futures Fair Value: {}'.format(fair_value_asset_futures(0.03, 50, 0.02))
#     print current_yield(1000, 0.08, 930)
    # print(present_value_of_k_payment(3))
    # print(annuity_value(1000, 0.03, 15))
    # print(perpetual_annuity_value(1000, 0.03) - annuity_value(1000, 0.03, 15))