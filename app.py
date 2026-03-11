import streamlit as st

st.set_page_config(page_title="PeopleSoft Role Recertification", page_icon="✅", layout="wide")

st.title("PeopleSoft Role Recertification")
st.caption("Kennesaw State University — Security Administration")

st.markdown("""
This is a placeholder app to confirm deployment.
In the next steps, we will:
1) Load your Approved Roles file (Excel).
2) Upload Assigned Roles (CSV).
3) Compare the two and generate a pass/fail result with exports.
""")

with st.expander("Environment Check"):
    st.write("Streamlit is running correctly! We will add more features step by step.")
