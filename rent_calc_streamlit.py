import streamlit as st

def calculate_finances(yearly_income, contribution_percentage, rent_price, personal_expenses):
    """
    Function to calculate the remaining monthly income after expenses and 
    provide both theoretical and actual budget allocations based on the 50/30/20 rule.
    """
    # Calculate salary after 401k contribution
    salary_after_contribution = yearly_income * (1 - (contribution_percentage / 100))

    # Hardcoded tax rate
    tax_rate = 30.4  # in percent

    # Calculate salary after taxes
    salary_after_tax = salary_after_contribution * (1 - (tax_rate / 100))

    # Calculate remaining monthly income
    remaining_monthly_income = salary_after_tax / 12

    # Theoretical budget allocation based on net income
    theoretical_needs, theoretical_wants, theoretical_savings = apply_502030_rule(remaining_monthly_income)

    # Actual budget allocation after rent and personal expenses
    actual_remaining_income = remaining_monthly_income - rent_price - personal_expenses
    actual_needs, actual_wants, actual_savings = apply_502030_rule(actual_remaining_income)

    return actual_remaining_income, (theoretical_needs, theoretical_wants, theoretical_savings), (actual_needs, actual_wants, actual_savings)

def apply_502030_rule(monthly_income):
    """
    Function to apply the 50/30/20 budgeting rule.
    """
    needs = monthly_income * 0.60  # 50% for needs
    wants = monthly_income * 0.30  # 30% for wants
    savings = monthly_income * 0.10  # 20% for savings/debt repayment
    return needs, wants, savings

# App layout
st.title("📊 Rent and Budget Calculator")

# Adding a description
st.markdown("""
This tool helps you calculate your remaining monthly income after accounting for your 401k contribution, taxes, rent, and personal expenses. 
It also provides a budget allocation based on the 60/30/10 rule, both theoretically and actually based on your expenses.
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
    actual_remaining_income, (theo_needs, theo_wants, theo_savings), (act_needs, act_wants, act_savings) = calculate_finances(yearly_income, contribution_percentage, rent_price, personal_expenses)
    st.markdown(f"### Remaining Monthly Income: ${actual_remaining_income:.2f}")
    st.markdown(f"#### Theoretical Budget Allocation (Based on Net Income):")
    st.markdown(f"- Needs (50%): ${theo_needs:.2f}")
    st.markdown(f"- Wants (30%): ${theo_wants:.2f}")
    st.markdown(f"- Savings/Debt Repayment (20%): ${theo_savings:.2f}")
    st.markdown(f"#### Actual Budget Allocation (After Rent and Personal Expenses):")
    st.markdown(f"- Needs: ${act_needs:.2f}")
    st.markdown(f"- Wants: ${act_wants:.2f}")
    st.markdown(f"- Savings/Debt Repayment: ${act_savings:.2f}")

# Optional: Add more interactive or informative sections as needed.
