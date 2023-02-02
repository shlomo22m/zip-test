import zipfile
import zlib
from dotenv import load_dotenv
import os


class Col:
    load_dotenv()
    def compress(self,file_names):
        """shlomo mhadker
            1.2.23
            function that get files nam in a list and zip them all"""


        path='C:\\Users\\shlomo\\PycharmProjects\\test-script\\'
        compression = zipfile.ZIP_DEFLATED

        zf = zipfile.ZipFile("new file2.zip", mode="w")
        try:
            for file_name in file_names:

                zf.write(path + file_name, file_name, compress_type=compression)
        except FileNotFoundError:
            print("An error occurred")
            return 0
        finally:
            zf.close()
        return 1

