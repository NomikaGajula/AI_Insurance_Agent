import streamlit as st

# st.markdown(
#                f"""
#                <div style="
#                    background-color: #f0f2f6;
#                    padding: 10px;
#                    border-left: 5px solid #4a90e2;
#                    border-radius: 5px;
#                    margin-bottom: 10px;
#                ">
#                    <strong>Title:</strong> {title}
#                </div>
#                """,
#                unsafe_allow_html=True
#            )
def home_page():
    st.title("Insurance News Dashboard")
    st.markdown("""
    Welcome to the **Insurance News Dashboard**. This app helps you track the latest news and insights from the world of **Insurance**.
    
    Select a domain below to get started!
    """)
    # Navigation
    selected_domain = st.selectbox(
        "Select Domain",
        ["-- Select Domain --","Climate Risk", "InsureTech", "Policies", "Business Exposure"]
    )
    # escaped_domain = escape_markdown(selected_domain)
    
    # Display news based on selected domain
    if selected_domain != "-- Select Domain --":
        # st.write(f"**Showing news for {selected_domain}**")
        st.markdown(
    f"""
    <div style="
        font-size: 20px;
        font-weight: 600;
        color: #333333;
        padding: 8px 4px;
        border-bottom: 1px solid #dddddd;
        margin-bottom: 20px;
    ">
        Showing news for {selected_domain}
    </div>
    """,
    unsafe_allow_html=True
)

        # st.write(f"### Showing news for **{selected_domain}**")
    else:
        st.warning("Please select a domain to continue.")
    # if selected_domain:
        # st.markdown(f"### Showing news for **{selected_domain}**")
        # display_news(selected_domain)
home_page()