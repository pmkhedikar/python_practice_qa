import pytest


class Test_Signup():
    def test_signupByEmail(self):
        print("SignupByEmail method in Test01 class")
        assert True==True

    @pytest.mark.run(order=1)
    def test_signupByFacebook(self,setup):
        print("SignupByFacebook method in Test01 class")
        assert True== False

    @pytest.mark.run(order=2)
    def test_signupByTwitter(self,setup):
        print("signupByTwitter method in Test01 class")
        assert True== True