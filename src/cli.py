import argparse


def main(lat: str, long: str) -> str:
    return f"Latitude: {lat}, Longitude: {long}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="CAICLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Retrieve avalanche and weather forecasts from the CAIC",
    )
    parser.add_argument("latitude", type=float, help="latitude coordinate")
    parser.add_argument("longitude", type=float, help="longitude coordinate")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.1.0")
    args = parser.parse_args()

    print(main(args.latitude, args.longitude))
