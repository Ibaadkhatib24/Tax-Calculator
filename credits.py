def apply_tax_credits(tax, credits, kids, dependents):
    child_tax_credit = 2000 * kids
    other_dependents_credit = 500 * dependents
    total_credits = sum(credits) + child_tax_credit + other_dependents_credit
    tax -= total_credits
    return max(tax, 0)
