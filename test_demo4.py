import pytest
class Test_Demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a!=b
        print("我的第一个测试用例")