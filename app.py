import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_3D_model(area):
    side_length = np.sqrt(area)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = [0, side_length, side_length, 0, 0]
    y = [0, 0, side_length, side_length, 0]
    z = [0, 0, 0, 0, 0]
    ax.plot(x, y, z, color='b')
    
    for i in range(4):
        ax.plot([x[i], x[i]], [y[i], y[i]], [0, side_length], color='b')
    
    z_top = [side_length] * 5
    ax.plot(x, y, z_top, color='b')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Architecture Model')
    
    st.pyplot(fig)

def suggest_colors(area):
    if area < 500:
        return ["Light Blue", "Pastel Green", "Soft Yellow"]
    elif area < 1000:
        return ["Coral", "Peach", "Lavender"]
    else:
        return ["Royal Blue", "Forest Green", "Goldenrod"]

st.title("3D Architecture and Color Suggestion App")
area_input = st.number_input("Enter the land area (in square feet):", min_value=1, step=1)

if st.button("Generate"):
    generate_3D_model(area_input)
    colors = suggest_colors(area_input)
    st.write("Suggested Colors for Your Home:")
    st.write(", ".join(colors))
