from src.cli import main


def test_main():
    response = main(100, 200)
    assert response == "Latitude: 100, Longitude: 200"
