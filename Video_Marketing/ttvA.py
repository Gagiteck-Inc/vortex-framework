from moviepy.editor import VideoFileClip, TextClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from gtts import gTTS
import os

# Text you want to convert into video
text = "This is an example of converting text into a video with an avatar for Vortex"

# Create a text-to-speech (TTS) audio file
tts = gTTS(text)
tts.save("text_audio.mp3")

# Load the audio and create a video with an avatar or animation
audio = VideoFileClip("text_audio.mp3")
avatar_clip = TextClip(text, fontsize=30, color="white", bg_color="black")

# Set the duration of the video to match the audio
avatar_clip = avatar_clip.set_duration(audio.duration)

# Combine the audio and the avatar video
final_video = avatar_clip.set_audio(audio)

# Export the final video
final_video.write_videofile("text_video_with_avatar.mp4", codec="libx264")

# Cleanup temporary files
os.remove("text_audio.mp3")
