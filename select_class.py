import time
import xlrd


class SelectClock:
    def __init__(self, *args):
        if args:
            self.select_info_s(args)
        else:
            self.select_info()

    def select_info(self):
        """
        查询当日签到信息
        :return:None
        """
        year = ("%Y", time.localtime(time.time()))[1][0]
        month = ("%m", time.localtime(time.time()))[1][1]
        day = ("%d", time.localtime(time.time()))[1][2]
        xls_file = r'学生签到情况/%d年/%d月/%d日.xls' % (year, month, day)
        book = xlrd.open_workbook(xls_file)
        sheet0 = book.sheet_by_index(0)
        sheet1 = book.sheet_by_name('sheet')
        n_rows = sheet0.nrows
        for j, content in enumerate(range(n_rows)):
            if j != 0:
                print("%-9s%-10s%-12s%-18s%-9s" % (sheet1.row_values(content)[0], sheet1.row_values(content)[1],
                                                   sheet1.row_values(content)[2], sheet1.row_values(content)[3],
                                                   sheet1.row_values(content)[4]))
            else:
                print("%-8s%-9s%-9s%-15s%-9s" % (sheet1.row_values(content)[0], sheet1.row_values(content)[1],
                                                 sheet1.row_values(content)[2], sheet1.row_values(content)[3],
                                                 sheet1.row_values(content)[4]))

    def select_info_s(self, date):
        """
        查询指定日期签到信息
        :param date:例如20180101
        :return:None
        """
        year = str(date[0])[0:4]
        month = str(date[0])[5:6]
        if int(str(date[0])[-2:]) >= 10:
            day = str(date[0])[-2:]
        else:
            day = str(date[0])[-1:]
        xls_file = r'学生签到情况/%s年/%s月/%s日.xls' % (year, month, day)
        book = xlrd.open_workbook(xls_file)
        sheet0 = book.sheet_by_index(0)
        sheet1 = book.sheet_by_name('sheet')
        n_rows = sheet0.nrows
        for j, content in enumerate(range(n_rows)):
            if j != 0:
                print("%-9s%-10s%-12s%-18s%-9s" % (sheet1.row_values(content)[0], sheet1.row_values(content)[1],
                                                   sheet1.row_values(content)[2], sheet1.row_values(content)[3],
                                                   sheet1.row_values(content)[4]))
            else:
                print("%-8s%-9s%-9s%-15s%-9s" % (sheet1.row_values(content)[0], sheet1.row_values(content)[1],
                                                 sheet1.row_values(content)[2], sheet1.row_values(content)[3],
                                                 sheet1.row_values(content)[4]))

