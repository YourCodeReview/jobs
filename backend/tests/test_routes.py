from http import HTTPStatus
from api.routes import NOT_FOUND


def test_root(test_client):
    response = test_client.get("/api/healthchecker")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "The API is LIVE!!"}


def test_create_get_vacancy(
    test_client,
    all_data_vancancy_payload,
    required_data_vancancy_payload,
    jobs_endpoint,
):
    post_response = test_client.post(jobs_endpoint, json=all_data_vancancy_payload)

    assert post_response.status_code == HTTPStatus.OK
    
    response = test_client.get(jobs_endpoint)
    response_json = response.json()
   
    id = response_json['data'][0]['id']
    response = test_client.get(jobs_endpoint + str(id))
    assert response.status_code == HTTPStatus.OK

    response_json = response.json()
    assert response_json["id"] == id
    assert response_json["external_id"] == 123
    assert response_json["company_name"] == "ABC Corporation"
    assert response_json["title"] == "Software Engineer"
    assert response_json["salary"] == "100000"
    assert response_json["location"] == "New York"
    assert response_json["speciality"] == "Python"
    assert response_json["internship"] == True
    assert response_json["remote"] == False
    assert response_json["url"] == "https://example.com/job"
    assert response_json["description"] == "This is a job description."

    post_response_2 = test_client.post(
        jobs_endpoint, json=required_data_vancancy_payload
    )
    assert post_response_2.status_code == HTTPStatus.OK
   
    response = test_client.get(jobs_endpoint)
    response_json = response.json()

    id = response_json['data'][1]['id']
    
    response = test_client.get(jobs_endpoint + str(id))
    assert response.status_code == HTTPStatus.OK

    response2_json = response.json()
    assert response2_json["id"] == id
    assert response2_json["external_id"] == None
    assert response2_json["company_name"] == None
    assert response2_json["title"] == "Software Engineer"
    assert response2_json["salary"] == None
    assert response2_json["location"] == None
    assert response2_json["speciality"] == "Python"
    assert response2_json["internship"] == False
    assert response2_json["remote"] == False
    assert response2_json["url"] == None
    assert response2_json["description"] == None


def test_create_vacancy_validation_error(
    test_client, validation_error_payload, jobs_endpoint
):
    response = test_client.post(jobs_endpoint, json=validation_error_payload)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_get_vacancy_not_found(test_client, jobs_endpoint):
    response = test_client.get(jobs_endpoint + "1000")
    assert response.status_code == HTTPStatus.NOT_FOUND
    response_json = response.json()
    assert response_json["detail"] == NOT_FOUND


def test_get_read_locations(
    test_client,
    locations_endpoint,
    jobs_endpoint,
    all_data_vancancy_payload,
    required_data_vancancy_payload,
):
    response = test_client.get(locations_endpoint)
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    assert "total_count" in response_json and "data" in response_json
    assert response_json["total_count"] == 0
    assert len(response_json["data"]) == 0

    response = test_client.post(jobs_endpoint, json=all_data_vancancy_payload)
    assert response.status_code == HTTPStatus.OK

    response2 = test_client.get(locations_endpoint)
    assert response2.status_code == HTTPStatus.OK
    response_json_2 = response2.json()
    assert "total_count" in response_json_2 and "data" in response_json_2
    assert response_json_2["total_count"] == 1
    assert len(response_json_2["data"]) == 1
    assert response_json_2["data"] == ["New York"]

    response = test_client.post(jobs_endpoint, json=required_data_vancancy_payload)
    assert response.status_code == HTTPStatus.OK

    response3 = test_client.get(locations_endpoint)
    assert response3.status_code == HTTPStatus.OK
    response_json_3 = response3.json()
    assert "total_count" in response_json_3 and "data" in response_json_3
    assert response_json_3["total_count"] == 2
    assert len(response_json_3["data"]) == 2
    assert set(response_json_3["data"]) == {"New York", None}
