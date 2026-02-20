# 📊 Customer Sentiment Analysis Bot
**An AI-powered dashboard for classifying customer feedback and instantly flagging urgent service complaints.**

## 📌 Project Overview
In fast-paced business environments, support teams are often overwhelmed by volume. This application acts as a "First Responder" agent, using **Gemini 3 Flash** to parse feedback, identify the emotional tone, and prioritize issues that require immediate human intervention.

### 🚀 Key Features
- **Dual-Task Processing:** Simultaneously classifies **Sentiment** (Positive/Neutral/Negative) and **Urgency** (Low/Medium/High).
- **Smart Urgency Flagging:** Automatically triggers a high-visibility alert for critical issues like delivery failures or technical outages.
- **Actionable Insights:** Provides a concise 1-sentence summary and a suggested "Next Step" for the support agent.
- **Modern Dashboard:** Built with Streamlit for a responsive, professional user experience.

---

## 🛠️ Tech Stack
- **Web Framework:** [Streamlit](https://streamlit.io/)
- **AI Engine:** [Google Gemini API](https://aistudio.google.com/) (Model: `gemini-3-flash-preview`)
- **Language:** Python 3.10+

---

## 🏗️ How it Works
1. **Feedback Input:** Support agents or automated systems paste raw customer text into the dashboard.
2. **Contextual Analysis:** The AI evaluates the language for frustration levels, keywords indicating urgency, and core intent.
3. **Automated Flagging:** If a complaint is deemed "High Urgency," the UI dynamically changes to alert the user.

---

## 🏃 Installation & Setup

### 1. Clone & Environment
```bash
git clone [https://github.com/palak317/sentiment-analyser.git](https://github.com/palak317/sentiment-analyser.git)
cd sentiment-analyser
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
