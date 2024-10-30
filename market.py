import streamlit as st
import google.generativeai as genai

# Configure Gemini AI API
genai.configure(api_key="AIzaSyBENnC8mfXMCC8kZ8TBJ9eNrT7gYo-37K0")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to generate marketing copy using Gemini AI
def generate_marketing_copy(product_name, product_features, tone, audience):
    prompt = (
        f"Generate a marketing copy for a product called '{product_name}'. "
        f"Here are the product features: {product_features}. "
        f"The tone should be {tone} and the target audience is {audience}."
        "Generate a photo of the product"
    )
    
    response = model.generate_content([prompt])
    return response.text

# Streamlit App Interface
st.title("AI Marketing Copy Generator")

# Collecting user input for product details
product_name = st.text_input("Product Name", "Smartphone X")
product_features = st.text_area("Product Features", "High resolution display, long battery life, fast charging")
tone = st.selectbox("Tone of Copy", ["Friendly", "Professional", "Casual", "Persuasive"])
audience = st.text_input("Target Audience", "Tech enthusiasts")

# Button to generate marketing copy
if st.button("Generate Marketing Copy"):
    if product_name and product_features and tone and audience:
        with st.spinner("Generating copy..."):
            copy = generate_marketing_copy(product_name, product_features, tone, audience)
        st.subheader("Generated Marketing Copy")
        st.write(copy)
    else:
        st.error("Please fill in all the fields.")

# Optional additional feedback feature
st.text_area("Feedback on Generated Copy", "")
st.button("Submit Feedback")

