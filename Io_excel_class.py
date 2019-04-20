import xlwt
import xlrd
import time
import os
from xlutils.copy import copy


class ExcelIO:
    def __init__(self, all_list, face_list, date_list):
        """
        初始化
        :param all_list:所有学生名单，数据类型为列表
        :param face_list:已签到的学生名单，数据类型为列表
        :param date_list:已签到的学生签到时间，数据类型为列表
        """
        self.__all_list = all_list
        self.__face_list = face_list
        self.__date_list = date_list
        self.__year = ("%Y", time.localtime(time.time()))[1][0]
        self.__month = ("%m", time.localtime(time.time()))[1][1]
        self.__day = ("%d", time.localtime(time.time()))[1][2]

    def write_excel(self):
        """
        把签到写入写入excel文件
        :return: None
        """
        if os.path.isdir('学生签到情况/%d年' % self.__year) == 0:
            os.mkdir('学生签到情况/%d年' % self.__year)
        if os.path.isdir('学生签到情况/%d年/%d月' % (self.__year, self.__month)) == 0:
            os.mkdir('学生签到情况/%d年/%d月' % (self.__year, self.__month))
        if os.path.isfile('学生签到情况/%d年/%d月/%d日.xls' % (self.__year, self.__month, self.__day)) == 0:
            book = xlwt.Workbook(encoding="utf-8", style_compression=0)
            sheet = book.add_sheet("sheet", cell_overwrite_ok=True)
            sheet.write(0, 0, "序号")
            sheet.write(0, 1, "姓名")
            sheet.write(0, 2, "是否签到")
            sheet.write(0, 3, "签到日期")
            sheet.write(0, 4, "签到时间")
            book.save(r'学生签到情况/%d年/%d月/%d日.xls' % (self.__year, self.__month, self.__day))
        rb = xlrd.open_workbook(r'学生签到情况/%d年/%d月/%d日.xls' % (self.__year, self.__month, self.__day))
        rb.sheet_by_index(0)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        num = 0
        for j, i in enumerate(self.__all_list):
            ws.write(j + 1, 0, str(j + 1))
            if i in self.__face_list:
                ws.write(j+1, 1, i)
                ws.write(j+1, 2, "✓")
                ws.write(j+1, 3, str(self.__year) + "-" + str(self.__month) + "-" + str(self.__day))
                ws.write(j+1, 4, self.__date_list[num])
                num += 1
            else:
                ws.write(j+1, 1, i)
                ws.write(j+1, 2, "X")
                ws.write(j+1, 3, "无")
                ws.write(j+1, 4, "无")
        wb.save(r'学生签到情况/%d年/%d月/%d日.xls' % (self.__year, self.__month, self.__day))



