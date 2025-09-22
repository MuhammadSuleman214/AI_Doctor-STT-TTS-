# AI Doctor - Multimodal Medical Assistant

An intelligent AI-powered medical assistant that combines voice recognition, image analysis, and natural language processing to provide medical insights. This project demonstrates the integration of multiple AI technologies including speech-to-text, computer vision, and text-to-speech capabilities.

## 🏥 Project Overview

The AI Doctor is a comprehensive medical consultation system that allows patients to:
- Record voice descriptions of their symptoms
- Upload medical images for analysis
- Receive AI-powered medical insights and recommendations
- Listen to doctor's responses through natural voice synthesis

## 🚀 Key Features

- **Voice Recognition**: Convert patient speech to text using advanced Whisper models
- **Medical Image Analysis**: Analyze medical images using state-of-the-art vision-language models
- **AI Medical Consultation**: Get professional medical insights from Llama-4 models
- **Natural Voice Response**: Convert doctor's text responses to natural speech
- **Interactive Web Interface**: User-friendly Gradio-based web application
- **Cross-platform Support**: Works on Windows, macOS, and Linux

## 🛠️ Technologies Used

- **AI Models**:
  - Groq API (Llama-4-scout-17b-16e-instruct for medical analysis)
  - Whisper Large V3 (Speech-to-text)
  - ElevenLabs (Text-to-speech)
  - Google TTS (Backup text-to-speech)

- **Frameworks & Libraries**:
  - Gradio (Web interface)
  - Python 3.11+
  - PyAudio (Audio recording)
  - FFmpeg (Audio processing)
  - Pydub (Audio manipulation)

## 📁 Project Structure

```
AI_Doctor/
├── brain_of_the_doctor.py      # Medical image analysis and AI consultation
├── voice_of_the_patient.py     # Audio recording and speech-to-text
├── voice_of_the_doctor.py      # Text-to-speech conversion
├── gradio_app.py               # Main web application interface
├── requirements.txt            # Python dependencies
├── Pipfile                     # Pipenv configuration
├── README.md                   # Project documentation
└── .env                        # Environment variables (API keys)
```

## 🔧 Prerequisites

Before running the project, ensure you have:

1. **Python 3.11+** installed
2. **API Keys** for:
   - Groq API (for LLM and Whisper)
   - ElevenLabs API (for premium TTS)
3. **System Dependencies**:
   - FFmpeg (for audio processing)
   - PortAudio (for microphone access)

## 🔑 API Keys Setup

Create a `.env` file in the project root with the following variables:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVEN_API_KEY=your_elevenlabs_api_key_here
```

## 📋 Table of Contents

1. [System Dependencies Installation](#installing-ffmpeg-and-portaudio)
   - [macOS](#macos)
   - [Linux](#linux)
   - [Windows](#windows)
2. [Python Environment Setup](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
3. [Running the Application](#project-phases-and-python-commands)
4. [Project Components](#project-components)
5. [Usage Guide](#usage-guide)
6. [Deployment Options](#deployment-options)
7. [Troubleshooting](#troubleshooting)

## Installing FFmpeg and PortAudio

### macOS

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install FFmpeg and PortAudio:**

   ```bash
   brew install ffmpeg portaudio
   ```


### Linux
For Debian-based distributions (e.g., Ubuntu):

1. **Update the package list**

```
sudo apt update
```

2. **Install FFmpeg and PortAudio:**
```
sudo apt install ffmpeg portaudio19-dev
```

### Windows

#### Download FFmpeg:
1. Visit the official FFmpeg download page: [FFmpeg Downloads](https://ffmpeg.org/download.html)
2. Navigate to the Windows builds section and download the latest static build.

#### Extract and Set Up FFmpeg:
1. Extract the downloaded ZIP file to a folder (e.g., `C:\ffmpeg`).
2. Add the `bin` directory to your system's PATH:
   - Search for "Environment Variables" in the Start menu.
   - Click on "Edit the system environment variables."
   - In the System Properties window, click on "Environment Variables."
   - Under "System variables," select the "Path" variable and click "Edit."
   - Click "New" and add the path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
   - Click "OK" to apply the changes.

#### Install PortAudio:
1. Download the PortAudio binaries from the official website: [PortAudio Downloads](http://www.portaudio.com/download.html)
2. Follow the installation instructions provided on the website.

---

## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```


# Project Phases and Python Commands

## Phase 1: Brain of the doctor
```
python brain_of_the_doctor.py
```

## Phase 2: Voice of the patient
```
python voice_of_the_patient.py
```

## Phase 3: Voice of the doctor
```
python voice_of_the_doctor.py
```

## Phase 4: Setup Gradio UI
```
python gradio_app.py
```

---

## 📖 Project Components

### 1. Brain of the Doctor (`brain_of_the_doctor.py`)
- **Purpose**: Medical image analysis and AI consultation
- **Features**:
  - Image encoding to base64 format
  - Integration with Groq's Llama-4 vision model
  - Medical diagnosis and recommendations
  - Professional doctor-like responses
- **Key Functions**:
  - `encode_image()`: Converts images to base64
  - `analyze_image_with_query()`: Analyzes medical images with AI

### 2. Voice of the Patient (`voice_of_the_patient.py`)
- **Purpose**: Audio recording and speech-to-text conversion
- **Features**:
  - Real-time audio recording from microphone
  - Audio processing with PyAudio and Pydub
  - Speech-to-text using Groq's Whisper Large V3
  - Cross-platform audio format support
- **Key Functions**:
  - `record_audio()`: Records audio from microphone
  - `transcribe_with_groq()`: Converts speech to text

### 3. Voice of the Doctor (`voice_of_the_doctor.py`)
- **Purpose**: Text-to-speech conversion for doctor responses
- **Features**:
  - Multiple TTS engines (ElevenLabs + Google TTS)
  - Cross-platform audio playback
  - High-quality voice synthesis
  - Automatic audio playing
- **Key Functions**:
  - `text_to_speech_with_elevenlabs()`: Premium TTS with ElevenLabs
  - `text_to_speech_with_gtts()`: Backup TTS with Google
  - `simple_audio_player()`: Universal audio playback

### 4. Main Application (`gradio_app.py`)
- **Purpose**: Web-based user interface
- **Features**:
  - Interactive web interface with Gradio
  - Audio and image input handling
  - Real-time processing and response
  - Professional medical consultation experience
- **Interface Components**:
  - Audio input (microphone recording)
  - Image upload
  - Text output (transcription)
  - Doctor's response display
  - Audio output (doctor's voice)

## 🎯 Usage Guide

### Step 1: Setup Environment
1. Clone the repository
2. Install system dependencies (FFmpeg, PortAudio)
3. Create virtual environment
4. Install Python dependencies
5. Setup API keys in `.env` file

### Step 2: Run the Application
```bash
python gradio_app.py
```

### Step 3: Using the Interface
1. **Record Audio**: Click microphone to record symptoms
2. **Upload Image**: Upload medical images (optional)
3. **Submit**: Click submit to process
4. **Review Results**: 
   - View transcribed text
   - Read doctor's analysis
   - Listen to audio response

### Step 4: Understanding Responses
- **Transcription**: Your speech converted to text
- **Medical Analysis**: AI doctor's assessment
- **Audio Response**: Natural voice explanation

## 🚀 Deployment Options

### 1. Hugging Face Spaces (Recommended)
```yaml
Platform: Hugging Face Spaces
Cost: FREE
Features:
  - Native Gradio support
  - Auto-deployment from GitHub
  - Custom domains
  - Always online
  - Professional URLs
```

**Setup Steps:**
1. Upload code to GitHub
2. Create Hugging Face account
3. Create new Space
4. Connect GitHub repository
5. Deploy automatically

### 2. Streamlit Cloud
```yaml
Platform: Streamlit Cloud
Cost: FREE
Features:
  - Easy GitHub integration
  - Auto-deployment
  - Custom domains
Note: Requires Streamlit conversion
```

### 3. Railway
```yaml
Platform: Railway
Cost: FREE tier available
Features:
  - Simple deployment
  - Good performance
  - Custom domains
```

### 4. Render
```yaml
Platform: Render
Cost: FREE tier
Features:
  - Auto-deploy from GitHub
  - Good for portfolios
  - Easy setup
```

## 🔧 Troubleshooting

### Common Issues:

#### 1. Audio Recording Problems
```bash
# Install PortAudio dependencies
# Windows: Download from official site
# macOS: brew install portaudio
# Linux: sudo apt install portaudio19-dev
```

#### 2. FFmpeg Not Found
```bash
# Add FFmpeg to PATH
# Windows: Add C:\ffmpeg\bin to PATH
# macOS: brew install ffmpeg
# Linux: sudo apt install ffmpeg
```

#### 3. API Key Errors
```bash
# Check .env file exists
# Verify API keys are correct
# Ensure no spaces in API keys
```

#### 4. Import Errors
```bash
# Activate virtual environment
pipenv shell  # or
source venv/bin/activate  # or
conda activate myenv

# Install dependencies
pip install -r requirements.txt
```

#### 5. Microphone Access
- **Windows**: Allow microphone access in settings
- **macOS**: Grant microphone permission
- **Linux**: Check audio device permissions

### Performance Optimization:

#### 1. API Rate Limits
- Groq: Monitor usage limits
- ElevenLabs: Check character limits
- Use backup TTS if needed

#### 2. Audio Quality
- Use good quality microphone
- Reduce background noise
- Speak clearly and slowly

#### 3. Image Processing
- Use standard image formats (JPG, PNG)
- Optimize image size (< 10MB)
- Ensure good image quality

## 📊 Project Statistics

- **Total Files**: 8 core files
- **Python Version**: 3.11+
- **Dependencies**: 50+ packages
- **API Integrations**: 3 (Groq, ElevenLabs, Google TTS)
- **Supported Platforms**: Windows, macOS, Linux
- **Interface**: Web-based (Gradio)
- **Audio Formats**: MP3, WAV
- **Image Formats**: JPG, PNG, JPEG

## 🤝 Contributing

This is a portfolio project demonstrating:
- Multimodal AI integration
- Voice processing capabilities
- Medical AI applications
- Web application development
- API integration skills

## 📄 License

This project is created for educational and portfolio purposes. Please ensure you have proper API keys and follow the terms of service for all integrated services.

## 🆘 Support

For issues or questions:
1. Check troubleshooting section
2. Verify API keys and dependencies
3. Ensure proper environment setup
4. Check system requirements

## 📸 Project Output & Results

### Application Interface
The AI Doctor provides a clean, intuitive web interface where users can:

1. **Record Audio**: Use the microphone to describe symptoms
2. **Upload Images**: Share medical images for analysis
3. **View Results**: See transcribed text and medical analysis
4. **Listen to Response**: Hear the AI doctor's voice response

### Sample Workflow
```
Input: Voice Recording + Medical Image
↓
Processing: Speech-to-Text + Image Analysis
↓
Output: Transcription + Medical Analysis + Voice Response
```

### Example Output Format
```
Speech to Text: "I have a rash on my arm that's been itching for 3 days"

Doctor's Response: "With what I see, I think you have contact dermatitis. 
The rash appears red and inflamed, which suggests an allergic reaction. 
I recommend applying a mild corticosteroid cream and avoiding potential irritants."

Audio Response: [Natural voice synthesis of the doctor's response]
```

### Technical Output
- **Audio Processing**: MP3 format, 128k bitrate
- **Image Analysis**: Base64 encoded, supports JPG/PNG
- **Response Time**: ~3-5 seconds for complete processing
- **Audio Quality**: High-quality ElevenLabs voice synthesis

---

**Note**: This is a demonstration project for educational purposes. Always consult real medical professionals for actual medical advice.

