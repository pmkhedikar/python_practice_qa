import pytest


class Test02():

    @pytest.fixture     #Decorator
    def setup_method(self):
        print("launching browser")   # executed once before every test method
        yield
        print("closing browse")   # executed once after every test method


    def test_login(self,setup_method):
        print("Test login method")

    def test_search(self,setup_method):
        print("Test search method")

    def test_advanceSearch(self):
        print("Test advance search")
