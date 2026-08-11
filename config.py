import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.default_config.copy()

    def load(self, custom_config_path):
        if os.path.isfile(custom_config_path):
            with open(custom_config_path, 'r') as file:
                custom_config = json.load(file)
                self._merge_configs(custom_config)
        return self.config

    def _merge_configs(self, custom_config):
        for key, value in custom_config.items():
            if isinstance(value, dict) and key in self.config:
                self.config[key] = self._merge_dicts(self.config[key], value)
            else:
                self.config[key] = value

    def _merge_dicts(self, default, custom):
        for key, value in custom.items():
            if isinstance(value, dict) and key in default:
                default[key] = self._merge_dicts(default[key], value)
            else:
                default[key] = value
        return default

# Example usage:
# if __name__ == '__main__':
#     defaults = {'setting1': 'default1', 'setting2': {'sub_setting1': 'default_sub1'}}
#     loader = ConfigLoader(defaults)
#     config = loader.load('./custom_config.json')
#     print(config)