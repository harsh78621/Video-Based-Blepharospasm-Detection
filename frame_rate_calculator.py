import cv2

def get_video_frame_rate(video_file):
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_file}'.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps

if __name__ == "__main__":
    video_file = "D:\\harsh\\Blepharospasm\\Norm2\\182.avi"
    frame_rate = get_video_frame_rate(video_file)
    print(f"Frame rate of the video: {frame_rate} fps")
