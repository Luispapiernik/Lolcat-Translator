from argparse import ArgumentParser

from lolcat_translator.tranzlator import tranzlate_file


def generate_config_file(args):
    with open("settings.env", "w") as file:
        file.write(f"DICTIONARY_FILEPATH = {args.dictionary_filepath}\n")


def main():
    parser = ArgumentParser()

    parser.add_argument(
        "-i", "--inputfile", default="test/english.txt",
    )
    parser.add_argument(
        "-o", "--outputfile", default="test/lolcat.txt",
    )
    parser.add_argument(
        "-dd", "--dictionary-filepath", default="storage/tranzlashun.json",
    )

    args = parser.parse_args()
    generate_config_file(args)

    tranzlate_file(args.inputfile, args.outputfile)


if __name__ == "__main__":
    main()
