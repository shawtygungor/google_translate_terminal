import argparse

if __package__:
    from .easygoogletranslate import EasyGoogleTranslate
else:
    from easygoogletranslate import EasyGoogleTranslate

egt = EasyGoogleTranslate()


def main():
    parser = argparse.ArgumentParser(description="Google Translate Terminal Tool")
    parser.add_argument("-f", "--from", dest="source", help="...", default="en")
    parser.add_argument("-t", "--to", dest="target", help="...", default="tr")
    parser.add_argument("--file", help="...")

    args, unknownargs = parser.parse_known_args()

    if args.file:
        pass  # TODO: just add a helper that reads the file into a multiple lines string
    else:
        return egt.translate(
            text=" ".join(unknownargs),
            target_language=args.target,
            source_language=args.source,
        )


if __name__ == "__main__":
    print(main())
