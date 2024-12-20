import streamlit as st
import requests
from PIL import Image
from dotenv import load_dotenv
import io
import os

# FastAPI endpoint URL
load_dotenv()
API_URL = os.getenv("API_URL")

st.title("Pneumonia Detection")

# Image upload widget
uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        # Convert image to bytes for sending to API
        img_bytes = io.BytesIO()
        image.save(img_bytes, format=image.format)
        img_bytes.seek(0)

        # Send the image to the FastAPI endpoint
        files = {"file": (uploaded_file.name, img_bytes, uploaded_file.type)}
        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            # Parse the response
            result = response.json()
            predicted_class = result["predicted_class"]
            confidence = result["confidence"]
            raw_predictions = result["predictions"]

            # Display the prediction results
            st.success(f"Prediction: {predicted_class}")
            st.info(f"Confidence: {confidence:.2%}")
            st.write(f"Raw Predictions: {raw_predictions}")
        else:
            # Handle errors
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
