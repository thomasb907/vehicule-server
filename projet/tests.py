import subprocess
import pytest


def test_program_builds():
    """Vérifie que le programme s'exécute sans erreur."""
    try:
        # Lancer le script principal
        subprocess.run(["python", "main.py"], check=True)
    except subprocess.CalledProcessError:
        pytest.fail("Le programme n'a pas pu être exécuté correctement.")


def test_code_quality():
    """Vérifie la qualité du code avec flake8."""
    try:
        # Lancer flake8 sur le projet
        subprocess.run(["flake8", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Linting échoué : {e}")
