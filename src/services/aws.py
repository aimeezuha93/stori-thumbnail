import os
import numpy as np
from io import BytesIO
from matplotlib import image
from boto3 import client as boto_client
from src.services.logging import get_logger

logger = get_logger()


class S3:
    def __init__(self):
        self.env = os.getenv("env")
        self.s3client = boto_client("s3")

    def _get_image(self,  bucket, key):
        file_byte_string = self.s3client.get_object(
            Bucket=bucket, Key=key)['Body'].read()
        return np.array(image.imread(BytesIO(file_byte_string)))

    def _put_image(self, img, bucket, key):
        buffer = BytesIO()
        img.save(buffer, "JPG")
        buffer.seek(0)
        sent_data = self.s3client.put_object(
            Bucket=bucket, Key=key, Body=buffer)
        if sent_data['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise Exception(f'Failed to upload image {key} to bucket {bucket}')
