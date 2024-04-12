import cv2

qrCode = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede abrir la camara")
    exit()

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qrCode.detectAndDecode(frame)
        if ret_qr:
            for info, point in zip(decoded_info, points):
                if info:
                    color = (0, 255, 0)
                    print(info)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [point.astype(int)], True, color, 8)
    else:
        print("No se detecta la imagen")
        break

    cv2.imshow('Detector de codios QR', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()