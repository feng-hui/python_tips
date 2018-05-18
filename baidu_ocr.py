# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/26 14:58'
# @email = 'fengh@asto-inc.com'
from aip import AipOcr


class OcrBaiDu(object):

    def __init__(self, app_id, api_key, secret_key):
        self.app_id = app_id
        self.api_key = api_key
        self.secret_key = secret_key

    def my_client(self):
        client = AipOcr(self.app_id, self.api_key, self.secret_key)
        return client

    @staticmethod
    def get_file_content(file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()


if __name__ == "__main__":
    APP_ID = '552820efc7574b7b9a2e2c54f07af9e2 '
    API_KEY = '650c52055c304b8daae0e97d193b55fb'
    SECRET_KEY = '70f001ce6fe7438cb484068a8517de6f'
    ocr_baidu = OcrBaiDu(APP_ID, API_KEY, SECRET_KEY)
    client = ocr_baidu.my_client()
    # options = {}
    # options["language_type"] = "CHN_ENG"
    # options["detect_direction"] = "true"
    # options["detect_language"] = "true"
    # options["probability"] = "true"
    # # print(client.basicGeneralUrl('http://www.ometal.com/files/2018/3/24/2018324635261449_Snap1.gif', options))
    image = ocr_baidu.get_file_content('123dd.png')
    result = client.basicGeneral(image)
    print(result, type(result))
