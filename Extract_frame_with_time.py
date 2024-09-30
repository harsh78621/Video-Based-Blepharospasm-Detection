import os
import cv2
import datetime  # To create a unique directory name based on timestamp

def extract_frames_from_video(video_file, output_base_dir):
    """
    Extract frames from a video file and save them as individual JPEG images.

    Args:
        video_file (str): The path to the video file.
        output_base_dir (str): The base directory where the extracted frames will be saved.

    Returns:
        None
    """
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    output_dir = os.path.join(output_base_dir, video_name)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_file}'.")
        return

    while True:
        ret, frame = cap.read()  # Read a frame from the video
        if not ret:  # If no more frames, exit the loop
            break

        # Get the timestamp of the current frame in milliseconds
        timestamp_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        timestamp_str = f"{timestamp_ms:.0f}ms"

        # Generate a filename for the frame using the timestamp
        frame_filename = os.path.join(output_dir, f"frame_{timestamp_str}.jpg")

        # Save the frame to a JPEG file
        cv2.imwrite(frame_filename, frame)

    cap.release()  # Release the VideoCapture object

    print(f"Extracted frames saved to '{output_dir}'.")

def extract_frames_from_directory(directory):
    # Create the base output directory in the parent directory of the specified directory
    parent_directory = os.path.dirname(directory)
    output_base_dir = os.path.join(parent_directory, "New Extracted Frames")

    # Create the base output directory if it doesn't exist
    os.makedirs(output_base_dir, exist_ok=True)

    # List all files in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".avi") or filename.endswith(".mp4"):  # Adjust extensions as needed
                video_file = os.path.join(root, filename)
                extract_frames_from_video(video_file, output_base_dir)

if __name__ == "__main__":
    # Specify the directory containing video files
    directory = "D:\\harsh\\Blepharospasm\\Norm2"

    # Extract frames from videos in the specified directory
    extract_frames_from_directory(directory)
