import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(BASE_URL + "/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_posts_with_params():
    params = {"userId": 1}
    response = requests.get(BASE_URL + "/posts", params=params)
    assert response.status_code == 200
    assert len(response.json()) > 0
    for post in response.json():
        assert post["userId"] == params["userId"]


def test_get_post_by_id():
    post_id = 1
    response = requests.get(BASE_URL + f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id



def test_delete_post():
    post_id = 1
    response = requests.delete(BASE_URL + f"/posts/{post_id}")
    assert response.status_code == 200
    assert requests.get(BASE_URL + f"/posts/{post_id}").status_code

    def test_get_posts():
        response = requests.get(BASE_URL + "posts")
        assert response.status_code == 200

    def test_post_posts():
        data = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(BASE_URL + "posts", json=data)
        assert response.status_code == 201

    def test_delete_posts():
        response = requests.delete(BASE_URL+ "posts/1")
        assert response.status_code == 200