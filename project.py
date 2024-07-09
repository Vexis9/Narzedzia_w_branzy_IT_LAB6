import sys

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    return input_file, output_file

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")


import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    
    if input_file.endswith('.json'):
        data = load_json(input_file)
        print("JSON data loaded successfully")
    else:
        print("Unsupported input file format")
        sys.exit(1)
    

