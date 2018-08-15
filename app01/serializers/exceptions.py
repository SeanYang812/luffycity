
# 自定义错误信息
class PriceException(Exception):

    def __init__(self):

        self.msg = "价格策略有问题！！"