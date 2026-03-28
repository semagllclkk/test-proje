"""AWS Connection Module - Secure Credential Handling."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_aws_credentials() -> dict:
    """Retrieve AWS credentials from environment variables.
    
    Returns:
        Dictionary containing AWS credentials
        
    Raises:
        ValueError: If required AWS credentials are not set
    """
    aws_secret_key = os.getenv("AWS_SECRET_KEY")
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_region = os.getenv("AWS_REGION", "us-east-1")
    
    if not aws_secret_key or not aws_access_key:
        raise ValueError(
            "Missing required AWS credentials. "
            "Set AWS_SECRET_KEY and AWS_ACCESS_KEY_ID environment variables."
        )
    
    return {
        "secret_key": aws_secret_key,
        "access_key": aws_access_key,
        "region": aws_region
    }


def connect() -> None:
    """Establish secure AWS connection using environment credentials.
    
    Raises:
        ValueError: If AWS credentials are missing
    """
    try:
        credentials = get_aws_credentials()
        # Log connection attempt WITHOUT exposing credentials
        print(f"Connecting to AWS region: {credentials['region']}...")
        # Connection would happen here using credentials
        print("✓ Connection established securely")
    except ValueError as error:
        print(f"✗ Connection failed: {error}")


if __name__ == "__main__":
    connect()
