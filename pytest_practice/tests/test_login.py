import pytest


class Test_login():
    @pytest.mark.second
    def test_loginByEmail(self,setup):
        print("loginByEmail method in Test01 class")
        assert True== True


    @pytest.mark.regression
    def test_loginByFacebook(self):
        print("loginByFacebook method in Test01 class")
        assert True== False

    @pytest.mark.skip
    def test_loginByTwitter(self):
        print("loginByTwitter method in Test01 class")
        assert True== True

    @pytest.mark.first
    @pytest.mark.sanity
    def test_loginByGmail(self):
        print("loginByGmail method in Test01 class")
        assert True== True