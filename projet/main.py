import requests
import fire


def list_vehicule(address="http://localhost:8080/vehicles"):
    try:
        response = requests.post(address)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la requête : {e}"


if __name__ == '__main__':
    fire.Fire(list_vehicule)
