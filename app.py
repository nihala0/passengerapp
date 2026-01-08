import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Passenger Demand Prediction",
    layout="wide"
)

# Title
st.title("🚍 Passenger Demand Prediction Dashboard")
st.write("User Interface for Passenger Demand Analysis")

st.markdown("---")

# Top section – Small
col1, col2 = st.columns(2)

with col1:
    st.subheader("Passenger Count")
    st.metric(label="Total Passengers", value="---")

with col2:
    st.subheader("Passenger Demand by Hour")
    st.line_chart([])  # Placeholder chart

st.markdown("---")

# Bottom section – Large
col3, col4 = st.columns(2)

with col3:
    st.subheader("High Demand Routes")
    st.bar_chart([])  # Placeholder chart

with col4:
    st.subheader("Weekday vs Weekend Passenger Demand")
    st.bar_chart([])  # Placeholder chart

st.markdown("---")

st.caption("This interface is built using Streamlit and Python.")
