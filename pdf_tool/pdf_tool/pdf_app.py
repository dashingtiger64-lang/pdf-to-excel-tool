import streamlit as st
import pandas as pd
import tabula

# Title & description
st.title("🚀 Smart PDF to Excel Converter")
st.write("Upload your PDF and convert it into clean Excel instantly")
st.info("⚡ Fast | 📊 Clean Data | 🤖 AI Powered")

# File upload
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    tables = tabula.read_pdf("temp.pdf", pages="all", multiple_tables=True)

    if tables:
        df = pd.concat(tables)
        st.write(df)

        df.to_excel("output.xlsx", index=False)

        with open("output.xlsx", "rb") as f:
            st.download_button("Download Excel", f, file_name="output.xlsx")
    else:
        st.warning("No tables found in PDF")

# Footer (your name)
st.markdown(
    "<p style='text-align:center; font-size:12px; color:gray;'>Made with ❤️ by Harshit</p>",
    unsafe_allow_html=True
)

