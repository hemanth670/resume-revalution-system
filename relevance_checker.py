# ------------------------------------------------------------
# © 2025 SR
# Resume Relevance Check System
# All rights reserved. Unauthorized copying, modification,
# or distribution of this file is prohibited.
# ------------------------------------------------------------
def keyword_match_score(resume_text, jd_text):
    """
    Computes keyword matching score between resume and job description using TF-IDF cosine similarity.
    Returns a float score between 0 and 1.
    """
    vectorizer = TfidfVectorizer().fit([resume_text, jd_text])
    vectors = vectorizer.transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(float(score), 3)

# ...existing code...
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained model (you can choose others)
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match_score(resume_text, jd_text):
    """
    Computes semantic similarity score between resume and job description using embeddings.
    Returns a float score between 0 and 1.
    """
    resume_emb = model.encode([resume_text])
    jd_emb = model.encode([jd_text])
    score = cosine_similarity(resume_emb, jd_emb)[0][0]
    return round(float(score), 3)

# ...existing code...
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_skills(text):
    skills_pattern = r"(Python|Java|SQL|TensorFlow|PyTorch|Docker|Kubernetes|Spring Boot|Pandas|NumPy)"
    return re.findall(skills_pattern, text, re.IGNORECASE)

def compute_relevance(resume_text, jd_text):
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))
    matched_skills = resume_skills & jd_skills
    hard_score = (len(matched_skills) / max(len(dj_skills:=jd_skills), 1)) * 50  # 50% weight

    vectorizer = TfidfVectorizer().fit([resume_text, jd_text])
    vectors = vectorizer.transform([resume_text, jd_text])
    soft_score = cosine_similarity(vectors[0], vectors[1])[0][0] * 50  # 50% weight

    total_score = round(hard_score + soft_score, 2)

    if total_score >= 75:
        verdict = "High"
    elif total_score >= 50:
        verdict = "Medium"
    else:
        verdict = "Low"

    missing_items = list(dj_skills - resume_skills)
    return total_score, verdict, missing_items
import spacy

# Load spaCy model globally for efficiency
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """
    Extracts entities (skills, organizations, etc.) from text using spaCy.
    Returns a list of entities.
    """
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    return entities

# ...existing code...
def weighted_score(keyword_score, semantic_score, alpha=0.5):
    """
    Combines keyword and semantic scores into a final weighted score.
    alpha: weight for keyword_score (0 to 1). Default is 0.5 (equal weight).
    Returns a float score between 0 and 1.
    """
    final = alpha * keyword_score + (1 - alpha) * semantic_score
    return round(final, 3)

# ...existing code...
