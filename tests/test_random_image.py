import requests
from utils.config import BASE_URL


def test_random_image():

    response = requests.get(
        f"{BASE_URL}/breeds/image/random"
    )

    # Status code
    assert response.status_code == 200

    body = response.json()

    # Status API
    assert body["status"] == "success"

    image = body["message"]

    # Valida URL
    assert image.startswith("https://")

    # Valida extensão imagem
    assert ".jpg" in image or ".jpeg" in image or ".png" in image