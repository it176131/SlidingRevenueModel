import streamlit as st


def update(key: str) -> None:
    """Update the min/max values of a slider.

    Values are updated to reflect changes made in either of the other
    two sliders. The totals of all three sliders must equal three (3)
    "standard deviations".
    """
    match key:
        case "profit":
            profit_ratio = st.session_state.profit / profit_share.max_value  # noqa: F841
            st.session_state.revenue = ...
            st.session_state.equity = ...

        case "revenue":
            revenue_ratio = (  # noqa: F841
                st.session_state.revenue / monthly_revenue.max_value
            )
            st.session_state.profit = ...
            st.session_state.equity = ...

        case "equity":
            equity_ratio = st.session_state.equity / equity.max_value  # noqa: F841
            st.session_state.profit = ...
            st.session_state.revenue = ...


profit_share = st.slider(
    label="Profit Share",
    min_value=0.0,
    max_value=30.0,
    step=0.1,
    format="%0.1f%%",
    key="profit",
)
monthly_revenue = st.slider(
    label="Monthly Revenue",
    min_value=5_000,
    max_value=20_000,
    step=100,
    key="revenue",
)
equity = st.slider(
    label="Equity",
    min_value=0.0,
    max_value=21.0,
    step=0.1,
    format="%0.1f%%",
    key="equity",
)
