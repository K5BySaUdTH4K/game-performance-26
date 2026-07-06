import json

class GameDataHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error loading data: {e}')
            return None

    def save_data(self, data):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(data, file, indent=4)
            print('Data saved successfully.')
        except IOError as e:
            print(f'Error saving data: {e}')

    def update_data(self, key, value):
        data = self.load_data()
        if data is not None:
            data[key] = value
            self.save_data(data)
        else:
            print('No data to update.')