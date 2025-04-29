"""
Assamese alphabet data and display functions for the Streamlit app.
"""
import streamlit as st

def get_color_for_letter(letter_index):
    """
    Return a color for the letter based on its index.
    Colors match the shared image style.
    """
    colors = [
        "#00AA55",  # Green
        "#0099CC",  # Light blue
        "#9900CC",  # Purple
        "#332288",  # Dark blue
        "#CC3311",  # Red
        "#EE4444",  # Light red
        "#996633",  # Brown
        "#CCAA44",  # Gold
        "#3366CC",  # Blue
        "#333333",  # Dark gray
        "#9944CC",  # Violet
    ]
    return colors[letter_index % len(colors)]

def display_colorful_letter(letter, color):
    """Display a single letter in a colored grid cell in the specified color."""
    return f"""
    <div style="
        width: 100%;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #ccc;
        margin: 2px;
        background-color: white;
    ">
        <span style="
            font-size: 36px;
            font-weight: bold;
            color: {color};
        ">{letter}</span>
    </div>
    """

def display_assamese_alphabet():
    """Display the Assamese alphabet in the Streamlit app."""
    st.subheader("অসমীয়া বৰ্ণমালা (Assamese Alphabet)")
    
    # Define the Assamese alphabet by category
    vowels = ["অ", "আ", "ই", "ঈ", "উ", "ঊ", "ঋ", "এ", "ঐ", "ও", "ঔ"]
    consonants_1 = ["ক", "খ", "গ", "ঘ", "ঙ", "চ", "ছ", "জ", "ঝ", "ঞ"]
    consonants_2 = ["ট", "ঠ", "ড", "ঢ", "ণ", "ত", "থ", "দ", "ধ", "ন"]
    consonants_3 = ["প", "ফ", "ব", "ভ", "ম", "য", "ৰ", "ল", "ৱ", "শ", "ষ", "স", "হ", "ক্ষ", "ড়", "ঢ়", "য়"]
    
    # Colorful grid display similar to the shared image
    st.markdown("#### স্বৰবৰ্ণ (Vowels)")
    
    # Display vowels in a colorful grid (3 columns)
    for i in range(0, len(vowels), 3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if i+j < len(vowels):
                    color = get_color_for_letter(i+j)
                    st.markdown(display_colorful_letter(vowels[i+j], color), unsafe_allow_html=True)
    
    st.markdown("#### ব্যঞ্জনবৰ্ণ (Consonants)")
    
    # Display first set of consonants
    for i in range(0, len(consonants_1), 3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if i+j < len(consonants_1):
                    color = get_color_for_letter(i+j+5)  # Offset to get different colors
                    st.markdown(display_colorful_letter(consonants_1[i+j], color), unsafe_allow_html=True)
    
    # Display second set of consonants
    for i in range(0, len(consonants_2), 3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if i+j < len(consonants_2):
                    color = get_color_for_letter(i+j+2)  # Offset to get different colors
                    st.markdown(display_colorful_letter(consonants_2[i+j], color), unsafe_allow_html=True)
    
    # Display third set of consonants in groups of 3
    for i in range(0, len(consonants_3), 3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                if i+j < len(consonants_3):
                    color = get_color_for_letter(i+j+7)  # Offset to get different colors
                    st.markdown(display_colorful_letter(consonants_3[i+j], color), unsafe_allow_html=True)
                    
    # Show the specific letters from the image in a highlighted section
    st.markdown("#### Featured Letters (As Shown in Image)")
    
    # These are the letters shown in the image
    image_letters = [
        ["অ", "আ", "ই"],
        ["ঈ", "উ", "ঊ"],
        ["ঋ", "এ", "ঐ"],
        ["ও", "ঔ", ""]
    ]
    
    # Display the letters from the image in the same 3x4 grid layout
    for i, row in enumerate(image_letters):
        cols = st.columns(3)
        for j, letter in enumerate(row):
            with cols[j]:
                if letter:  # Skip empty cells
                    color = get_color_for_letter(i*3 + j)
                    st.markdown(display_colorful_letter(letter, color), unsafe_allow_html=True)