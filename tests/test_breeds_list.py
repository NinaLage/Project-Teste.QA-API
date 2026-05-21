import requests
from utils.config import BASE_URL


def test_list_all_breeds():

    response = requests.get(
        f"{BASE_URL}/breeds/list/all"
    )

    # Status code
    assert response.status_code == 200

    body = response.json()

    # Status API
    assert body["status"] == "success"

    # Valida existência do message
    assert "message" in body

    # Valida que retornou raças
    assert len(body["message"]) > 0