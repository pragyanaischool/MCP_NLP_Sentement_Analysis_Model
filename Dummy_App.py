import streamlit as st
# Create Streamlit app
st.title("PragyanAI - MCP - Case Study - Sentiment Analysis")
# Input text area
user_input = st.text_area("Enter your text here:")

# Prediction button
if st.button("Predict"):
    predicted_sentiment_label = "Positive"
    # Display predicted sentiment
    st.write(f"Predicted Sentiment: {predicted_sentiment_label}")
