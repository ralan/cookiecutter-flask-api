from flask import json


def test_01_ping(client):
    response = client.get('/ping')
    json_data = json.loads(response.data)

    assert response.status_code == 200
    assert json_data == {'status': 'ok'}
