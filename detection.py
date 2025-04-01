import cv2
import numpy as np
import easyocr

# Load YOLO model
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
layers = net.getLayerNames()
out_layers = [layers[i - 1] for i in net.getUnconnectedOutLayers()]

# Load COCO class labels
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Define video capture
cap = cv2.VideoCapture(0)  # Change to video file path if needed

# Initialize OCR reader
reader = easyocr.Reader(['en'])

def detect_objects(frame):
    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(out_layers)
    return outputs, width, height

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    outputs, width, height = detect_objects(frame)
    boxes, confidences, class_ids = [], [], []
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and (class_id == 0 or class_id == 1):  # Person or Helmet
                center_x, center_y, w, h = (detection[:4] * [width, height, width, height]).astype("int")
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    helmet_wearers, non_helmet_wearers = [], []
    
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = classes[class_ids[i]]
            color = (0, 255, 0) if label == "helmet" else (0, 0, 255)
            if label == "person":
                non_helmet_wearers.append((x, y, w, h))
            elif label == "helmet":
                helmet_wearers.append((x, y, w, h))
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # License Plate Detection for non-helmet wearers
    for (x, y, w, h) in non_helmet_wearers:
        roi = frame[y:y + h, x:x + w]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        results = reader.readtext(gray)
        for (bbox, text, prob) in results:
            print(f"Vehicle Number (No Helmet): {text}")
            cv2.putText(frame, text, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
