import codecs


class RegLogin:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def sign_up(self):
        """
        注册账号
        :return: True
        """
        with codecs.open("user.txt", "a+", "utf-8") as f:
            f.write(self.__username + "|" + self.__password + "\n")
        return True

    def proving_user(self):
        """
        检测用户名是否存在
        :return: 存在返回True,否则返回False
        """
        res = False
        with codecs.open("user.txt", "r", "utf-8") as f1:
            for i in f1.readlines():
                s = i.replace("\n", "")
                new_list = s.split("|")
                if new_list[0] == self.__username:
                    res = True
                    break
                else:
                    res = False
        return res

    def sign_in(self):
        """
        登录方法
        :return:成功则返回True,否则返回False
        """
        res = False
        with codecs.open("user.txt", "r", "utf-8") as f2:
            for i in f2.readlines():
                s = i.replace("\n", "")
                s = s.replace("\r", "")
                new_list = s.split("|")
                if new_list[0] == self.__username and new_list[1] == self.__password:
                    res = True
                    break
                else:
                    res = False
        return res
