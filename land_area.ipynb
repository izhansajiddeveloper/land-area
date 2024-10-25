import streamlit as st
import matplotlib.pyplot as plt
from transformers import pipeline

def generate_2D_layout(area):
    # Define the areas for different rooms
    bedroom_area = area * 0.3  # 30% for bedroom
    washroom_area = area * 0.1  # 10% for washroom
    kitchen_area = area * 0.2   # 20% for kitchen
    parking_area = area * 0.4   # 40% for car parking

    # Calculate dimensions (for simplicity, we assume square rooms)
    bedroom_size = bedroom_area ** 0.5
    washroom_size = washroom_area ** 0.5
    kitchen_size = kitchen_area ** 0.5
    parking_size = parking_area ** 0.5

    # Create the 2D layout
    fig, ax = plt.subplots()

    # Plotting the rooms
    ax.add_patch(plt.Rectangle((0, 0), bedroom_size, bedroom_size, color='skyblue', label='Bedroom'))
    ax.add_patch(plt.Rectangle((0, bedroom_size), washroom_size, washroom_size, color='lightcoral', label='Washroom'))
    ax.add_patch(plt.Rectangle((bedroom_size, 0), kitchen_size, kitchen_size, color='lightgreen', label='Kitchen'))
    ax.add_patch(plt.Rectangle((bedroom_size, kitchen_size), parking_size, parking_size, color='lightyellow', label='Car Parking'))

    # Set limits and labels
    ax.set_xlim(0, max(bedroom_size, kitchen_size + parking_size))
    ax.set_ylim(0, max(bedroom_size + washroom_size, kitchen_size))
    ax.set_xlabel('Width (ft)')
    ax.set_ylabel('Length (ft)')
    ax.set_title('2D House Layout')
    ax.legend()

    st.pyplot(fig)

def generate_description(area):
    # Load a text generation model from Hugging Face
    generator = pipeline('text-generation', model='gpt2')  # You can change 'gpt2' to any other model available on Hugging Face
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

if st.button("Generate"):
    generate_2D_layout(area_input)
    colors = suggest_colors(area_input)
    st.write("Suggested Colors for Your Home:")
    st.write(", ".join(colors))
    
    # Generate and display a description using Hugging Face model
    description = generate_description(area_input)
    st.write("Generated Description:")
    st.write(description)
