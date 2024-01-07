import streamlit as st

def calculate_finances(yearly_income, contribution_percentage, rent_price, personal_expenses):
    """
    Function to calculate the remaining monthly income after expenses.
    :param yearly_income: Annual income before any deductions.
    :param contribution_percentage: Percentage of income contributed to 401k.
    :param rent_price: Monthly rent price.
    :param personal_expenses: Monthly personal expenses.
    :return: Remaining monthly income after all deductions and expenses, and budget allocation.
    """
    # Calculate salary after 401k contribution
    salary_after_contribution = yearly_income * (1 - (contribution_percentage / 100))

    # Hardcoded tax rate
    tax_rate = 30.4  # in percent

    # Calculate salary after taxes
    salary_after_tax = salary_after_contribution * (1 - (tax_rate / 100))

    # Calculate total annual expenses (rent + personal expenses)
    total_annual_expenses = (rent_price * 12) + (personal_expenses * 12)

    # Calculate remaining annual income
    remaining_annual_income = salary_after_tax - total_annual_expenses

    # Convert to monthly
    remaining_monthly_income = remaining_annual_income / 12

    # Apply the 50/30/20 budget rule
    needs, wants, savings = apply_502030_rule(remaining_monthly_income)

    return remaining_monthly_income, needs, wants, savings

def apply_502030_rule(monthly_income):
    """
    Function to apply the 50/30/20 budgeting rule.
    :param monthly_income: Monthly net income.
    :return: Tuple of amounts allocated to needs, wants, and savings.
    """
    needs = monthly_income * 0.50  # 50% for needs
    wants = monthly_income * 0.30  # 30% for wants
    savings = monthly_income * 0.20  # 20% for savings/debt repayment
    return needs, wants, savings

# App layout
st.title("📊 Rent and Budget Calculator")

# Adding a description
st.markdown("""
This tool helps you calculate your remaining monthly income after accounting for your 401k contribution, taxes, rent, and personal expenses.
It also provides a budget allocation based on the 50/30/20 rule.
Fill in the details below and click 'Calculate' to see your results.
""")

# Input fields
col1, col2 = st.columns(2)
with col1:
    yearly_income = st.number_input("Yearly Income", min_value=0)
    rent_price = st.number_input("Monthly Rent Price", min_value=0)

with col2:
    contribution_percentage = st.number_input("401k Contribution Percentage", min_value=0, max_value=100)
    personal_expenses = st.number_input("Monthly Personal Expenses", min_value=0)

# Calculate button
if st.button("Calculate Remaining Monthly Income and Budget Allocation"):
    remaining_monthly_income, needs, wants, savings = calculate_finances(yearly_income, contribution_percentage, rent_price, personal_expenses)
    st.markdown(f"### Remaining Monthly Income: ${remaining_monthly_income:.2f}")
    st.markdown(f"#### Budget Allocation:")
    st.markdown(f"- Needs (50%): ${needs:.2f}")
    st.markdown(f"- Wants (30%): ${wants:.2f}")
    st.markdown(f"- Savings/Debt Repayment (20%): ${savings:.2f}")

# Optional: Add more interactive or informative sections as needed.
