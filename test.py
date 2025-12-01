from google.colab import files
uploaded = files.upload()

# Example: your uploaded file might be "myface.jpg"
image_path = list(uploaded.keys())[0]
print("✅ Uploaded file:", image_path)
import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt

# Load detector and predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the image
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detector(gray)

if len(faces) == 0:
    print("⚠️ No face detected. Try a clearer front-facing photo.")
else:
    for face in faces:
        landmarks = predictor(gray, face)

        # Helper: get coordinates
        def point(n):
            return (landmarks.part(n).x, landmarks.part(n).y)

        # Key points
        top_head = point(27)      # between eyebrows (approx forehead)
        chin = point(8)
        left_cheek = point(1)
        right_cheek = point(15)
        nose_tip = point(30)
        nose_left = point(31)
        nose_right = point(35)
        mouth_left = point(48)
        mouth_right = point(54)
        eye_left_outer = point(36)
        eye_right_outer = point(45)

        # Distance helper
        def dist(p1, p2):
            return np.linalg.norm(np.array(p1) - np.array(p2))

        # Distances
        face_length = dist(top_head, chin)
        face_width = dist(left_cheek, right_cheek)
        nose_width = dist(nose_left, nose_right)
        mouth_width = dist(mouth_left, mouth_right)
        eye_distance = dist(eye_left_outer, eye_right_outer)

        # Ratios
        ratios = {
            "Face Length / Width": face_length / face_width,
            "Mouth Width / Nose Width": mouth_width / nose_width,
            "Eye Distance / Nose Width": eye_distance / nose_width,
        }

        print("\n✨ Golden Ratio Analysis ✨\n")
        for name, value in ratios.items():
            result = "✅ Close to Golden Ratio" if 1.5 <= value <= 1.7 else "⚠️ Not Ideal"
            print(f"{name}: {value:.3f} → {result}")

        avg_ratio = sum(ratios.values()) / len(ratios)
        score = (min(avg_ratio, 1.618) / 1.618) * 100
        print(f"\nOverall Face Symmetry Score: {score:.2f}%")

        # Draw landmarks
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(img, (x, y), 2, (0, 255, 0), -1)

    # Display image inline
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8,6))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("Golden Ratio Face Analyzer")
    plt.show()
