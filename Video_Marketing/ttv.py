from moviepy.editor import VideoClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import numpy as np

# Function to generate a video frame with text
def create_frame(t):
    # Create a blank frame with a white background
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    frame.fill(255)  # Set the background to white

    # Define the text content and style
    text = "This is some scrolling text in a video."
    font_size = 30
    font_color = (0, 0, 0)  # Black text color

    # Calculate the text position for scrolling effect
    x = int(1280 * t) - 20 * len(text)
    y = 360

    frame = VideoClip.make_text(
        frame, text, fontsize=font_size, color=font_color, position=(x, y)
    )

    return frame

# Create a video clip with the scrolling text
video = VideoClip(make_frame=create_frame, duration=10)

# Export the video to a file
video.write_videofile("text_video.mp4", codec="libx264")
