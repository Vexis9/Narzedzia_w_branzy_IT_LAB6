import sys
import json
import yaml
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

def parse_arguments():
    if len(sys.argv) != 3:
        return None, None
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

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

def save_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving JSON: {e}")
        sys.exit(1)

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

def save_xml(file_path, data):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving XML: {e}")
        sys.exit(1)

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Error loading YAML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

def save_yaml(file_path, data):
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving YAML: {e}")
        sys.exit(1)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select input and output files for conversion", self)
        layout.addWidget(self.label)

        self.btn_input = QPushButton('Select Input File', self)
        self.btn_input.clicked.connect(self.show_input_file_dialog)
        layout.addWidget(self.btn_input)

        self.btn_output = QPushButton('Select Output File', self)
        self.btn_output.clicked.connect(self.show_output_file_dialog)
        layout.addWidget(self.btn_output)

        self.btn_convert = QPushButton('Convert', self)
        self.btn_convert.clicked.connect(self.convert_files)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.setWindowTitle('Data Converter')
        self.show()

    def show_input_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yaml *.yml)", options=options)
        if file_name:
            self.input_file = file_name
            self.label.setText(f"Selected input file: {file_name}")

    def show_output_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Select Output File", "", "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yaml *.yml)", options=options)
        if file_name:
            self.output_file = file_name
            self.label.setText(f"Selected output file: {file_name}")

    def convert_files(self):
        if hasattr(self, 'input_file') and hasattr(self, 'output_file'):
            if self.input_file.endswith('.json'):
                data = load_json(self.input_file)
            elif self.input_file.endswith('.xml'):
                data = load_xml(self.input_file)
            elif self.input_file.endswith('.yaml') or self.input_file.endswith('.yml'):
                data = load_yaml(self.input_file)
            else:
                self.label.setText("Unsupported input file format")
                return

            if self.output_file.endswith('.json'):
                save_json(self.output_file, data)
            elif self.output_file.endswith('.xml'):
                save_xml(self.output_file, data)
            elif self.output_file.endswith('.yaml') or self.output_file.endswith('.yml'):
                save_yaml(self.output_file, data)
            else:
                self.label.setText("Unsupported output file format")
                return

            self.label.setText("Conversion completed successfully")
        else:
            self.label.setText("Please select both input and output files")

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    if input_file and output_file:
        if input_file.endswith('.json'):
            data = load_json(input_file)
        elif input_file.endswith('.xml'):
            data = load_xml(input_file)
        elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
            data = load_yaml(input_file)
        else:
            print("Unsupported input file format")
            sys.exit(1)

        if output_file.endswith('.json'):
            save_json(output_file, data)
        elif output_file.endswith('.xml'):
            save_xml(output_file, data)
        elif output_file.endswith('.yaml') or output_file.endswith('.yml'):
            save_yaml(output_file, data)
        else:
            print("Unsupported output file format")
            sys.exit(1)
    else:
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())


    

