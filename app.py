import openai
import streamlit as st
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the Streamlit UI
st.title("Feature Prioritization AI Agent")
st.write("Enter feature requests below, and the AI will rank them by impact.")

# Input box for user feature requests
requests = st.text_area("Enter feature requests (one per line):")

# Function to call OpenAI API for prioritization
def prioritize_features(feature_list):
    prompt = f"Rank these feature requests by impact and provide a brief reason:\n{feature_list}"
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content

# Button to process prioritization
if st.button("Prioritize Features"):
    if requests.strip():
        ranked_features = prioritize_features(requests)
        st.subheader("Prioritized Feature List:")
        st.write(ranked_features)
    else:
        st.warning("Please enter at least one feature request.")
