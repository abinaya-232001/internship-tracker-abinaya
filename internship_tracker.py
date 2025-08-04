import streamlit as st
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# 🎨 Page config
st.set_page_config(page_title="Abinaya’s Internship Tracker", layout="wide")
st.markdown("""
    <style>
    body {font-family: 'Segoe UI'; background-color: #f5f7fa;}
    .title-style {font-size:36px;font-weight:bold;text-align:center;color:#3b82f6;padding:10px;}
    .section-header {font-size:24px;color:#14b8a6;padding-top:20px;}
    .metric-box {padding:8px;border-radius:6px;background-color:#f0f9ff;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-style">🚀 Internship Dashboard by Abinaya 👩‍💻</div>', unsafe_allow_html=True)
st.markdown("---")

# 📂 Sidebar navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
st.sidebar.header("📁 Navigation")
page = st.sidebar.radio("Select Page", ["📋 Tracker", "🧠 Analyzer", "📤 Upload"])

# 💼 Session setup
if "applications" not in st.session_state:
    st.session_state.applications = []

# 📊 Metrics
total_apps = len(st.session_state.applications)
interviews = sum(i["Status"] == "Interviewing" for i in st.session_state.applications)
offers = sum(i["Status"] == "Accepted" for i in st.session_state.applications)

st.markdown("### 📊 Your Internship Stats")
col1, col2, col3 = st.columns(3)
col1.metric("📝 Applications", total_apps)
col2.metric("📞 Interviews", interviews)
col3.metric("🏆 Offers", offers)

# 📋 Internship Tracker Page
if page == "📋 Tracker":
    st.markdown('<div class="section-header">📋 Internship Tracker</div>', unsafe_allow_html=True)

    with st.expander("➕ Add Internship"):
        with st.form("entry_form"):
            c1, c2, c3 = st.columns(3)
            company = c1.text_input("🏢 Company")
            role = c2.text_input("💼 Role")
            deadline = c3.date_input("📅 Deadline")
            status = st.selectbox("📍 Status", ["Not Applied", "Applied", "Interviewing", "Rejected", "Accepted"])
            submit = st.form_submit_button("Add")
            if submit:
                st.session_state.applications.append({
                    "Company": company,
                    "Role": role,
                    "Deadline": deadline,
                    "Status": status
                })
                st.success(f"✅ {role} at {company} added!")

    df = pd.DataFrame(st.session_state.applications)

    if not df.empty:
        st.markdown('<div class="section-header">📄 My Applications</div>', unsafe_allow_html=True)
        status_filter = st.selectbox("🔍 Filter by Status", ["All"] + df["Status"].unique().tolist())
        if status_filter != "All":
            df = df[df["Status"] == status_filter]

        st.dataframe(df.sort_values("Deadline"), use_container_width=True)

        st.markdown('<div class="section-header">⏰ Upcoming Deadlines</div>', unsafe_allow_html=True)
        upcoming = df[df["Deadline"] >= datetime.today().date()]
        st.table(upcoming.sort_values("Deadline"))

        st.markdown('<div class="section-header">📈 Status Chart</div>', unsafe_allow_html=True)
        st.bar_chart(df["Status"].value_counts())

        csv = df.to_csv(index=False)
        st.download_button("⬇️ Download CSV", data=csv, file_name="internships.csv", mime="text/csv")
    else:
        st.info("📭 No applications yet. Add your first one above!")

# 🧠 Resume Analyzer Page
elif page == "🧠 Analyzer":
    st.markdown('<div class="section-header">🧠 Resume Analyzer</div>', unsafe_allow_html=True)

    resume_text = st.text_area("📄 Paste Resume Text")
    jd_text = st.text_area("📄 Paste Job Description")

    def keyword_match(resume, jd):
        vec = TfidfVectorizer(stop_words="english")
        tfidf = vec.fit_transform([resume, jd])
        return (tfidf * tfidf.T).toarray()[0][1]

    def extract_keywords(text):
        doc = nlp(text)
        return list(set([t.text for t in doc if t.pos_ in ["PROPN", "NOUN"] and not t.is_stop]))[:10]

    if st.button("🔍 Analyze Match"):
        if resume_text.strip() and jd_text.strip():
            score = keyword_match(resume_text, jd_text)
            keywords = extract_keywords(resume_text)
            st.metric("✨ Match Score", f"{score:.2f}")
            st.markdown(f"🔑 **Top Resume Keywords:** `{', '.join(keywords)}`")

            if score >= 0.75:
                st.success("✅ Great match! You’re ready to apply.")
            elif score >= 0.5:
                st.info("🧐 Decent match. Tailor your resume for better results.")
            else:
                st.warning("⚠️ Weak match. Update your resume with keywords from the JD.")
        else:
            st.warning("📌 Paste both resume and job description to analyze.")

# 📤 Upload Page
elif page == "📤 Upload":
    st.markdown('<div class="section-header">📤 Upload Resume & JD (.txt files)</div>', unsafe_allow_html=True)

    resume_file = st.file_uploader("📎 Upload Resume", type=["txt"])
    jd_file = st.file_uploader("📎 Upload Job Description", type=["txt"])

    def keyword_match(resume, jd):
        vec = TfidfVectorizer(stop_words="english")
        tfidf = vec.fit_transform([resume, jd])
        return (tfidf * tfidf.T).toarray()[0][1]

    def extract_keywords(text):
        doc = nlp(text)
        return list(set([t.text for t in doc if t.pos_ in ["PROPN", "NOUN"] and not t.is_stop]))[:10]

    if resume_file and jd_file:
        resume_data = resume_file.read().decode("utf-8")
        jd_data = jd_file.read().decode("utf-8")

        st.text_area("📄 Resume Preview", resume_data, height=150)
        st.text_area("📄 JD Preview", jd_data, height=150)

        if st.button("📊 Analyze Uploaded Files"):
            score = keyword_match(resume_data, jd_data)
            keywords = extract_keywords(resume_data)
            st.metric("🧪 Match Score", f"{score:.2f}")
            st.markdown(f"🔑 **Top Resume Keywords:** `{', '.join(keywords)}`")

            if score >= 0.75:
                st.success("💼 Strong match! Submit your resume confidently.")
            elif score >= 0.5:
                st.info("📝 Fair match. Consider optimizing your resume.")
            else:
                st.warning("⚠️ Weak match. Focus on keyword alignment.")

# 🎓 Career Tips
st.markdown("---")
st.subheader("📢 Tips to Boost Internship Success")
st.markdown("""
- 💻 Create a portfolio on [GitHub](https://github.com/)  
- 💼 Keep your [LinkedIn](https://linkedin.com/) profile updated  
- 🧠 Add a well-written README to your projects explaining purpose and impact  
- 📝 Share posts about what you’ve built and tag potential recruiters  
- 🎓 Take courses that target your skill gaps (Python, ML, Data Viz, etc.)  
""")
