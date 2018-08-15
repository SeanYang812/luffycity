
class BaseResponse(object):

    def __init__(self):

        self.data = None
        self.error_msg = ""
        self.code = 1000

    @property
    def dict(self):

        # 返回所有的初始化属性
        return self.__dict__