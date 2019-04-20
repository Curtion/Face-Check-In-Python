import cv2
import face_recognition
import os
import time
import Io_excel_class as i_e


class StartFace:
    def get_all_face_encode_file(self, path):
        """
        检测路径下所有文件
        :param path: 文件夹路径
        :return: 所有文件路径
        """
        fs = os.listdir(path)
        list_path = []
        for f1 in fs:
            tmp_path = os.path.join(path, f1)
            if not os.path.isdir(tmp_path):
                list_path.append(tmp_path)
        return list_path

    def open_cv(self, encodings):
        """
        打开摄像头，检测人脸和列表中数据对比
        :param encodings:编码后的图片数据，数据类型为
        :return:None
        """
        process_this_frame = True
        face_names = []
        now_time_list = []
        video_capture = cv2.VideoCapture(0)
        path = "face_encodings/"
        labels = []
        for i in self.get_all_face_encode_file(path):
            labels.append(i[15:-4])
        while True:
            ret, frame = video_capture.read()
            cv2.imshow("capture", frame)
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            if process_this_frame:
                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)
                for face_encoding in face_encodings:
                    match = face_recognition.compare_faces(encodings, face_encoding, tolerance=0.4)
                    for i in range(0, len(match)):
                        if match[i]:
                            print('这个人是:' + labels[i])
                            if labels[i] not in face_names:
                                localtime = time.localtime(time.time())
                                now_time = str(("%y", localtime)[1][3]) + ":" + str(("%y", localtime)[1][4])
                                face_names.append(labels[i])
                                now_time_list.append(now_time)
            process_this_frame = not process_this_frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                xls = i_e.ExcelIO(labels, face_names, now_time_list)
                xls.write_excel()
                print("点到完成！")
                break
        video_capture.release()
        cv2.destroyAllWindows()
