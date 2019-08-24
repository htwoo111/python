import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, url):
    req = urllib.request.urlopen(url)
    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg",  "https://rpic.douyucdn.cn/live-cover/roomCover/2019/07/17/73ac6b480be404700713cbc1fc52aaf4_big.jpg?x-oss-process=image/format,webp"),
        gevent.spawn(downloader,"2.jpg", "https://rpic.douyucdn.cn/asrpic/190720/927053_6611509_74112_2_1027.jpg?x-oss-process=image/format,webp")
    ])


if __name__ == "__main__":
    main()

# https://rpic.douyucdn.cn/live-cover/roomCover/2019/07/17/73ac6b480be404700713cbc1fc52aaf4_big.jpg?x-oss-process=image/format,webp
# https://rpic.douyucdn.cn/asrpic/190720/927053_6611509_74112_2_1027.jpg?x-oss-process=image/format,webp