import  pytest

@pytest.mark.parametrize('num1,num2',[(1,2),(2,2),(9,9)])
class TestParameterization():
    def test_equalNo(self,num1,num2):
        assert num1==num2