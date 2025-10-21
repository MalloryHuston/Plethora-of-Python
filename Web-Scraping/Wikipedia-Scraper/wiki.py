import wikipedia as wiki
import argparse as ap


def main():
    parser = ap.ArgumentParser(
        description="Query Wikipedia and optionally download an image."
    )
    parser.add_argument(
        'keyword', type=str,
        help="Wikipedia search query (e.g. 'Morgan Freeman')"
    )
    parser.add_argument(
        '--loc', type=str, dest='location',
        help="Directory to save output (e.g. '/Users/malpal101/Desktop')"
    )
    parser.add_argument(
        '-i', '--image', action='store_true',
        help="Download main image"
    )

    args = parser.parse_args()

    if args.location:
        wiki.query_wikipedia(args.keyword, args.location, download=args.image)
    else:
        wiki.query_wikipedia(args.keyword, download=args.image)


if __name__ == "__main__":
    main()
