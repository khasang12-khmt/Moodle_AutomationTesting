import json

class TestDataParser:
    @staticmethod
    def parse_json(json_file):
        with open(json_file, 'r') as file:
            test_data = json.load(file)
        return test_data