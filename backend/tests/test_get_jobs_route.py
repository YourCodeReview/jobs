from http import HTTPStatus
from mock_data import vacancy_list
from api.routes import LIMIT_DEFAULT


def test_get_vacancies(test_client, jobs_endpoint):
    for vacancy in vacancy_list:
        response = test_client.post("/api/jobs/", json=vacancy)
        assert response.status_code == HTTPStatus.OK

    response = test_client.get(jobs_endpoint)
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 20
    assert len(response_json["data"]) == LIMIT_DEFAULT

    response = test_client.get(jobs_endpoint, params={"limit": 5})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 20
    assert len(response_json["data"]) == 5

    response = test_client.get(jobs_endpoint, params={"specialities": "frontend"})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 2
    assert len(response_json["data"]) == 2
    assert response_json["data"][0]["speciality"] == "frontend"
    assert response_json["data"][1]["speciality"] == "frontend"

    response = test_client.get(jobs_endpoint, params={"internship": True})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 2
    assert len(response_json["data"]) == 2
    assert response_json["data"][0]["internship"] == True
    assert response_json["data"][1]["internship"] == True
    assert response_json["data"][0]["title"] == "Стажёр Data Scientist"
    assert response_json["data"][1]["company_name"] == "ТестСофт"

    response = test_client.get(jobs_endpoint, params={"remote": True})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 6
    assert len(response_json["data"]) == 6

    response = test_client.get(jobs_endpoint, params={"location": "New York"})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 0
    assert len(response_json["data"]) == 0

    response = test_client.get(jobs_endpoint, params={"location": "Сан-Франциско, США"})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 1
    assert len(response_json["data"]) == 1
    assert response_json["data"][0]["location"] == "Сан-Франциско, США"

    """Test data jobs condition"""

    response = test_client.get(jobs_endpoint, params={"specialities": "data"})
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 2
    assert len(response_json["data"]) == 2
    assert response_json["data"][0]["speciality"] == "data science"
    assert response_json["data"][1]["speciality"] == "ml"
