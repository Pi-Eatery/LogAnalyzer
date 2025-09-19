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
    return None

