import cv2
import face_recognition
import numpy as np


class NewFace:
    def __init__(self, name):
        self.__name = name

    def open_cv(self):
        """
        打开摄像头，按下q时把人脸数据保存为npy文件
        把人脸保存为jpg文件
        :return:None
        """
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)
                if face_encodings:
                    # 保存图像人脸信息到文件
                    cv2.imencode('.jpg', frame)[1].tofile("records/" + self.__name + ".jpg")
                    np.save("face_encodings/" + self.__name + ".npy", face_encodings[0])
                    print("保存成功")
                else:
                    print("没有检测到人脸，请重试！")
                cap.release()
                cv2.destroyAllWindows()
                break
