import os
import threading
import urllib
from urllib import request
from queue import Queue


class Downloader(threading.Thread):
    """Stream file downloader"""

    def __init__(self, queue):
        """Thread initialization"""
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Start thread"""
        while True:
            # get url from the queue
            url = self.queue.get()

            # download file
            self.download_file(url)

            # sent signal that task complete
            self.queue.task_done()

    def download_file(self, url):
        """Download file"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)

        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)


def main(urls):
    """Start program"""
    queue = Queue()

    # Start thread and queue
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    # We give the queue we need links to download
    for url in urls:
        queue.put(url)

    # We're waiting for the completion of the queue
    queue.join()


if __name__ == "__main__":
    urls = [
        "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
    ]
    main(urls)


# import os
# import urllib
# from urllib import request
# from threading import Thread
#
#
# class DownloadThread(Thread):
#     """An example of multi-threading downloading files from the internet"""
#
#     def __init__(self, url, name):
#         """Thread initialization"""
#         Thread.__init__(self)
#         self.name = name
#         self.url = url
#
#     def run(self):
#         """Thread start"""
#         handle = urllib.request.urlopen(self.url)
#         fname = os.path.basename(self.url)
#
#         with open(fname, "wb") as f_handler:
#             while True:
#                 chunk = handle.read(1024)
#                 if not chunk:
#                     break
#                 f_handler.write(chunk)
#
#         msg = "%s finish downloading %s!" % (self.name, self.url)
#         print(msg)
#
#
# def main(urls):
#     """Run the program"""
#
#     for item, url in enumerate(urls):
#         name = "Thread %s" % (item+1)
#         thread = DownloadThread(url, name)
#         thread.start()
#
#
# if __name__ == "__main__":
#     urls = [
#         "https://www.irs.gov/pub/irs-pdf/f1040.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
#     ]
#     main(urls)


# import random
# import time
# from threading import Thread
#
#
# class MyThread(Thread):
#     """A threading example"""
#     def __init__(self, name):
#         """Thread initialization"""
#         Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         """Start thread"""
#         amount = random.randint(3, 15)
#         time.sleep(amount)
#         message = "%s is running" % self.name
#         print(message)
#
#
# def create_threads():
#     """Create thread group"""
#     for i in range(5):
#         name = "Thread #%s" % (i+1)
#         my_thread = MyThread(name)
#         my_thread.start()
#
#
# if __name__ == "__main__":
#     create_threads()


# import threading
#
#
# lock = threading.Lock()
#
#
# def get_first_part():
#     lock.acquire()
#     try:
#         pass
#     finally:
#         lock.release()
#     return data
#
# def get_second_part():
#     lock.asquire()
#     try:
#         pass
#     finally:
#         lock.release()
#     return data


# from multiprocessing import Lock
#
# lock = Lock()
# lock.acquire()
#
# lock.release()

# counter = 0
#
# def process_item(item):
#     global counter
#     counter += 1
#     return counter
