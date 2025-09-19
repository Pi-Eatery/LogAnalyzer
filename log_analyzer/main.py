import yaml

def load_config(config_path):
    try:
        with open(config_path, 'r') as config_object:
            config = yaml.safe_load(config_object)
    except FileNotFoundError as e:
        print(f"The file you requested cannot be found...\nError: {e}")
        return None
    except yaml.YAMLError as e:
        print(f"The file you requested seems to be malformed...\nError: {e}")
        return None
    return config

if __name__ == "__main__":
    dict_to_print = {}
    dict_to_print = load_config('../config/config.yaml')
    print(f"The configuration settings are as follows:\n{dict_to_print}")
    load_config('../config/nonexistent.yaml')
    load_config('../config/broken_config.yaml')
