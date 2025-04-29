"""
SVG icons and images for the Streamlit app.
"""
import streamlit as st

def voice_icon():
    """Return the SVG code for a voice/microphone icon."""
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#F63366" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path>
        <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
        <line x1="12" y1="19" x2="12" y2="23"></line>
        <line x1="8" y1="23" x2="16" y2="23"></line>
    </svg>
    """

def bihu_dancer_svg():
    """Return an SVG representation of a Bihu dancer."""
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="300" height="250" viewBox="0 0 300 250">
        <!-- Colorful background representing Assam's vibrant culture -->
        <rect width="300" height="250" fill="#f8f8f8" stroke="#ccc" stroke-width="1" rx="5" ry="5" />
        
        <!-- Title -->
        <text x="150" y="30" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle" fill="#333">
            বিহু নৃত্য (Bihu Dance)
        </text>
        
        <!-- Group of 3 dancers -->
        <g transform="translate(150, 125) scale(0.8)">
            <!-- Dancer 1 (left) -->
            <g transform="translate(-80, 0)">
                <!-- Head -->
                <circle cx="0" cy="-60" r="15" fill="#F6C285" />
                
                <!-- Traditional headgear (Japi) -->
                <path d="M-30 -65 Q 0 -100 30 -65" stroke="#8B4513" fill="#f2d59e" stroke-width="3" />
                
                <!-- Body - with traditional colorful attire -->
                <rect x="-20" y="-45" width="40" height="50" fill="#FF6633" rx="5" ry="5" />
                
                <!-- Dhoti/traditional lower garment -->
                <path d="M-20 5 L-30 50 L30 50 L20 5 Z" fill="#FFFFFF" />
                
                <!-- Gamosa (traditional red and white cloth) -->
                <path d="M-20 -35 L-30 -15 L30 -15 L20 -35 Z" fill="#FF5252" />
                <path d="M-25 -25 L-20 -20 M-15 -25 L-10 -20 M-5 -25 L0 -20 M5 -25 L10 -20 M15 -25 L20 -20" stroke="#FFFFFF" stroke-width="2" />
                
                <!-- Arms in dancing position -->
                <path d="M-20 -35 L-40 -20 L-45 0" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                <path d="M20 -35 L40 -20 L45 0" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                
                <!-- Legs in dancing position -->
                <path d="M-10 5 L-20 40" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                <path d="M10 5 L25 30" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
            </g>
            
            <!-- Dancer 2 (center) - in a different pose -->
            <g transform="translate(0, 0)">
                <!-- Head -->
                <circle cx="0" cy="-65" r="15" fill="#F6C285" />
                
                <!-- Traditional headgear (Japi) -->
                <path d="M-30 -70 Q 0 -105 30 -70" stroke="#8B4513" fill="#f2d59e" stroke-width="3" />
                
                <!-- Body - with traditional colorful attire -->
                <rect x="-20" y="-50" width="40" height="50" fill="#44AA66" rx="5" ry="5" />
                
                <!-- Dhoti/traditional lower garment -->
                <path d="M-20 0 L-25 45 L25 45 L20 0 Z" fill="#FFFFFF" />
                
                <!-- Gamosa (traditional red and white cloth) -->
                <path d="M-20 -40 L-30 -20 L30 -20 L20 -40 Z" fill="#FF5252" />
                <path d="M-25 -30 L-20 -25 M-15 -30 L-10 -25 M-5 -30 L0 -25 M5 -30 L10 -25 M15 -30 L20 -25" stroke="#FFFFFF" stroke-width="2" />
                
                <!-- Arms in dancing position - different pose -->
                <path d="M-20 -40 L-45 -30 L-50 -10" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                <path d="M20 -40 L45 -30 L50 -10" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                
                <!-- Legs in dancing position - different pose -->
                <path d="M-10 0 L-15 30 L-5 45" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                <path d="M10 0 L15 30 L5 45" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
            </g>
            
            <!-- Dancer 3 (right) -->
            <g transform="translate(80, 0)">
                <!-- Head -->
                <circle cx="0" cy="-60" r="15" fill="#F6C285" />
                
                <!-- Traditional headgear (Japi) -->
                <path d="M-30 -65 Q 0 -100 30 -65" stroke="#8B4513" fill="#f2d59e" stroke-width="3" />
                
                <!-- Body - with traditional colorful attire -->
                <rect x="-20" y="-45" width="40" height="50" fill="#5588DD" rx="5" ry="5" />
                
                <!-- Dhoti/traditional lower garment -->
                <path d="M-20 5 L-30 50 L30 50 L20 5 Z" fill="#FFFFFF" />
                
                <!-- Gamosa (traditional red and white cloth) -->
                <path d="M-20 -35 L-30 -15 L30 -15 L20 -35 Z" fill="#FF5252" />
                <path d="M-25 -25 L-20 -20 M-15 -25 L-10 -20 M-5 -25 L0 -20 M5 -25 L10 -20 M15 -25 L20 -20" stroke="#FFFFFF" stroke-width="2" />
                
                <!-- Arms in dancing position - mirror of first dancer -->
                <path d="M-20 -35 L-45 -15 L-40 10" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                <path d="M20 -35 L45 -15 L40 10" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                
                <!-- Legs in dancing position - mirror of first dancer -->
                <path d="M-10 5 L-25 30" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
                <path d="M10 5 L20 40" stroke="#F6C285" fill="none" stroke-width="10" stroke-linecap="round" />
            </g>
        </g>
        
        <!-- Bihu instruments -->
        <g transform="translate(50, 210)">
            <!-- Dhol (drum) -->
            <rect x="0" y="0" width="40" height="20" fill="#8B4513" rx="2" ry="2" />
            <rect x="0" y="0" width="40" height="4" fill="#D2B48C" />
            <rect x="0" y="16" width="40" height="4" fill="#D2B48C" />
            <text x="20" y="35" font-family="Arial" font-size="10" text-anchor="middle" fill="#333">ঢোল (Dhol)</text>
        </g>
        
        <!-- Pepa (horn) -->
        <g transform="translate(130, 210)">
            <path d="M0 0 C5 5, 10 15, 0 20 L 10 25 L 15 15 L 5 -5 Z" fill="#8B4513" />
            <text x="10" y="35" font-family="Arial" font-size="10" text-anchor="middle" fill="#333">পেঁপা (Pepa)</text>
        </g>
        
        <!-- Gogona (musical instrument) -->
        <g transform="translate(200, 210)">
            <rect x="0" y="5" width="30" height="5" fill="#8B4513" rx="1" ry="1" />
            <path d="M15 5 L15 15" stroke="#8B4513" stroke-width="2" />
            <circle cx="15" cy="18" r="3" fill="#8B4513" />
            <text x="15" y="35" font-family="Arial" font-size="10" text-anchor="middle" fill="#333">গোগনা (Gogona)</text>
        </g>
        
        <!-- Caption -->
        <text x="150" y="240" font-family="Arial" font-size="10" text-anchor="middle" fill="#333">
            Bihu Dance - Assam's Cultural Heritage
        </text>
    </svg>
    """

def assam_landscape_svg():
    """Return an SVG representation of Assam's landscape with tea gardens and the Brahmaputra river."""
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="150" height="100" viewBox="0 0 150 100">
        <!-- Sky background -->
        <rect width="150" height="100" fill="#87CEEB" />
        
        <!-- Sun -->
        <circle cx="30" cy="20" r="10" fill="#FFD700" />
        
        <!-- Brahmaputra river -->
        <path d="M0 60 Q 40 50 80 65 Q 120 80 150 70" fill="#4682B4" />
        
        <!-- Hills in the background -->
        <path d="M0 40 Q 15 20 30 40 Q 45 30 60 45 Q 75 25 90 40 L 90 60 L 0 60 Z" fill="#6B8E23" />
        
        <!-- Tea gardens represented as rows -->
        <g transform="translate(0, 70)">
            <path d="M10 0 L 140 0" stroke="#006400" stroke-width="1" />
            <path d="M10 5 L 140 5" stroke="#006400" stroke-width="1" />
            <path d="M10 10 L 140 10" stroke="#006400" stroke-width="1" />
            <path d="M10 15 L 140 15" stroke="#006400" stroke-width="1" />
            <!-- Tea bushes represented as small circles -->
            <g fill="#228B22">
                <circle cx="20" cy="0" r="2" />
                <circle cx="40" cy="0" r="2" />
                <circle cx="60" cy="0" r="2" />
                <circle cx="80" cy="0" r="2" />
                <circle cx="100" cy="0" r="2" />
                <circle cx="120" cy="0" r="2" />
                
                <circle cx="30" cy="5" r="2" />
                <circle cx="50" cy="5" r="2" />
                <circle cx="70" cy="5" r="2" />
                <circle cx="90" cy="5" r="2" />
                <circle cx="110" cy="5" r="2" />
                <circle cx="130" cy="5" r="2" />
                
                <circle cx="20" cy="10" r="2" />
                <circle cx="40" cy="10" r="2" />
                <circle cx="60" cy="10" r="2" />
                <circle cx="80" cy="10" r="2" />
                <circle cx="100" cy="10" r="2" />
                <circle cx="120" cy="10" r="2" />
                
                <circle cx="30" cy="15" r="2" />
                <circle cx="50" cy="15" r="2" />
                <circle cx="70" cy="15" r="2" />
                <circle cx="90" cy="15" r="2" />
                <circle cx="110" cy="15" r="2" />
                <circle cx="130" cy="15" r="2" />
            </g>
        </g>
        
        <!-- Text label -->
        <text x="75" y="95" font-family="Arial" font-size="8" text-anchor="middle" fill="#333">Assam - Land of the Brahmaputra & Tea Gardens</text>
    </svg>
    """

def display_icons_and_images():
    """Display the icons and images in the Streamlit app."""
    # Simpler implementation without complex HTML/JavaScript
    
    # Section headers
    st.subheader("Voice & Language")
    
    # Simple columns
    col1, col2 = st.columns(2)
    
    # Voice icon section - simplified
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Speaker_Icon.svg/500px-Speaker_Icon.svg.png", width=80)
        st.markdown("##### Voice Recording")
    
    # Language indicator
    with col2:
        st.markdown("##### অসমীয়া (Assamese)")
        st.markdown("Traditional language of Assam, India")
    
    # Cultural header
    st.subheader("Assam's Cultural Heritage")
    
    # Information about Bihu dance
    st.markdown("""
    #### Bihu Dance (বিহু নৃত্য)
    Bihu is a traditional folk dance from Assam performed during the Bihu festival, 
    especially during Bohag Bihu in mid-April. The dancers wear traditional colorful 
    Assamese attire, including the dhoti, gamosa, and mekhela chador.
    
    #### Traditional Instruments
    - **Dhol (ঢোল)**: A cylindrical drum that creates the primary rhythm
    - **Pepa (পেঁপা)**: A buffalo horn pipe that produces a distinctive sound
    - **Gogona (গোগনা)**: A bamboo instrument held between the teeth
    """)
    
    # Assam landscape description
    st.markdown("""
    #### Assam's Natural Beauty
    Assam is known for its lush landscapes featuring:
    - The mighty Brahmaputra River flowing through the region
    - Vast tea gardens producing world-famous Assam tea
    - Rich biodiversity including the one-horned rhinoceros
    """)
    
    # Image description (instead of directly embedding)
    st.info("In a fully deployed application, this section would display beautiful illustrations of Bihu dancers and Assamese landscapes.")