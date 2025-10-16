🚀 Internship Tracker - Abinaya Rajasekara (Data/AI Enthusiast)














A smart and interactive Streamlit web app to help you manage internship applications, analyze your resume against job descriptions using NLP & TF-IDF, and gain insights into your job readiness — all from one dashboard.

<p align="center"> <img src="assets/internship_dashboard_preview.webp" width="720" alt="Internship Tracker Dashboard Preview"/> </p>
✨ Features

📋 Add, view, and filter internship applications

📅 Automatically highlight upcoming deadlines

📊 Visualize progress with status charts

🧠 Analyze resume–job description match using TF-IDF

📤 Upload .txt files for resume and JD comparison

💾 Download internship data as CSV

💡 Career tips to strengthen your professional profile

🛠️ Tools & Technologies

Python 3.11

Streamlit — Interactive UI Framework

Pandas — Data Handling & Management

Scikit-learn — TF-IDF Vectorization

spaCy — Keyword Extraction (NLP)

Matplotlib — Chart Visualization

VS Code Dev Container — for isolated environment setup

🧩 How It Works

Add your internships (Company, Role, Deadline, Status).

Paste or upload your resume and job description.

The app computes a TF-IDF similarity score.

spaCy extracts keywords to show strengths & gaps.

View results, insights, and download your data instantly.

📁 Folder Structure
internship-tracker-abinaya/
│
├── internship_tracker.py        # Main Streamlit App
├── requirements.txt             # Dependencies
├── .devcontainer/
│   └── devcontainer.json        # VS Code container setup
├── assets/                      # (Optional) images/icons
└── README.md                    # Documentation

🧠 Resume Analyzer Logic
Step	Functionality	Description
1️⃣	TF-IDF Similarity	Compares resume & JD textual overlap
2️⃣	Keyword Extraction	Identifies strong nouns & skills
3️⃣	Match Score	Displays similarity score with insights
4️⃣	Feedback	Recommends how to improve alignment
📊 Dashboard Insights

📝 Applications Submitted

📞 Interviews in Progress

🏆 Offers Received

⏰ Upcoming Deadlines

Everything updates dynamically as you track your journey!

🧠 Common Issues & Fixes
<details> <summary>Click to expand</summary>
Step	Issue	Cause	Solution
1	spaCy model missing	Model not downloaded	Run: python -m spacy download en_core_web_sm
2	TF-IDF error	Missing text input	Provide both resume & JD text
3	Streamlit crash	Incorrect form indentation	Check block structure
4	Chart empty	No applications added	Add entries before viewing chart
5	CSV not downloading	Session cache reset	Restart Streamlit session
</details>
📈 Future Enhancements
<details> <summary>Click to expand</summary>

💾 Persistent storage via SQLite or Firebase

📧 Email reminders for upcoming deadlines

📄 Resume PDF parsing & keyword highlighting

🤖 AI-based resume enhancement feedback

☁️ Cloud deployment (Streamlit Cloud / Hugging Face Spaces)

</details>
👩‍💻 Author

Abinaya Rajasekara
🎓 Data & AI Enthusiast | 💼 Internship Project Developer
🌱 Passionate about NLP, ML, and practical AI tools for students

🔗 LinkedIn

🐙 GitHub

📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it — with proper credit.

⭐ Support

If you like this project, please ⭐ star the repository →
github.com/abinaya-232001/internship-tracker-abinaya

Your support inspires more open-source projects like this 💙
