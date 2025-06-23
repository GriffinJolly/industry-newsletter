import streamlit as st

# --- Sidebar ---
st.sidebar.title("Sector Newsletter Generator")

# Sector selection (multi-select)
sectors = ["Technology", "Healthcare", "Finance", "Energy", "Consumer Goods"]
selected_sectors = st.sidebar.multiselect("Select Sectors", sectors)

# Optional filters
date_range = st.sidebar.date_input("Date Range", [])
region = st.sidebar.text_input("Region (optional)")
insight_types = ["M&A", "Innovation", "Partnerships", "Expansions"]
selected_types = st.sidebar.multiselect("Insight Types", insight_types)

# Generate button
if st.sidebar.button("Generate Newsletter"):
    st.session_state['generating'] = True
    st.write("Generating newsletter... (pipeline not yet implemented)")
    # TODO: Call main pipeline
else:
    st.session_state['generating'] = False

# Progress/status log
if st.session_state.get('generating', False):
    st.progress(0.1)
    st.info("Fetching data...")
    # TODO: Update progress as pipeline runs

# Download button (disabled for now)
st.button("Download .pptx", disabled=True)
