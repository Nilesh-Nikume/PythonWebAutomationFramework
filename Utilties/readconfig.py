import os
import configparser

config = configparser.ConfigParser()

# Get project root directory automatically
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build config file path dynamically
config_path = os.path.join(project_root, "Configuration", "config.ini")

config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_email():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def get_password():
        Password = config.get('login data', 'password')
        return Password

    @staticmethod
    def valid_user_email():
        user_email = config.get("login data", "valid_user")
        return user_email

    @staticmethod
    def valid_user_password():
        user_password = config.get("login data", "valid_user")
        return user_password