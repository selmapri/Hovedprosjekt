from data_norge import search_datasets, print_datasets
from opencage import geocode_address

from data_norge import search_datasets, print_datasets


def main():

    print("=" * 50)
    print("DATA.NORGE.NO")
    print("=" * 50)

    query = input(
        "\nHva vil du søke etter? "
    )

    try:

        data = search_datasets(query)

        print("\nResultater:\n")

        print_datasets(data)

    except Exception as error:

        print(f"\nFeil: {error}")


if __name__ == "__main__":
    main()


""""
def main():

    print("=" * 50)
    print("NORSKE OFFENTLIGE HELSEDATA")
    print("=" * 50)

    # --------------------------------
    # 1. Data.norge.no
    # --------------------------------

    print("\nSøker på Data.norge.no...")

    data = search_datasets(
        "spesialisthelsetjenesten"
    )

    print("\nDatasett funnet:\n")

    print_datasets(data)

    # --------------------------------
    # 2. OpenCage
    # --------------------------------

    print("\n" + "=" * 50)
    print("OPEN CAGE")
    print("=" * 50)

    address = input(
        "\nSkriv inn en adresse eller et sted i Norge: "
    )

    try:

        location = geocode_address(address)

        if location is None:

            print(
                "\nFant ikke koordinater for stedet."
            )

        else:

            print("\nResultat:")
            print(
                f"Adresse: {location['formatted']}"
            )
            print(
                f"Latitude: {location['latitude']}"
            )
            print(
                f"Longitude: {location['longitude']}"
            )

    except Exception as error:

        print(
            f"\nNoe gikk galt: {error}"
        )


if __name__ == "__main__":
    main()

"""