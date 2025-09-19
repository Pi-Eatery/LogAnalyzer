import os
import yaml

def load_config(config_path):
    try:
        with open(config_path, 'r') as config_object:
            config = yaml.safe_load(config_object)
    except yaml.YAMLError as e:
        print(f"\nThe .yaml file you requested seems to be malformed...\nError: {e}\n\n")
        return None
    except FileNotFoundError as e:
        print(f"\nThe file you requested cannot be found...\nError: {e}\n\n")
        return None
    return config

if __name__ == "__main__":
    current_wd = os.path.dirname(__file__)
    config_dir_path = os.path.join(current_wd, '../config/')
    config_file_path = os.path.join(config_dir_path, 'config.yaml')
    dict_to_print = load_config(config_file_path)
    load_config(os.path.join(config_dir_path, 'nonexistent'))
    load_config(os.path.join(config_dir_path, 'broken_config.yaml'))

    print(f"\nThese are the current config options:\n---\n{dict_to_print}\n\n\n")
