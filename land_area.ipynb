# Create app.py file
%%writefile app.py
import streamlit as st
from transformers import pipeline
import numpy as np
import matplotlib.pyplot as plt
from stl import mesh  # For 3D structures in STL format

# Hugging Face Models
architecture_model = pipeline("text-to-image", model="CompVis/stable-diffusion-v1-4")  # Placeholder model
color_model = pipeline("image-segmentation", model="facebook/detectron2")  # Placeholder for color suggestion

# Streamlit Interface - Main Title and UI
st.markdown("<h1 style='text-align: center; color: #FF5733;'>3D Home Architecture and Color Recommendation App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #33A1FF;'>Enter your land area to generate a 3D layout and color scheme</h2>", unsafe_allow_html=True)

# Input for land area
land_area = st.text_input("Enter land area (feet/inches):")

# Handle the 3D architecture generation and color suggestion
if land_area:
    st.markdown(f"<h3 style='color: #FF33A6;'>Generated 3D Home Design for {land_area} Feet Area:</h3>", unsafe_allow_html=True)
    
    # Generate 3D architecture model using Hugging Face model
    prompt = f"Generate a 3D model of a home for {land_area} feet area"
    result = architecture_model(prompt)
    
    # Display the generated 3D design
    st.image(result[0]['image'], caption="Generated 3D Home Design")
    
    # Generate and display suggested colors for the home
    st.markdown("<h3 style='color: #33A1FF;'>Suggested Colors for Home Interior:</h3>", unsafe_allow_html=True)
    color_suggestion = color_model("input_image.jpg")  # Replace 'input_image.jpg' with actual image
    st.write(color_suggestion)

# Colorful UI Section - Graph with Vibrant Colors
st.markdown("<h2 style='text-align: center; color: #FF5733;'>Vibrant Graph with Colorful Lines</h2>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px; color:#28B463;'>This graph showcases a sine and cosine wave with different colors.</p>", unsafe_allow_html=True)

# Generate and plot sine and cosine waves
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a colorful plot
fig, ax = plt.subplots()
ax.plot(x, y1, label='Sine Wave', color='#FF5733', linewidth=2.5)  # Orange
ax.plot(x, y2, label='Cosine Wave', color='#33A1FF', linewidth=2.5)  # Blue

# Customize graph title, labels, and grid
ax.set_title('Sine and Cosine Waves', fontsize=16, color='#FF5733')
ax.set_xlabel('X-axis', fontsize=14, color='#33A1FF')
ax.set_ylabel('Y-axis', fontsize=14, color='#33A1FF')
ax.grid(True, color='#D3D3D3', linestyle='--', linewidth=1)
ax.legend()

# Display the graph in Streamlit
st.pyplot(fig)

# Footer description for graph explanation
st.markdown("<h3 style='color: #FF33A6;'>Graph Explanation:</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size:16px; color:#884EA0;'>The sine wave is represented in orange, and the cosine wave is in blue.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5D6D7E;'>This is a demonstration of a colorful Streamlit app.</p>", unsafe_allow_html=True)
