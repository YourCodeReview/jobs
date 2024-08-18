from http import HTTPStatus

def test_root(test_client):
    response = test_client.get("/api/healthchecker")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "The API is LIVE!!"}
