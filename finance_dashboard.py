import pandas as pd
import streamlit as st

# Load transaction data
df = pd.read_csv("data/transactions.csv", parse_dates=["date"])

# Calculate totals
total_income = df[df["amount"] > 0]["amount"].sum()
total_expenses = df[df["amount"] < 0]["amount"].sum()
balance = total_income + total_expenses

# Calculate spending by category
category_spending = (
    df[df["amount"] < 0]
    .groupby("category")["amount"]
    .sum()
    .abs()
)

# Streamlit dashboard UI
st.title("Personal Finance Dashboard")

st.metric("Income", f"${total_income}")
st.metric("Expenses", f"${abs(total_expenses)}")
st.metric("Balance", f"${balance}")

st.subheader("Spending by Category")
st.bar_chart(category_spending)
