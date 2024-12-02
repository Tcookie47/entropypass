import argparse
from entropypass.password_gen import return_strong_password, process_file

def main():
    parser = argparse.ArgumentParser(description="High Entropy Password Generator CLI")

    parser.add_argument(
        "-e", "--entropy",
        type=int,
        default=60,
        help="Entropy level (default is 60, range 0-200)"
    )
    parser.add_argument(
        "-i", "--input",
        type=str,
        help="Path to input file containing passwords (1 per line)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Path to output file to save the generated passwords"
    )
    parser.add_argument(
        "password",
        nargs="?",
        help="Password string to transform"
    )

    args = parser.parse_args()

    if args.input:
        if args.output:
            process_file(args.input, args.output, args.entropy)
        else:
            print("Error: Output file path (-o) must be provided when using -i.")
    elif args.password:
        print(return_strong_password(args.password, args.entropy))
    else:
        print("Error: Provide a password, or use -i for input files.")

if __name__ == "__main__":
    main()
