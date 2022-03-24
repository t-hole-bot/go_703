import random
import time
import requests
API_ROOT = 'https://t-hole.red/_api/v1/'
prox =[
    '61.135.169.55',
    '61.135.169.22',
    '220.181.51.40',
    '220.181.51.39',
    '111.13.13.74',
    '111.13.13.73',
    '111.13.13.72',
    '111.13.13.71',
    '111.13.13.6',
    '111.13.13.5',
    '111.13.13.4',
    '111.13.13.3',
    '101.254.184.206',
    '1.95.9.244'
]
proxyi = [{'http':pro} for pro in prox]
text = [
    '冲','接着冲','给爷冲','dz快来请火锅','我要看大结局','gkd','我来助大家一臂之力','gkdgkd'
]

def post(text:str,token:str,proxyi)->requests.Response:
    headers = {
        'user-agent':r'Mozilla/6.0 (Windows NT 9.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'User-Token':token,
              }
    POST_URL = API_ROOT + 'docomment'
    data = {
        'pid' : 1075,
        'text' : text,
        'use_title': ''
            }
    
    req = requests.post(url=POST_URL,data=data,headers=headers,proxies=proxyi)
    return req #cookie


def main():
    token = '5489e8d55d25d8ec'
    count = 1
    init = random.randint(1500000,2000000)
    for i in range(init,init+10):
        t_token = f'{token}_{i}'
        proxy_used = proxyi[random.randint(0,13)]
        x = post(text[random.randint(0,7)],t_token,proxy_used)
        print(x.text)
        
        print(f'count:{count}')
        print(f'i:{i}')
        print(f'proxy:{proxy_used}')
        count += 1
        time.sleep(3.5)

if __name__ == '__main__':
    main()
