import streamlit as st

def calculate_finances(yearly_income, contribution_percentage, rent_price, personal_expenses):
    """
    Function to calculate the remaining monthly income after expenses.
    :param yearly_income: Annual income before any deductions.
    :param contribution_percentage: Percentage of income contributed to 401k.
    :param rent_price: Monthly rent price.
    :param personal_expenses: Monthly personal expenses.
    :return: Remaining monthly income after all deductions and expenses.
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

    return remaining_monthly_income

# App layout
st.title("📊 Finance Calculator")

# Adding a description
st.markdown("""
This tool helps you calculate your remaining monthly income after accounting for your 401k contribution, taxes, rent, and personal expenses.
Fill in the details below and click 'Calculate' to see your results.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Input Your Details")
    yearly_income = st.number_input("Yearly Income", min_value=0)
    contribution_percentage = st.number_input("401k Contribution Percentage", min_value=0.0, max_value=100.0)
    rent_price = st.number_input("Monthly Rent Price", min_value=0)
    personal_expenses = st.number_input("Monthly Personal Expenses", min_value=0)
    calculate_button = st.button("Calculate")

# Main page layout for displaying the result
if calculate_button:
    remaining_monthly_income = calculate_finances(yearly_income, contribution_percentage, rent_price, personal_expenses)
    st.markdown(f"### Remaining Monthly Income: ${remaining_monthly_income:.2f}")

# Optional: You can add more sections or visualizations here if relevant.