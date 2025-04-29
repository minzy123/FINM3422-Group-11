def pe_ratio(price, earnings): # Function to calculate the P/E ratio of a stock
    return price / earnings

def dividend_yield(dividend, price): # Function to calculate the dividend yield of a stock
    return dividend / price

def eps(earnings, shares_outstanding): # Function to calculate the earnings per share of a stock
    return earnings / shares_outstanding

def roa(earnings, total_assets): # Function to calculate ROA of a stock
    return earnings / total_assets

def roe(earnings, total_equity): # Function to calculate ROE of a stock
    return earnings / total_equity

def de_ratio(total_debt, total_equity): # Function to calculate debt to equity ratio of a stock
    return total_debt / total_equity

def current_ratio(current_assets, current_liabilities): # Function to calculate the current ratio of a stock
    return current_assets / current_liabilities

def quick_ratio(current_assets, current_liabilities, inventory): # Function to calculate the quick ratio of a stock
    return (current_assets - inventory)/ current_liabilities

def net_margin(earnings, total_revenue): # Function to calculate the net margin of a stock
    return earnings / total_revenue

def interest_coverage_ratio(ebit, interest_expense): # Function to calculate the interest coverage ratio of a stock
    return ebit / interest_expense

def ev_ebitda(ev, ebitda): # Function to calculate the Enterprise Value over EBITDA of a stock
    return ev / ebitda

def asset_turnover(total_assets, total_revenue): # Function to calculate the asset turnover of a stock
    return total_assets / total_revenue

def inventory_turnover(inventory, total_revenue): # Function to calculate the inventory turnover of a stock
    return inventory / total_revenue