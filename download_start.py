# qBittorrent script to notify when a download starts
# python3 /path/to/download_start.py %N %D

# get the args from qbittorrent
import sys
import logging
import datetime
from dingtalk_utils import dingtalk

# logging
logging.basicConfig(filename='/path/to/downloads.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

# get the args from qbittorrent
torrent_name = sys.argv[1]
torrent_save_path = sys.argv[2]
logging.info(f"Download of `{torrent_name}` to `{torrent_save_path}` starts")

# send infomation to DingTalk
send_body = {
    "msgtype": "markdown",
    "markdown": {
        "title":"Download Starts",
        "text": f"### Start download of `{torrent_name}` to `{torrent_save_path}`\n - at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    },
    "at": {
        "isAtAll": True,
    },
}

dingtalk = dingtalk()
r = dingtalk.post(send_body)
logging.info(f"Send to DingTalk, with return: {r.text}")