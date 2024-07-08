def get_standard_deduction(filing_status, over_65, spouse_over_65):
    standard_deductions = {
        "single": 12400,
        "married_filing_jointly": 24800,
        "married_filing_separately": 12400,
        "head_of_household": 18650
    }
    additional_standard_deduction = {
        "single": 1650,
        "married_filing_jointly": 1300,
        "married_filing_separately": 1300,
        "head_of_household": 1650
    }
    base_deduction = standard_deductions.get(filing_status.lower(), 0)
    additional_deduction = 0
    if over_65:
        additional_deduction += additional_standard_deduction.get(filing_status.lower(), 0)
    if spouse_over_65 and filing_status.lower() == "married_filing_jointly":
        additional_deduction += additional_standard_deduction.get(filing_status.lower(), 0)
    return base_deduction + additional_deduction
