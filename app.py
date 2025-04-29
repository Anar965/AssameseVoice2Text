import streamlit as st
import tempfile
import os
import time
from utils import record_audio, transcribe_audio
from icons import display_icons_and_images
from assamese_alphabet import display_assamese_alphabet
from background import display_background, apply_background_style

# Page configuration
st.set_page_config(
    page_title="Assamese Voice into Text",
    page_icon="🎤",
    layout="wide"
)

# Apply custom background styling
apply_background_style()

# Display the beautiful Assam-themed background at the top
display_background()

# Voice icon shown below the header
st.markdown("""
<div style="text-align: center; margin: 10px 0;">
    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#F63366" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path>
        <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
        <line x1="12" y1="19" x2="12" y2="23"></line>
        <line x1="8" y1="23" x2="16" y2="23"></line>
    </svg>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 1.2em;'>Convert your Assamese speech into text with ease!</p>", unsafe_allow_html=True)

# Demo version notice
st.warning("""
    **DEMO VERSION**: This is a demonstration version with simulated voice recording and transcription.
    In a production app, this would use an actual microphone and speech recognition model for Assamese language.
""")

# Initialize session state variables if they don't exist
if 'transcribed_text' not in st.session_state:
    st.session_state.transcribed_text = ""
if 'recording' not in st.session_state:
    st.session_state.recording = False
if 'temp_file' not in st.session_state:
    st.session_state.temp_file = None
if 'message' not in st.session_state:
    st.session_state.message = ""

# Function to handle recording
def start_recording():
    st.session_state.recording = True
    st.session_state.message = "Recording in progress... Speak in Assamese"
    st.session_state.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    st.rerun()

def stop_recording():
    st.session_state.recording = False
    st.session_state.message = "Processing audio..."
    st.rerun()

# Sidebar with instructions
with st.sidebar:
    st.header("Demo Instructions")
    st.markdown("""
    1. Click the **Start Recording** button
    2. In this demo version, you don't need to actually speak
    3. Click **Stop Recording** when the progress bar completes
    4. Sample Assamese text will appear in the text area
    5. Edit the text if needed
    6. Use the export options to save or copy your text
    """)
    
    st.header("About")
    st.markdown("""
    This is a demonstration version of an application that would convert Assamese speech into text. The full version would use actual speech recognition technology.
    
    **Features Demonstrated:**
    - User interface for voice-to-text conversion
    - Workflow simulation for Assamese language processing
    - Text editing capabilities
    - Export options
    """)
    
    st.header("Full Version Capabilities")
    st.markdown("""
    The full version of this application would include:
    - Real-time audio recording from microphone
    - Actual speech recognition model trained for Assamese
    - Accurate transcription of spoken Assamese
    - Additional language options
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    # Recording interface
    st.subheader("Speech Input")
    
    # Status message
    if st.session_state.message:
        status_placeholder = st.empty()
        status_placeholder.info(st.session_state.message)
    
    # Recording buttons
    if not st.session_state.recording:
        st.button("Start Recording", on_click=start_recording, type="primary", use_container_width=True)
    else:
        st.button("Stop Recording", on_click=stop_recording, type="primary", use_container_width=True)
        
        # Actually do the recording if we're in recording state
        if st.session_state.temp_file:
            progress_bar = st.progress(0)
            try:
                filename = st.session_state.temp_file.name
                record_audio(filename)
                
                # Show progress bar animation
                for i in range(100):
                    progress_bar.progress(i + 1)
                    time.sleep(0.01)
                
                # Now transcribe the audio
                st.session_state.message = "Transcribing audio..."
                transcribed_text = transcribe_audio(filename)
                if transcribed_text:
                    st.session_state.transcribed_text = transcribed_text
                    st.session_state.message = "Transcription complete!"
                else:
                    st.session_state.message = "Could not transcribe audio. Please try again."
                
                # Clean up the temp file
                try:
                    os.unlink(filename)
                except:
                    pass
                st.session_state.temp_file = None
                st.rerun()
            except Exception as e:
                st.error(f"Error during recording: {str(e)}")
                st.session_state.recording = False
                st.session_state.message = ""
                if st.session_state.temp_file:
                    try:
                        os.unlink(st.session_state.temp_file.name)
                    except:
                        pass
                    st.session_state.temp_file = None

with col2:
    # Text output and editing
    st.subheader("Text Output")
    
    # Text area for editing the transcribed text
    st.session_state.transcribed_text = st.text_area(
        "Edit transcribed text if needed:",
        value=st.session_state.transcribed_text,
        height=200
    )
    
    # Export options
    if st.session_state.transcribed_text:
        st.subheader("Export Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Copy to Clipboard", use_container_width=True):
                # Display copy success message
                st.info("Text copied to clipboard! (This is a simulation in the demo version)")
                
                # In a real application, we would use a proper clipboard mechanism
                # But we'll skip the JavaScript that was causing errors
        
        with col2:
            if st.download_button(
                label="Save as Text File",
                data=st.session_state.transcribed_text,
                file_name="assamese_text.txt",
                mime="text/plain",
                use_container_width=True
            ):
                st.success("File downloaded successfully!")

# Cultural elements section with colorful heading
st.markdown("---")
st.markdown("""
<h2 style="text-align: center; color: #D32F2F; text-shadow: 1px 1px 2px #00000050; 
              background-color: #f8f8f8; padding: 10px; border-radius: 5px;
              border-left: 5px solid #D32F2F; border-right: 5px solid #D32F2F;">
    অসমীয়া সংস্কৃতি (Assamese Cultural Heritage)
</h2>
""", unsafe_allow_html=True)

# Display the cultural elements with a more streamlined approach
st.markdown('<div style="background-color: #f8f8f8; padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0; margin: 20px 0;">', unsafe_allow_html=True)
display_icons_and_images()
st.markdown('</div>', unsafe_allow_html=True)

# Display the Assamese alphabet with a simplified container
st.markdown('<div style="background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">', unsafe_allow_html=True)
display_assamese_alphabet()
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Assamese Voice into Text - Convert your Assamese speech to text with ease")
