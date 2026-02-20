import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="SentimentAI Bot", page_icon="📊")
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("📊 Customer Sentiment Analysis Bot")
st.write("Classify feedback and instantly flag urgent customer issues.")

# --- 2. INPUT ---
feedback = st.text_area("Paste customer feedback here:", height=200,
                        placeholder="e.g., 'My order never arrived and nobody is answering the phone!'")


def analyze_sentiment(text):
    model = genai.GenerativeModel('gemini-3-flash-preview')
    prompt = f"""
    Analyze the following customer feedback:
    "{text}"

    Provide a JSON-style response with:
    1. **Sentiment**: (Positive, Neutral, or Negative)
    2. **Urgency**: (High, Medium, or Low)
    3. **Summary**: A 1-sentence summary of the issue.
    4. **Action**: A suggested next step for the support team.

    If Urgency is 'High', explain why.
    """
    response = model.generate_content(prompt)
    return response.text


# --- 3. UI LOGIC ---
if st.button("Analyze Feedback"):
    if feedback.strip():
        with st.spinner("Analyzing customer voice..."):
            result = analyze_sentiment(feedback)

            # Displaying the result
            st.subheader("📋 Analysis Report")

            # Highlighting Urgency (UX improvement)
            if "Urgency: High" in result or "High Urgency" in result:
                st.error("🚨 URGENT COMPLAINT DETECTED")

            st.markdown(result)
            st.balloons()
    else:
        st.warning("Please enter feedback to analyze.")