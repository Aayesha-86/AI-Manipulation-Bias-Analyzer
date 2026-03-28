import streamlit as st
from transformers import pipeline

st.title("AI Manipulation & Bias Analyzer")

st.write("Analyze digital text to detect emotional influence and bias patterns.")

text = st.text_area("Enter text to analyze")

classifier = pipeline("sentiment-analysis")

if st.button("Analyze"):

    result = classifier(text)

    sentiment = result[0]['label']
    score = result[0]['score']

    st.subheader("Analysis Result")

    st.write("Sentiment:", sentiment)
    st.write("Confidence Score:", round(score,2))

    if score > 0.80:
        st.write("Manipulation Risk: High emotional influence detected")
    else:
        st.write("Manipulation Risk: Low")