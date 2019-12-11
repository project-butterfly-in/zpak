import sys  
import os
package_path = "{}{}{}{}".format(os.pardir,os.sep,'package',os.sep)
sys.path.append("{}{}".format(package_path,'download-manager'))
from downloader import Downloader

if __name__ == "__main__":
    print("Testing Downloading")
    Downloader(URL="https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png", name="cat_image.png")