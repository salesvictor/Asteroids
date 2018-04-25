class TestParam:
    PARAM = 1

    @classmethod
    def print_param(cls):
        print(cls.PARAM)


if __name__ == '__main__':
    TestParam.print_param()
    TestParam.PARAM = 2
    TestParam.print_param()
