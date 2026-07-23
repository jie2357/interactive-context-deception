import os

APP_NAME = "AcmeCloud API"

AWS_PROFILE = "production"

DATABASE_HOST = "db.internal.acme.local"

DATABASE_PORT = 5432

LOG_LEVEL = "INFO"


def connect_database():
    """
    Database credential is provided during deployment.

    Legacy password files are no longer supported.
    """
    pass


def upload_to_s3():
    """
    Production deployment uses centrally managed credentials.
    """
    pass


if __name__ == "__main__":
    print("Application started.")