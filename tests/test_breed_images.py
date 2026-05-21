import requests
from utils.config import BASE_URL


def test_breed_images():

    breed = "hound"

    response = requests.get(
        f"{BASE_URL}/breed/{breed}/images"
    )

    # Status code
    assert response.status_code == 200

    body = response.json()

    # Status API
    assert body["status"] == "success"

    # Lista imagens
    images = body["message"]

    # Valida retorno
    assert len(images) > 0

    # Valida formato URL
    assert images[0].startswith("https://")