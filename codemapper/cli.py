import argparse
import json
from .utils import create_map

def main():
    parser = argparse.ArgumentParser(description='Map a code repository for LLM editing.')
    parser.add_argument('root_dir', help='The root directory of the repository.')
    parser.add_argument('ignore_file', help='The .ignore file to use.')
    parser.add_argument('output_file', help='The output file to save the map.')

    args = parser.parse_args()

    try:
        code_map = create_map(args.root_dir, args.ignore_file)
        
        with open(args.output_file, 'w') as f:
            json.dump(code_map, f, indent=4)
        
        print(f"Code map successfully written to {args.output_file}")
        print("\nVersion Information:")
        print(f"Python: {code_map['version_info']['python']}")
        print(f"CodeMapper: {code_map['version_info']['codemapper']}")
        print("\nDependencies:")
        for dep, version in code_map['version_info']['dependencies'].items():
            print(f"{dep}: {version}")
        
        print(f"\nTotal files processed: {len(code_map['files'])}")
        print("Files with content included:")
        for file_info in code_map['files']:
            if 'content' in file_info:
                print(f"- {file_info['path']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
