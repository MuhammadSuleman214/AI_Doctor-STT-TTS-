# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS

import os
from gtts import gTTS
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="Hi this is Ai with Suleman!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs

import elevenlabs
from elevenlabs.client import ElevenLabs
ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

#Step2: Use Model for Text output to Voice

import subprocess
import platform
import os
def simple_audio_player(audio_filepath):
    """
    Simple audio player that works on all platforms
    """
    os_name = platform.system()
    
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', audio_filepath])
            
        elif os_name == "Windows":  # Windows
            # Use start command to open with default player
            subprocess.run(['start', audio_filepath], shell=True)
            
        elif os_name == "Linux":  # Linux
            # Use xdg-open to open with default player
            subprocess.run(['xdg-open', audio_filepath])
            
        else:
            print(f"Audio file saved: {audio_filepath}")
            print("Please play manually")
            
    except Exception as e:
        print(f"Audio file saved: {audio_filepath}")
        print("Please play manually using any media player")

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    # Use universal audio player
    simple_audio_player(output_filepath)


input_text="Hi this is Ai with Suleman, autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    # Use universal audio player
    simple_audio_player(output_filepath)

#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")