import cv2

qrCode = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)

def QR():
    if not cap.isOpened():
        print("No se puede abrir la camara")
        exit()

    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qrCode.detectAndDecodeMulti(frame)
            if ret_qr:
                for info, point in zip(decoded_info, points):
                    if info:
                        cv2.putText(frame, info, (0, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 1, cv2.LINE_4)
                        color = (0, 255, 0)
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

if __name__ == '__main__':
    QR()