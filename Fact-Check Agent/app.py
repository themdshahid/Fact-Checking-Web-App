import streamlit as st

from services.pdf_reader import extract_text_from_pdf
from services.claim_extractor import extract_claims
from services.web_search import search_claim
from services.verifier import verify_claim
from utils.helpers import create_results_dataframe

st.set_page_config(page_title="AI Fact Checker", layout="wide")

st.title("🕵️ AI Fact-Checking Web App")
st.write("Upload a PDF and verify claims against live web data.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("Reading PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF loaded successfully.")

    with st.spinner("Extracting factual claims..."):
        claims = extract_claims(pdf_text)

    st.subheader("Extracted Claims")

    for i, claim in enumerate(claims, start=1):
        st.write(f"{i}. {claim}")

    results = []

    if st.button("Start Fact Checking"):
        progress_bar = st.progress(0)

        for idx, claim in enumerate(claims):
            st.write("---")
            st.subheader(f"Checking Claim {idx + 1}")

            st.write(f"**Claim:** {claim}")

            with st.spinner("Searching live web..."):
                web_data = search_claim(claim)

            with st.spinner("Verifying claim..."):
                verification = verify_claim(claim, web_data)

            st.write(verification)

            results.append({
                "claim": claim,
                "result": verification
            })

            progress_bar.progress((idx + 1) / len(claims))

        st.success("Fact-checking completed.")

        df = create_results_dataframe(results)

        st.subheader("Summary")
        st.dataframe(df, use_container_width=True)