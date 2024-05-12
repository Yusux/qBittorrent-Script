# qBittorrent Scripts

Simple scripts to notify you when a download starts or completes in qBittorrent via DingTalk.

## Usage

Fill `your_access_token` and `your_secret` in `dingtalk_utils.py` with your own DingTalk robot settings.

```python
    def __init__(self):
        self.access_token = "your_access_token"
        self.secret = "your_secret"
        self.webhook = None
```

Change the log path in `download_start.py` and `download_complete.py` to your own log path.

```python
    logging.basicConfig(filename='/path/to/downloads.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
```

Add the scripts to qBittorrent in "Options" -> "Downloads" -> "Run external program on torrent completion" and "Run external program on torrent start". The added scripts should be like:

```bash
python3 /path/to/download_start.py %N %D
```

```bash
python3 /path/to/download_complete.py %N %F %D %C %Z %I %J
```

## License

MIT