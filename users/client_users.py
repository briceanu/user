import requests
import sys



def create():
    url = 'http://127.0.0.1:8000/user/signup'

    data = {'username':'qawdawdawdawdd',
            'password':'Aawdawd123',
            'email':'gmail.com'}


    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.url)
    print(res.text)



if __name__ == "__main__":
    if sys.argv[1]== 'create':
        create()

    else:
        exit(0) 

