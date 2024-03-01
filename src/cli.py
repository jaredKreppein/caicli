import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="CAICLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Retrieve avalanche and weather forecasts from the CAIC",
    )
    parser.add_argument("latitude", type=float, help="latitude coordinate")
    parser.add_argument("longitude", type=float, help="longitude coordinate")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.1.0")
    return parser


def parse(argv: list[str]) -> argparse.Namespace:
    parser = create_parser()
    return parser.parse_args(argv)


def coordinates(lat: str, long: str) -> str:
    return f"Latitude: {lat}, Longitude: {long}"


def main(argv=None):
    parser = parse(argv)
    print(coordinates(parser.latitude, parser.longitude))


if __name__ == "__main__":  # pragma: no cover
    main()
