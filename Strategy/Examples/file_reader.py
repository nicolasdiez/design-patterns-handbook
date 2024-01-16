from abc import ABC, abstractmethod
from typing import List, Dict, Any
import csv
import json
import xml.etree.ElementTree as ET

# FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

# The 3 different file parser strategies: CSV, JSON, XML
class CSVParser(FileParser):
    
    def __init__(self):
        pass
        
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            row_header = next(reader)
            parsed_data = []
            for row in reader:
                row_data = {}
                i = 0
                for column in row_header:
                    row_data[column] = row[i]
                    i = i + 1
                    print(row_data)
                parsed_data.append(row_data)
        print(parsed_data)
        return parsed_data
    
    # cleaner implementation for parse_file method
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
            
class JSONParser(FileParser):
    
    def __init__(self):
        pass
        
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:          
        with open(file_path) as json_data:
            parsed_data = json.load(json_data)
        print(parsed_data)
        return parsed_data

class XMLParser(FileParser):
    
    def __init__(self):
        pass
        
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        tree = ET.parse(file_path)
        root = tree.getroot()
 
        parsed_data = []
        for child in root:
            parsed_data.append(child.attrib)
 
        return parsed_data

# The FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # Initialize the file reader with the given file_parser strategy
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        parsed_data = self.file_parser.parse_file(file_path)
        return parsed_data

# Test the implementation
if __name__ == "__main__":
    reader = FileReader(CSVParser())
    
    data = reader.read_file("Example/sample.json")
    print(data)
