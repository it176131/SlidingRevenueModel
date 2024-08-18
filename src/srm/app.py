import streamlit as st

MIN_PROFIT = 0.0
MAX_PROFIT = 30.0
MIN_REVENUE = 5_000
MAX_REVENUE = 20_000
RANGE_REVENUE = MAX_REVENUE - MIN_REVENUE
MIN_EQUITY = 0.0
MAX_EQUITY = 21.0


def update(key: str, locked: bool) -> None:
    """Update the min/max values of a slider.

    Values are updated to reflect changes made in either of the other
    two sliders. The totals of all three sliders must equal three (3)
    "standard deviations".
    """
    match key, locked:
        case "profit", False:
            ratio = st.session_state.profit / MAX_PROFIT
            if not st.session_state.revenue_lock:
                st.session_state.revenue = (
                    RANGE_REVENUE * (1 - ratio) / 2 + MIN_REVENUE
                )

            if not st.session_state.equity_lock:
                st.session_state.equity = MAX_EQUITY * (1 - ratio) / 2

        case "revenue", False:
            # Revenue does *not* start at 0. Need to reduce the value
            # by the min and then normalize by the range.
            ratio = (st.session_state.revenue - MIN_REVENUE) / RANGE_REVENUE
            if not st.session_state.profit_lock:
                st.session_state.profit = MAX_PROFIT * (1 - ratio) / 2

            if not st.session_state.equity_lock:
                st.session_state.equity = MAX_EQUITY * (1 - ratio) / 2

        case "equity", False:
            ratio = st.session_state.equity / MAX_EQUITY
            if not st.session_state.profit_lock:
                st.session_state.profit = MAX_PROFIT * (1 - ratio) / 2

            if not st.session_state.revenue_lock:
                st.session_state.revenue = (
                    RANGE_REVENUE * (1 - ratio) / 2 + MIN_REVENUE
                )


profit_col0, profit_col1 = st.columns([0.2, 0.8])
with profit_col0:
    profit_lock = st.checkbox(label="Lock", key="profit_lock")

with profit_col1:
    profit_share = st.slider(
        label="Profit Share",
        min_value=MIN_PROFIT,
        max_value=MAX_PROFIT,
        value=MAX_PROFIT * 1 / 3,
        step=0.1,
        format="%0.1f%%",
        key="profit",
        on_change=update,
        args=("profit", profit_lock),
        disabled=profit_lock,
    )

revenue_col0, revenue_col1 = st.columns([0.2, 0.8])
with revenue_col0:
    revenue_lock = st.checkbox(label="Lock", key="revenue_lock")

with revenue_col1:
    monthly_revenue = st.slider(
        label="Monthly Revenue",
        min_value=MIN_REVENUE,
        max_value=MAX_REVENUE,
        value=int(
            round((MAX_REVENUE - MIN_REVENUE) * 1 / 3, -3) + MIN_REVENUE
        ),
        step=100,
        key="revenue",
        on_change=update,
        args=("revenue", revenue_lock),
        disabled=revenue_lock,
    )

equity_col0, equity_col1 = st.columns([0.2, 0.8])
with equity_col0:
    equity_lock = st.checkbox(label="Lock", key="equity_lock")

with equity_col1:
    equity = st.slider(
        label="Equity",
        min_value=MIN_EQUITY,
        max_value=MAX_EQUITY,
        value=(MAX_EQUITY - MIN_EQUITY) * 1 / 3,
        step=0.1,
        format="%0.1f%%",
        key="equity",
        on_change=update,
        args=("equity", equity_lock),
        disabled=equity_lock,
    )
