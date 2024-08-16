# URLの画像をバイナリ文字列に置き換える
# 画像のURLは適宜差し替える

import requests
import base64

URL = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhW3KMdODRKj2N4RquyZx3ZOKak9LtfnfsVcre4YZ3fgD4i9wadruI5voBaHcoTaLp7YTi_fjz_TKsP0z8tGPv5i_pqzJdOz390JpEQSFZr_XIXr-Z2i5dAYfedRPBw3Xf3koGSnQ_WC94/s140/icon_business_man08.png'

def url_to_binary_string(image_url):
    # 画像をダウンロード
    response = requests.get(image_url)
    response.raise_for_status()  # エラーチェック

    # バイナリデータを取得
    image_data = response.content

    # バイナリデータを文字列に変換
    binary_string = base64.b64encode(image_data).decode('utf-8')

    return binary_string

# 使用例
binary_string = url_to_binary_string(URL)
print(binary_string)