import streamlit as st


def update(key: str) -> None:
    """Update the min/max values of a slider.

    Values are updated to reflect changes made in either of the other
    two sliders. The totals of all three sliders must equal three (3)
    "standard deviations".
    """
    match key:
        case "profit":
            ...

        case "revenue":
            ...

        case "equity":
            ...


profit_share = st.slider(
    "Profit Share", min_value=0.0, max_value=30.0, step=0.1, key="profit"
)
monthly_revenue = st.slider(
    "Monthly Revenue",
    min_value=5_000,
    max_value=20_000,
    step=100,
    key="revenue",
)
equity = st.slider(
    "Equity", min_value=0.0, max_value=21.0, step=0.1, key="equity"
)
