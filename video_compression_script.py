import subprocess
import os

def get_new_output_name(output_path):
    base_name, ext = os.path.splitext(output_path)
    count = 1
    new_output_path = output_path
    while os.path.exists(new_output_path):
        new_output_path = f"{base_name}({count}){ext}"
        count += 1
    return new_output_path

def compress_video(input_path, output_path):
    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-vf', 'scale=iw:ih',      # Keep original dimensions
        '-b:v', '4k',              # Even lower video bitrate for worse quality
        '-r', '2',                 # Very low frame rate
        '-acodec', 'mp3',          # Change audio codec to MP3 for audio compression
        '-ab', '2k',               # Extremely low audio bitrate
        '-af', 'volume=10dB',     # Increase audio volume by 10 decibels
        output_path
    ]

    subprocess.run(cmd)

# Get the input video file name from the user
input_video_path = input("Enter the name of the video file (include extension): ")

# Generate the output video file name based on the input
output_video_path = f'compressed_{input_video_path}'

# Adjust output path if a file with the same name already exists
output_video_path = get_new_output_name(output_video_path)

compress_video(input_video_path, output_video_path)
