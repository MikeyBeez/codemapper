import argparse
import json
from utils import create_map

def main():
    """
    The main function for the command-line interface.
    """
    parser = argparse.ArgumentParser(description='Map a code repository for LLM editing.')
    parser.add_argument('root_dir', help='The root directory of the repository.')
    parser.add_argument('ignore_file', help='The .ignore file to use.')
    parser.add_argument('output_file', help='The output file to save the map.')

    args = parser.parse_args()

    code_map = create_map(args.root_dir, args.ignore_file)

    with open(args.output_file, 'w') as f:
        json.dump(code_map, f, indent=4)

if __name__ == '__main__':
    main()

