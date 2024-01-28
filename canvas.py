import cv2
import mediapipe as mp

# Initialize Mediapipe Hand components
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Create a drawing canvas
window_size = 720
canvas = cv2.VideoCapture(0)
canvas.set(3, window_size)
canvas.set(4, window_size)

# Initial pen position
xp, yp = 0, 0

# Initialize Mediapipe Hand model
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8) as hands:
    while True:
        # Capture frame from the camera
        success, frame = canvas.read()
        if not success or frame is None:
            continue

        # Convert the frame to RGB format for Mediapipe
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find hands and get hand landmarks
        results = hands.process(image_rgb)

        # Draw landmarks on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for idx, landmark in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    if idx == 8:  # Index finger tip landmark (Landmark 8)
                        x, y = cx, cy

                # Check for a closed hand to reset the pen position
                if results.multi_handedness[0].classification[0].index == 0:
                    xp, yp = x, y

                # Draw on the canvas if index finger is up (open hand)
                if results.multi_handedness[0].classification[0].index == 1:
                    cv2.line(frame, (xp, yp), (x, y), (0, 255, 0), 5)
                    xp, yp = x, y

                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the frame (canvas)
        cv2.imshow("Virtual Drawing", frame)

        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
canvas.release()
cv2.destroyAllWindows()
