def test_patient_registration(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/api/patients' page is requested (POST) with valid data
    THEN check that the response is valid and a new patient is registered
    """
    endpoint = '/api/patients'

    valid_payload = {
        'name': 'Jane Doe',
        'email': 'jane@example.com',
        'password': 'example'
    }


    response = client.post(endpoint, json=valid_payload)


    assert response.status_code == 201


    json_data = response.get_json()
    assert 'id' in json_data
    assert json_data['id'] > 0
