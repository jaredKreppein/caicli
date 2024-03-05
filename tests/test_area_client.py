from shapely.geometry import Point

from src.area_client import AreaClient
from tests.resources.TEST_AREA import TEST_AREA


def test_get_avalanche_area_id_success(mocker):
    processor = AreaClient()

    mock_response = type(
        "MockResponse", (), {"status_code": 200, "json": lambda: TEST_AREA}
    )
    mocker.patch("requests.get", return_value=mock_response)
    test_point = Point(0.5, 0.5)
    point_area_id = processor.get_avalanche_area_id(test_point)
    assert point_area_id == "TESTAREAID"


def test_get_special_product_id_success(mocker):
    processor = AreaClient()

    mock_response = type(
        "MockResponse", (), {"status_code": 200, "json": lambda: TEST_AREA}
    )
    mocker.patch("requests.get", return_value=mock_response)
    test_point = Point(0.5, 0.5)
    point_area_id = processor.get_special_product_id(test_point)
    assert point_area_id == "TESTAREAID"


def test_get_regional_discussion_area_id_success(mocker):
    processor = AreaClient()

    mock_response = type(
        "MockResponse", (), {"status_code": 200, "json": lambda: TEST_AREA}
    )
    mocker.patch("requests.get", return_value=mock_response)
    test_point = Point(0.5, 0.5)
    point_area_id = processor.get_regional_discussion_id(test_point)
    assert point_area_id == "TESTAREAID"


def test_get_id_methods_http_failure(mocker):
    processor = AreaClient()

    mock_response = type("MockResponse", (), {"status_code": 500})
    mocker.patch("requests.get", return_value=mock_response)
    test_point = Point(0.5, 0.5)
    point_area_id = processor.get_avalanche_area_id(test_point)
    assert point_area_id == None
    point_area_id = processor.get_special_product_id(test_point)
    assert point_area_id == None
    point_area_id = processor.get_regional_discussion_id(test_point)
    assert point_area_id == None
