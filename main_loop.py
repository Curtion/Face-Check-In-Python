# -*- coding: UTF-8 -*-
import os
import reg_login_class as r_l
import new_face_class as n_f
import start_face_class as s_f
import numpy as np
import select_class as s_c
while True:
    print("欢迎使用人脸识别点名系统，请输入相应的操作项!")
    print("1.输入\"1\"录入学生人脸信息")
    print("2.输入\"2\"开始进行人脸识别点到")
    print("3.输入\"3\"查看今日签到结果")
    print("4.输入\"4\"查看指定日期签到结果")
    print("5.输入\"5\"登录系统")
    print("6.输入\"6\"注册账号")
    print("7.输入\"7\"退出系统")
    dictate = input("请输入：")
    if dictate == "1":
        print("稍后按q退出并保存录入信息！")
        name = input("请输入您的姓名：")
        if os.path.exists("records/" + name + ".jpg"):
            print("你已录入人脸信息，无需重新录入，如果有重名请在名字后加编号重试！")
        else:
            nf_obj = n_f.NewFace(name)
            nf_obj.open_cv()
    elif dictate == "2":
        path = "face_encodings/"
        sf_obj = s_f.StartFace()
        B = []
        for i in sf_obj.get_all_face_encode_file(path):
            B.append(np.load(i))
        sf_obj.open_cv(B)
    elif dictate == "3":
        if os.path.exists("login.lock"):
            s_c.SelectClock()
        else:
            print("请登录后操作")
    elif dictate == "4":
        if os.path.exists("login.lock"):
            in_date = input("请输入日期，例如20180101：")
            if in_date.isdigit():
                s_c.SelectClock(int(in_date))
            else:
                print("输入格式有误，请重试！")
            s_c.SelectClock()
        else:
            print("请登录后操作")
    elif dictate == "5":
        user = input("请输入账号：")
        pwd = input("请输入密码：")
        if user == "" or pwd == "":
            print("你输入的账号或者密码有空值")
        else:
            user_obj = r_l.RegLogin(user, pwd)
            if user_obj.proving_user():
                if user_obj.sign_in():
                    print("登录成功！")
                    with open("login.lock", "w") as fp:
                        pass
                else:
                    print("账号或者密码错误！")
            else:
                print("账号不存在")
    elif dictate == "6":
        user = input("请输入账号：")
        pwd = input("请输入密码：")
        if user == "" or pwd == "":
            print("你输入的账号或者密码有空值")
        else:
            user_obj = r_l.RegLogin(user, pwd)
            if user_obj.proving_user():
                print("账号已存在")
            else:
                user_obj.sign_up()
                print("注册成功！")
    elif dictate == "7":
        if os.path.exists("login.lock"):
            os.remove("login.lock")
        break
    else:
        print("没有这一选项！请重新选择")
