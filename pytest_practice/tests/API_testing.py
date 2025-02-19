import requests
import json


def test_reqres_api():
    url = "http://reqres.in/api/users?page=2"
    response = requests.get(url)

    # Validate HTTP Status Code
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    # Parse JSON Response
    response_json = response.json()

    # Validate Keys in Response
    expected_keys = {"page", "per_page", "total", "total_pages", "data", "support"}
    assert expected_keys.issubset(response_json.keys()), "Missing expected keys in response"

    # Validate Pagination Data
    assert response_json["page"] == 2, "Page number mismatch"
    assert response_json["per_page"] == 6, "Per page count mismatch"
    assert response_json["total"] == 12, "Total count mismatch"
    assert response_json["total_pages"] == 2, "Total pages count mismatch"

    # Validate User Data
    assert isinstance(response_json["data"], list), "Data is not a list"
    assert len(response_json["data"]) == response_json["per_page"], "Mismatch in user count"

    for user in response_json["data"]:
        assert "id" in user, "User ID missing"
        assert "email" in user, "Email missing"
        assert "first_name" in user, "First name missing"
        assert "last_name" in user, "Last name missing"
        assert "avatar" in user, "Avatar missing"
        assert user["email"].endswith("@reqres.in"), "Invalid email domain"

    # Validate Support Section
    assert "url" in response_json["support"], "Support URL missing"
    assert "text" in response_json["support"], "Support text missing"

    print("API test passed successfully!")


if __name__ == "__main__":
    test_reqres_api()
