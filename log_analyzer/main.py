import os
import yaml

def load_config(config_path):
    current_wd = os.path.dirname(__file__)
    change_directories = os.path.join (current_wd, config_path)
    try:
        with open(change_directories, 'r') as config_object:
            config = yaml.safe_load(config_object)
    except yaml.YAMLError as e:
        print(f"The .yaml file you requested seems to be malformed...\nError: {e}")
        return None
    except FileNotFoundError as e:
        print(f"The file you requested cannot be found...\nError: {e}")
        return None
    return config

if __name__ == "__main__":
    dict_to_print = load_config('../config/config.yaml')
    print(f"The configuration settings are as follows:\n{dict_to_print}")
    load_config('../config/nonexistent.yaml')
    load_config('../config/broken_config.yaml')
