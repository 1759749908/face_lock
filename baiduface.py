import base64

from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '15545840'
API_KEY = 'X7jA6x9zei2G2kjIEkiK90f5'
SECRET_KEY = 'GgKDR2Q1v6qzdPodvNvrbndSMZQhGcrp'

'''创建应用'''
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

'''
def base64_data(filepath):
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read())
images=[{'image':base64_data('qiwei.jpg'),'image_type':'BASE64',},{'image':base64_data('yuwenwen.jpg'),'image_type':'BASE64'},]
'''
""" 调用人脸对比 """
def faceimage(image1,image2):
    result = client.match([
        {
            'image': str(base64.b64encode(open(image1, 'rb').read()), 'utf-8'),
            'image_type': 'BASE64',
        },
        {
            'image': str(base64.b64encode(open(image2, 'rb').read()), 'utf-8'),
            'image_type': 'BASE64',
        }
    ])

    #print(result)

    """判断是否为一个人"""
    result_score = result['result']['score']

    if result_score >= 80:
        #print('相似度为%s,完全一个人' % result_score)
        return 1
    else:
        #print('相似度仅为%s，不是同一个人' % result_score)
        return 0


if __name__ == "__main__":
    faceimage("danil.jpg","girl_1.jpg")