from pyngrok import conf
import os
import yaml

config_path = conf.get_default().config_path
print(f"Config path: {config_path}")

if os.path.exists(config_path):
    print("Config file exists.")
    try:
        with open(config_path, 'r') as f:
            content = yaml.safe_load(f)
            if content and 'authtoken' in content:
                print("Authtoken found in config.")
                print(f"Token starts with: {content['authtoken'][:4]}...")
            else:
                print("Authtoken NOT found in config.")
    except Exception as e:
        print(f"Error reading config: {e}")
else:
    print("Config file does NOT exist.")
