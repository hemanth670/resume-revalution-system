# ------------------------------------------------------------
# © 2025 Sarthak Raut
# Resume Relevance Check System
# All rights reserved. Unauthorized copying, modification,
# or distribution of this file is prohibited.
# ------------------------------------------------------------

# ...existing code...

import streamlit as st
from resume_parser import parse_resume, parse_jd
from relevance_checker import (
    compute_relevance,
    extract_entities,
    semantic_match_score,
    keyword_match_score,
    weighted_score
)
import pandas as pd

st.set_page_config(page_title="Automated Resume Relevance Check", layout="wide")
st.title("Automated Resume Relevance Check System")

jd_file = st.file_uploader("Upload Job Description (PDF/DOCX)", type=["pdf", "docx"])
jd_text = None
if jd_file is not None:
    jd_path = f"temp_jd.{jd_file.name.split('.')[-1]}"
    with open(jd_path, "wb") as f:
        f.write(jd_file.getbuffer())
    jd_text = parse_jd(jd_path)
    st.text_area("Job Description Text", jd_text, height=200)

resume_files = st.file_uploader(
    "Upload Resumes (PDF/DOCX) - You can select multiple files", 
    type=["pdf", "docx"], accept_multiple_files=True
)

# ...existing code...

results = []

if jd_text and resume_files:
    jd_entities = extract_entities(jd_text)
    for resume_file in resume_files:
        resume_path = f"temp_resume.{resume_file.name.split('.')[-1]}"
        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())
        
        resume_text = parse_resume(resume_path)
        resume_entities = extract_entities(resume_text)
        
        st.write("Resume Text:", resume_text)
        st.write("JD Text:", jd_text)
        
        keyword_score = keyword_match_score(resume_text, jd_text)
        semantic_score = semantic_match_score(resume_text, jd_text)
        final_score = weighted_score(keyword_score, semantic_score)
        score, verdict, missing_items = compute_relevance(resume_text, jd_text)

        st.markdown(f"**{resume_file.name} ATS Score:** {final_score}")

        results.append({
            "Resume Name": resume_file.name,
            "Keyword Score": keyword_score,
            "Semantic Score": semantic_score,
            "Weighted Score": final_score,
            "ATS Score": final_score,
            "Verdict": verdict,
            "Missing Skills/Projects/Certifications": ", ".join(missing_items) if missing_items else "None"
        })

    df_results = pd.DataFrame(results)
    st.subheader("Evaluation Results")
    st.dataframe(df_results, use_container_width=True)