import argparse

from easygoogletranslate import EasyGoogleTranslate

egt = EasyGoogleTranslate()


def main():
    parser = argparse.ArgumentParser(description="Google Translate Terminal Tool")
    parser.add_argument("-f", "--from", dest="source", required=True, help="...")
    parser.add_argument("-t", "--to", dest="target", required=True, help="...")
    parser.add_argument("--file", help="...")

    args, unknownargs = parser.parse_known_args()

    if args.file:
        pass
    else:
        return egt.translate(
            text=" ".join(unknownargs), target_language=args.target, source_language=args.source
        )


if __name__ == "__main__":
    print(main())
