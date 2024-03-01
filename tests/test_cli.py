from argparse import ArgumentParser

from pytest import raises

from src.cli import coordinates, create_parser, main, parse


def test_create_parser():
    parser = create_parser()
    assert type(parser) is ArgumentParser


def test_valid_parse():
    parser = parse(["100", "200"])
    assert parser.latitude
    assert parser.longitude


def test_invalid_type_parse():
    with raises(SystemExit):
        parse(["hello", "world"])


def test_missing_required_parse():
    with raises(SystemExit):
        parse([])


def test_coordinates():
    response = coordinates(100, 200)
    assert response == "Latitude: 100, Longitude: 200"


def test_main(capsys):
    main(["100", "200"])
    capt = capsys.readouterr()
    assert capt.out == "Latitude: 100.0, Longitude: 200.0\n"
