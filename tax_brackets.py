def get_tax_brackets(filing_status):
    tax_brackets = {
        "single": [
            (9875, 0.10), (40125, 0.12), (85525, 0.22), (163300, 0.24),
            (207350, 0.32), (518400, 0.35), (float('inf'), 0.37)
        ],
        "married_filing_jointly": [
            (19750, 0.10), (80250, 0.12), (171050, 0.22), (326600, 0.24),
            (414700, 0.32), (622050, 0.35), (float('inf'), 0.37)
        ],
        "married_filing_separately": [
            (9875, 0.10), (40125, 0.12), (85525, 0.22), (163300, 0.24),
            (207350, 0.32), (311025, 0.35), (float('inf'), 0.37)
        ],
        "head_of_household": [
            (14100, 0.10), (53700, 0.12), (85500, 0.22), (163300, 0.24),
            (207350, 0.32), (518400, 0.35), (float('inf'), 0.37)
        ]
    }
    return tax_brackets.get(filing_status.lower(), [])

def calculate_tax(income, filing_status):
    brackets = get_tax_brackets(filing_status)
    tax = 0
    previous_limit = 0

    for limit, rate in brackets:
        if income > limit:
            tax += (limit - previous_limit) * rate
        else:
            tax += (income - previous_limit) * rate
            break
        previous_limit = limit

    return tax
