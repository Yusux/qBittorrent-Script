# qBittorrent script to notify when a download starts
# python3 /path/to/download_complete.py %N %F %D %C %Z %I %J

# get the args from qbittorrent
import sys
import logging
import datetime
from dingtalk_utils import dingtalk

# logging
logging.basicConfig(filename='/path/to/downloads.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

# get the args from qbittorrent
file_name = sys.argv[1]
file_content_path = sys.argv[2]
file_save_path = sys.argv[3]
file_count = sys.argv[4]
file_size = int(sys.argv[5]) / 1024 / 1024
file_hash_v1 = sys.argv[6]
file_hash_v2 = sys.argv[7]
logging.info(f"Download of `{file_name}` to `{file_save_path}` completed\n\
                                - file_content_path: {file_content_path}\n\
                                - file_count: {file_count}\n\
                                - file_size: {file_size} MB\n\
                                - file_hash_v1: {file_hash_v1}\n\
                                - file_hash_v2: {file_hash_v2}")

# send infomation to DingTalk
send_body = {
    "msgtype": "markdown",
    "markdown": {
        "title":"Download Completed",
        "text": f"### Completed download of `{file_name}` to `{file_save_path}`\n - at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n - file_content_path: {file_content_path}\n - file_count: {file_count}\n - file_size: {file_size:.3f} MB\n - file_hash_v1: {file_hash_v1}\n - file_hash_v2: {file_hash_v2}"
    },
    "at": {
        "isAtAll": True,
    },
}

dingtalk = dingtalk()
r = dingtalk.post(send_body)
logging.info(f"Send to DingTalk, with return: {r.text}")

