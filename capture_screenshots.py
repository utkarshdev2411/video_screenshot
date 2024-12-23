import cv2
import os

def capture_screenshots(video_path, output_dir, interval=5):
    """
    Captures screenshots from a video every `interval` seconds.

    Parameters:
        video_path (str): Path to the input video file.
        output_dir (str): Directory to save the screenshots.
        interval (int): Time interval (in seconds) between screenshots.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the video
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error: Unable to open video file.")
        return

    # Get video frame rate
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_interval = interval * fps

    frame_count = 0
    screenshot_count = 0

    while True:
        ret, frame = video.read()

        # Break if video ends
        if not ret:
            break

        # Save screenshot every `frame_interval` frames
        if frame_count % frame_interval == 0:
            screenshot_path = os.path.join(output_dir, f"screenshot_{screenshot_count:03d}.jpg")
            cv2.imwrite(screenshot_path, frame)
            print(f"Saved: {screenshot_path}")
            screenshot_count += 1

        frame_count += 1

    video.release()
    print("Screenshot capture complete.")

if __name__ == "__main__":
    # Instructions for user
    print("Ensure OpenCV is installed. Run `pip install opencv-python` if not.")
    
    # Input: Path to the video file
    video_path = input("Enter the path to your video file: ")

    # Output: Directory for screenshots
    output_dir = input("Enter the directory to save screenshots: ")

    # Call the function
    capture_screenshots(video_path, output_dir)
