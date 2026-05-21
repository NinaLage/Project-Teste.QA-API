import requests
from utils.config import BASE_URL


def test_invalid_breed():

    breed = "invalidbreed"

    response = requests.get(
        f"{BASE_URL}/breed/{breed}/images"
    )

    # API retorna 404
    assert response.status_code == 404

    body = response.json()

    assert body["status"] == "error"