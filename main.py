# Trapezoidal Membership Function
def trapezoidal_membership(value, a, b, c, d):
    if value <= a or value >= d:
        return 0
    elif a < value <= b:
        return (value - a) / (b - a)
    elif b < value <= c:
        return 1
    elif c < value < d:
        return (d - value) / (d - c)
    return 0

def trapezoidal_defuzzification(value, a, b, c, d):
    """Trapezoidal membership function for defuzzification."""
    if value == 1:
        return (b + c) / 2
    elif 0 < value < 1:
        if value <= (b - a) / (d - a):
            return a + value * (b - a)
        else:
            return d - value * (d - c)
    return 0


def triangular_membership(value, a, b, c):
    if value <= a or value >= c:
        return 0
    elif a < value <= b:
        return (value - a) / (b - a)
    elif b < value < c:
        return (c - value) / (c - b)
    return 0

def triangular_defuzzification(value, a, b, c):
    """
    Defuzzification for a triangular membership function.
    - 'value' is the membership value (between 0 and 1).
    - 'a', 'b', 'c' are the triangle points (a ≤ b ≤ c).
    """
    if value == 0:
        return 0  # Membership value is 0, no contribution
    elif value == 1:
        return b  # Maximum membership, return the peak value

    # Calculate the corresponding crisp value when membership value is between 0 and 1
    if value < 1:
        if b - a != 0:
            left_side = a + value * (b - a)
        else:
            left_side = b
        
        if c - b != 0:
            right_side = c - value * (c - b)
        else:
            right_side = b
        
        # Return the average of the left and right side calculations
        return left_side


# Fuzzification for market value
def fuzzify_market_value(market_value):

    low = trapezoidal_membership(market_value, 0, 0, 90000, 100000)
    medium = trapezoidal_membership(market_value, 80000, 120000, 200000, 250000)
    high = trapezoidal_membership(market_value, 200000, 300000, 650000, 850000)
    very_high = trapezoidal_membership(market_value, 650000, 850000, 1000000, 1000000)

    print("Market Value Fuzzification:", {'low': low, 'medium': medium, 'high': high, 'very_high': very_high})
    
    return {'low': low, 'medium': medium, 'high': high, 'very_high': very_high}

# Fuzzification for location
def fuzzify_location(location_score):

    bad = trapezoidal_membership(location_score, 0, 0, 1.5, 4)
    fair = trapezoidal_membership(location_score, 2.5, 5, 6, 8.5)
    excellent = trapezoidal_membership(location_score, 6, 8, 10, 10)

    print("location Value Fuzzification:", {'bad': bad, 'fair': fair, 'excellent': excellent})
    
    return {'bad': bad, 'fair': fair, 'excellent': excellent}

def fuzzify_assets(assets_value):
    low = triangular_membership(assets_value, 0, 0, 150_000)
    medium = trapezoidal_membership(assets_value, 70000, 250000, 480000, 650000)
    high = trapezoidal_membership(assets_value, 500000, 700000, 1000000, 1000000)

    print("assets Value Fuzzification:", {'low': low, 'medium': medium, 'high': high})
    
    return {'low': low, 'medium': medium, 'high': high}

# Fuzzification for salary
def fuzzify_salary(salary_value):
    low = trapezoidal_membership(salary_value, 0, 0, 10_000, 25_000)
    medium = triangular_membership(salary_value, 15_000, 35_000, 55_000)
    high = triangular_membership(salary_value, 40_000, 60_000, 80_000)
    very_high = trapezoidal_membership(salary_value, 60_000, 80_000, 100_000, 100_000)

    print("salary Value Fuzzification:", {'low': low, 'medium': medium, 'high': high, 'very_high': very_high})
    
    return {'low': low, 'medium': medium, 'high': high, 'very_high': very_high}

# Fuzzification for interest rate
def fuzzify_interest_rate(interest_rate):

    low = trapezoidal_membership(interest_rate, 0, 0, 2, 5)
    medium = trapezoidal_membership(interest_rate, 2, 4, 6, 8)
    high = trapezoidal_membership(interest_rate, 6, 8, 10, 10)

    print("interest rate Value Fuzzification:", {'low': low, 'medium': medium, 'high': high})
    
    return {'low': low, 'medium': medium, 'high': high}



# Rule-based system for House Evaluation
def evaluate_house(market_value, location):
    # Debugging print to check input evaluations

    house_value = {
        'very_low': 0,
        'low': 0,
        'medium': 0,
        'high': 0,
        'very_high': 0
    }

    # Rule 1: If (Market_value is Low) -> House is Low
    if market_value['low'] > 0:
        house_value['low'] = market_value['low']

    # Rule 2: If (Location is Bad) -> House is Low
    if location['bad'] > 0:
        house_value['low'] = location['bad']

    # Rule 3: If (Location is Bad) and (Market_value is Low) -> House is Very_Low
    if location['bad'] > 0 and market_value['low'] > 0:
        house_value['very_low'] = min(location['bad'], market_value['low'])

    # Rule 4: If (Location is Bad) and (Market_value is Medium) -> House is Low
    if location['bad'] > 0 and market_value['medium'] > 0:
        house_value['low'] = min(location['bad'], market_value['medium'])

    # Rule 5: If (Location is Bad) and (Market_value is High) -> House is Medium
    if location['bad'] > 0 and market_value['high'] > 0:
        house_value['medium'] = min(location['bad'], market_value['high'])

    # Rule 6: If (Location is Bad) and (Market_value is Very_High) -> House is High
    if location['bad'] > 0 and market_value['very_high'] > 0:
        house_value['high'] = min(location['bad'], market_value['very_high'])

    # Rule 7: If (Location is Fair) and (Market_value is Low) -> House is Low
    if location['fair'] > 0 and market_value['low'] > 0:
        house_value['low'] = min(location['fair'], market_value['low'])

    # Rule 8: If (Location is Fair) and (Market_value is Medium) -> House is Medium
    if location['fair'] > 0 and market_value['medium'] > 0:
        house_value['medium'] = min(location['fair'], market_value['medium'])

    # Rule 9: If (Location is Fair) and (Market_value is High) -> House is High
    if location['fair'] > 0 and market_value['high'] > 0:
        house_value['high'] = min(location['fair'], market_value['high'])

    # Rule 10: If (Location is Fair) and (Market_value is Very_High) -> House is Very_High
    if location['fair'] > 0 and market_value['very_high'] > 0:
        house_value['very_high'] = min(location['fair'], market_value['very_high'])

    # Rule 11: If (Location is Excellent) and (Market_value is Low) -> House is Medium
    if location['excellent'] > 0 and market_value['low'] > 0:
        house_value['medium'] = min(location['excellent'], market_value['low'])

    # Rule 12: If (Location is Excellent) and (Market_value is Medium) -> House is High
    if location['excellent'] > 0 and market_value['medium'] > 0:
        house_value['high'] = min(location['excellent'], market_value['medium'])

    # Rule 13: If (Location is Excellent) and (Market_value is High) -> House is Very_High
    if location['excellent'] > 0 and market_value['high'] > 0:
        house_value['very_high'] = min(location['excellent'], market_value['high'])

    # Rule 14: If (Location is Excellent) and (Market_value is Very_High) -> House is Very_High
    if location['excellent'] > 0 and market_value['very_high'] > 0:
        house_value['very_high'] = min(location['excellent'], market_value['very_high'])

    # Debugging print to inspect the house evaluation values
    print("House Evaluation (After logic):", house_value)
    
    return house_value


# Rule-based system for Applicant Evaluation
def evaluate_applicant(assets, salary):
    # Debugging print to check input evaluations

    applicant_value = {
        'low': 0,
        'medium': 0,
        'high': 0
    }

    # Rule 1: If (Asset is Low) and (Income is Low) -> Applicant is Low
    if assets['low'] > 0 and salary['low'] > 0:
        applicant_value['low'] = min(assets['low'], salary['low'])

    # Rule 2: If (Asset is Low) and (Income is Medium) -> Applicant is Low
    if assets['low'] > 0 and salary['medium'] > 0:
        applicant_value['low'] = min(assets['low'], salary['medium'])

    # Rule 3: If (Asset is Low) and (Income is High) -> Applicant is Medium
    if assets['low'] > 0 and salary['high'] > 0:
        applicant_value['medium'] = min(assets['low'], salary['high'])

    # Rule 4: If (Asset is Low) and (Income is Very_High) -> Applicant is High
    if assets['low'] > 0 and salary['very_high'] > 0:
        applicant_value['high'] = min(assets['low'], salary['very_high'])

    # Rule 5: If (Asset is Medium) and (Income is Low) -> Applicant is Low
    if assets['medium'] > 0 and salary['low'] > 0:
        applicant_value['low'] = min(assets['medium'], salary['low'])

    # Rule 6: If (Asset is Medium) and (Income is Medium) -> Applicant is Medium
    if assets['medium'] > 0 and salary['medium'] > 0:
        applicant_value['medium'] = min(assets['medium'], salary['medium'])

    # Rule 7: If (Asset is Medium) and (Income is High) -> Applicant is High
    if assets['medium'] > 0 and salary['high'] > 0:
        applicant_value['high'] = min(assets['medium'], salary['high'])

    # Rule 8: If (Asset is Medium) and (Income is Very_High) -> Applicant is High
    if assets['medium'] > 0 and salary['very_high'] > 0:
        applicant_value['high'] = min(assets['medium'], salary['very_high'])

    # Rule 9: If (Asset is High) and (Income is Low) -> Applicant is Medium
    if assets['high'] > 0 and salary['low'] > 0:
        applicant_value['medium'] = min(assets['high'], salary['low'])

    # Rule 10: If (Asset is High) and (Income is Medium) -> Applicant is Medium
    if assets['high'] > 0 and salary['medium'] > 0:
        applicant_value['medium'] = min(assets['high'], salary['medium'])

    # Rule 11: If (Asset is High) and (Income is High) -> Applicant is High
    if assets['high'] > 0 and salary['high'] > 0:
        applicant_value['high'] = min(assets['high'], salary['high'])

    # Rule 12: If (Asset is High) and (Income is Very_High) -> Applicant is High
    if assets['high'] > 0 and salary['very_high'] > 0:
        applicant_value['high'] = min(assets['high'], salary['very_high'])

    # Debugging print to inspect the applicant evaluation values
    print("Applicant Evaluation (After logic):", applicant_value)
    
    return applicant_value


# Rule-based system for Loan Evaluation
def evaluate_loan(applicant, house, interest_rate):
    # Debugging print to check input evaluations

    loan_value = {
        'very_low': 0,
        'low': 0,
        'medium': 0,
        'high': 0,
        'very_high': 0
    }
    
    # Rule 1: If (Income is Low) and (Interest is Medium) -> Credit is Very_Low
    if applicant['low'] > 0 and interest_rate['medium'] > 0:
        loan_value['very_low'] = max(applicant['low'], interest_rate['medium'])

    # Rule 2: If (Income is Low) and (Interest is High) -> Credit is Very_Low
    if applicant['low'] > 0 and interest_rate['high'] > 0:
        loan_value['very_low'] = max(applicant['low'], interest_rate['high'])
    
    # Rule 3: If (Income is Medium) and (Interest is High) -> Credit is Low
    if applicant['medium'] > 0 and interest_rate['high'] > 0:
        loan_value['low'] = max(applicant['medium'], interest_rate['high'])
    
    # Rule 4: If (Applicant is Low) -> Credit is Very_Low
    if applicant['low'] > 0:
        loan_value['very_low'] = applicant['low']
    
    # Rule 5: If (House is Very_Low) -> Credit is Very_Low
    if house['very_low'] > 0:
        loan_value['very_low'] = house['very_low']
    
    # Rule 6: If (Applicant is Medium) and (House is Very_Low) -> Credit is Low
    if applicant['medium'] > 0 and house['very_low'] > 0:
        loan_value['low'] = max(applicant['medium'], house['very_low'])
    
    # Rule 7: If (Applicant is Medium) and (House is Low) -> Credit is Low
    if applicant['medium'] > 0 and house['low'] > 0:
        loan_value['low'] = max(applicant['medium'], house['low'])
    
    # Rule 8: If (Applicant is Medium) and (House is Medium) -> Credit is Medium
    if applicant['medium'] > 0 and house['medium'] > 0:
        loan_value['medium'] = max(applicant['medium'], house['medium'])
    
    # Rule 9: If (Applicant is Medium) and (House is High) -> Credit is High
    if applicant['medium'] > 0 and house['high'] > 0:
        loan_value['high'] = max(applicant['medium'], house['high'])
    
    # Rule 10: If (Applicant is Medium) and (House is Very_High) -> Credit is High
    if applicant['medium'] > 0 and house['very_high'] > 0:
        loan_value['high'] = max(applicant['medium'], house['very_high'])
    
    # Rule 11: If (Applicant is High) and (House is Very_Low) -> Credit is Low
    if applicant['high'] > 0 and house['very_low'] > 0:
        loan_value['low'] = max(applicant['high'], house['very_low'])
    
    # Rule 12: If (Applicant is High) and (House is Low) -> Credit is Medium
    if applicant['high'] > 0 and house['low'] > 0:
        loan_value['medium'] = max(applicant['high'], house['low'])
    
    # Rule 13: If (Applicant is High) and (House is Medium) -> Credit is High
    if applicant['high'] > 0 and house['medium'] > 0:
        loan_value['high'] = max(applicant['high'], house['medium'])
    
    # Rule 14: If (Applicant is High) and (House is High) -> Credit is High
    if applicant['high'] > 0 and house['high'] > 0:
        loan_value['high'] = max(applicant['high'], house['high'])
    
    # Rule 15: If (Applicant is High) and (House is Very_High) -> Credit is Very_High
    if applicant['high'] > 0 and house['very_high'] > 0:
        loan_value['very_high'] = max(applicant['high'], house['very_high'])
    
    # Debugging print to inspect the loan evaluation values
    print("Loan Evaluation (After logic):", loan_value)
    
    return loan_value

def defuzzify_loan(loan_eval):
    priority = ['very_low', 'low', 'medium', 'high', 'very_high']
    max_key = max(loan_eval, key=lambda k: (loan_eval[k], priority.index(k)))

    if max_key == 'very_low':
        crisp_loan_amount = triangular_defuzzification(loan_eval[max_key], 0, 0, 100_000)
    elif max_key == 'low':
        crisp_loan_amount = triangular_defuzzification(loan_eval[max_key], 0, 125_000, 250_000)
    elif max_key == 'medium':
        crisp_loan_amount = triangular_defuzzification(loan_eval[max_key], 125_000, 250_000, 375_000)
    elif max_key == 'high':
        crisp_loan_amount = triangular_defuzzification(loan_eval[max_key], 250_000, 375_000, 500_000)
    elif max_key == 'very_high':
        crisp_loan_amount = triangular_defuzzification(loan_eval[max_key], 375_000, 500_000, 500_000)

    return crisp_loan_amount

def defuzzify_house(house_eval):
    priority = ['very_low', 'low', 'medium', 'high', 'very_high']
    max_key = max(house_eval, key=lambda k: (house_eval[k], priority.index(k)))

    if max_key == 'very_low':
        crisp_house_value = triangular_defuzzification(house_eval[max_key], 0, 0, 3)
    elif max_key == 'low':
        crisp_house_value = triangular_defuzzification(house_eval[max_key], 0, 3, 6)
    elif max_key == 'medium':
        crisp_house_value = triangular_defuzzification(house_eval[max_key], 2, 5, 8)
    elif max_key == 'high':
        crisp_house_value = triangular_defuzzification(house_eval[max_key], 4, 7, 10)
    elif max_key == 'very_high':
        crisp_house_value = triangular_defuzzification(house_eval[max_key], 7, 10, 10)

    return crisp_house_value

def defuzzify_applicant(applicant_eval):
    priority = ['low', 'medium', 'high']
    max_key = max(applicant_eval, key=lambda k: (applicant_eval[k], priority.index(k)))

    if max_key == 'low':
        crisp_applicant_value = trapezoidal_defuzzification(applicant_eval[max_key], 0, 0, 2, 4)
    elif max_key == 'medium':
        crisp_applicant_value = triangular_defuzzification(applicant_eval[max_key], 2, 5, 8)
    elif max_key == 'high':
        crisp_applicant_value = trapezoidal_defuzzification(applicant_eval[max_key], 6, 8, 10, 10)

    return crisp_applicant_value


# Main function to integrate all the steps
def main():
    # Example input values
    market_value = 213_000
    location_score = 5
    assets_value = 125_000
    income_value = 63_000
    interest_rate_value = 5

    # Fuzzification process
    fuzzy_market_value = fuzzify_market_value(market_value)
    fuzzy_location = fuzzify_location(location_score)
    fuzzy_assets = fuzzify_assets(assets_value)
    fuzzy_income = fuzzify_salary(income_value)
    fuzzy_interest_rate = fuzzify_interest_rate(interest_rate_value)

    house_eval = evaluate_house(fuzzy_market_value, fuzzy_location)
    applicant_eval = evaluate_applicant(fuzzy_assets, fuzzy_income)
    loan_eval = evaluate_loan(applicant_eval, house_eval, fuzzy_interest_rate)
    
    house_final = defuzzify_house(house_eval)
    applicant_final = defuzzify_applicant(applicant_eval)
    loan_final = defuzzify_loan(loan_eval)


    # Print results
    print(f"Applicant Value: {applicant_final}")
    print(f"House Value: {house_final}")
    print(f"Loan Amount: ${loan_final:.2f}")


if __name__ == "__main__":
    main()


