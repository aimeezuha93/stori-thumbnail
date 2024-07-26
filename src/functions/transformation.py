import os
import sys
import traceback
import json
import json
import pandas as pd
import urllib.parse
import numpy as np
import matplotlib.pyplot as plt
from src.services.logging import get_logger
from src.services.aws import S3

logger = get_logger()
s3 = S3()


def handler(event, context):
    try:
        logger.info("Starting Stori Thumbnail Pipeline")

        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(
            event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
        )
        img_original = S3._get_image(bucket, key)
        downscale_factor = 4
        img_thumbnail = img_original[::downscale_factor, ::downscale_factor, :]

        plt.text(0.6, 0.7, "click here", size=50, rotation=30.,
                 ha="left", va="center",
                 bbox=dict(boxstyle="round",
                           ec=(1., 0.5, 0.5),
                           fc=(1., 0.8, 0.8),
                           )
                 )

        S3._put_image(
            img_thumbnail, "stori-data-services-out-prod", "images/doggie.jpg")

        logger.info("Ending Stori Thumbnail Pipeline Successfully")

    except Exception:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(
            exception_type, exception_value, exception_traceback
        )
        logger.info("Ending Stori Thumbnail Pipeline Unsuccessfully:")
        err_msg = {
            "errorType": exception_type.__name__,
            "errorMessage": str(exception_value),
            "stackTrace": traceback_string,
        }
        logger.error(json.dumps(err_msg))
