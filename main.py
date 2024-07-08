from tax_brackets import calculate_tax
from deductions import get_standard_deduction
from credits import apply_tax_credits
import config

def tax_calculator():
    filing_status = config.status
    income = float(input("Enter your annual income: $").replace(',', ''))
    credits = float(input("Enter your total tax credits: $").replace(',', ''))

    # Apply standard deduction or itemized deductions
    if config.itemizing:
        itemized_deductions = float(input("Enter your total itemized deductions: $").replace(',', ''))
        taxable_income = max(0, income - itemized_deductions)
    else:
        standard_deduction = get_standard_deduction(filing_status, config.over_65, config.spouse_over_65)
        taxable_income = max(0, income - standard_deduction)

    # Calculate tax
    tax = calculate_tax(taxable_income, filing_status)

    # Apply tax credits
    final_tax = apply_tax_credits(tax, [credits], config.kids, config.dependents)

    print(f"\nTax Summary for {filing_status.replace('_', ' ').title()}:")
    print(f"Income: ${income:,.2f}")
    if config.itemizing:
        print(f"Itemized Deductions: -${itemized_deductions:,.2f}")
    else:
        print(f"Standard Deduction: -${standard_deduction:,.2f}")
    print(f"Taxable Income: ${taxable_income:,.2f}")
    print(f"Calculated Tax: ${tax:,.2f}")
    print(f"Tax Credits: -${credits:,.2f}")
    print(f"Final Tax: ${final_tax:,.2f}")

# Run the calculator
if __name__ == "__main__":
    tax_calculator()
