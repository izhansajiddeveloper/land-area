import streamlit as st
import matplotlib.pyplot as plt
from transformers import pipeline

def generate_2D_layout(area, num_bedrooms, num_washrooms, num_gardens):
    # Define areas based on user input
    bedroom_area = (area * 0.3) / num_bedrooms if num_bedrooms > 0 else 0
    washroom_area = (area * 0.1) / num_washrooms if num_washrooms > 0 else 0
    garden_area = area * 0.2 if num_gardens > 0 else 0
    kitchen_area = area * 0.4  # Fixed area for kitchen

    # Calculate dimensions for rooms (for simplicity, we'll assume square rooms)
    bedroom_size = bedroom_area ** 0.5
    washroom_size = washroom_area ** 0.5
    kitchen_size = kitchen_area ** 0.5
    garden_size = garden_area ** 0.5

    # Create the 2D layout
    fig, ax = plt.subplots()

    # Plotting bedrooms
    for i in range(num_bedrooms):
        ax.add_patch(plt.Rectangle((0, i * bedroom_size), bedroom_size, bedroom_size, color='skyblue', label='Bedroom' if i == 0 else ""))
    
    # Plotting washrooms
    for i in range(num_washrooms):
        ax.add_patch(plt.Rectangle((bedroom_size, i * washroom_size), washroom_size, washroom_size, color='lightcoral', label='Washroom' if i == 0 else ""))
    
    # Plotting kitchen
    ax.add_patch(plt.Rectangle((0, num_bedrooms * bedroom_size), kitchen_size, kitchen_size, color='lightgreen', label='Kitchen'))
    
    # Plotting garden
    if num_gardens > 0:
        ax.add_patch(plt.Rectangle((0, (num_bedrooms + 1) * bedroom_size), garden_size, garden_size, color='lightyellow', label='Garden'))

    # Set limits and labels
    ax.set_xlim(0, max(bedroom_size, kitchen_size))
    ax.set_ylim(0, (num_bedrooms + num_washrooms + 1) * bedroom_size + kitchen_size)
    ax.set_xlabel('Width (ft)')
    ax.set_ylabel('Length (ft)')
    ax.set_title('2D House Layout')
    ax.legend()

    st.pyplot(fig)

def generate_description(area):
    # Load a text generation model from Hugging Face
    generator = pipeline('text-generation', model='gpt2')
    prompt = f"Generate a description for a house layout of area {area} square feet."
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

def suggest_colors(area):
    if area < 500:
        return ["Light Blue", "Pastel Green", "Soft Yellow"]
    elif area < 1000:
        return ["Coral", "Peach", "Lavender"]
    else:
        return ["Royal Blue", "Forest Green", "Goldenrod"]

st.title("2D House Layout and Color Suggestion App")
area_input = st.number_input("Enter the land area (in square feet):", min_value=1, step=1)
num_bedrooms = st.number_input("Enter the number of bedrooms:", min_value=0, step=1)
num_washrooms = st.number_input("Enter the number of washrooms:", min_value=0, step=1)
num_gardens = st.number_input("Enter the number of gardens:", min_value=0, step=1)

if st.button("Generate"):
    generate_2D_layout(area_input, num_bedrooms, num_washrooms, num_gardens)
    colors = suggest_colors(area_input)
    st.write("Suggested Colors for Your Home:")
    st.write(", ".join(colors))
    
    # Generate and display a description using Hugging Face model
    description = generate_description(area_input)
    st.write("Generated Description:")
    st.write(description)
