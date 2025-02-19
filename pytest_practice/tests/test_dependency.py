import pytest


class Test_dependency():
    @pytest.mark.depedency()
    def test_login(self):
        print("Login method")
        assert True==False

    @pytest.mark.depedency(depends=['Test_dependency::test_login'])
    def test_search(self):
        print("Search method")

    @pytest.mark.depedency(depends=['Test_dependency::test_search'])
    def test_addtocart(self):
        print("Add to cart method")

    @pytest.mark.depedency()
    def test_payment(self):
        print("Payment method")

    @pytest.mark.depedency()
    def test_logout(self):
        print("logout method")