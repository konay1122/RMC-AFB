
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5878639052:AAELDROSpjq-RDLJhrH_9NW6DhWeGkH_uRs")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "6691216"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "56170666b4adfa400f7ef9f18f1fe6f3")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BVtsOGQBu1YoTwClEOHGPGH7Cj1irSdDO8jy5HDDtZFCcXwTjiFxEoXVQNABi5xcac5hzjPPlfnruUGH_LldWI_lZwstFuadQ1rZCIDTr_bge991lsMYBaNkVsdAxFJHWt53tpFu47CL8DxJQkidj5rh09bydmK_GwWru9cL-hhxwpGuVrYRp3C47eT-2ygKIvTZLc4zaUnCtYqawBdkgG7cFvsrRxn8WlkcoghQYCJV59GYZBrD2Xi84hU75YIDdoguI5Un9jPVBRv2m6F8CfJ_CsuX53V-rJNdV8JmSZneq3WvcgaaxEh7n9iVb4Xn0y_TBcG8CdqD_H3Hd9q3eIKmYf_lVgM=")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001705940198")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
