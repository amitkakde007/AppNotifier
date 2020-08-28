from win10toast import ToastNotifier
import time
import requests

url='https://reqres.in/api/users?page=1'

req=requests.get(url)
data=req.json()
data['data']
for d in data['data']:
    if 'Charles' in d['first_name']:
        email=d['email']
notify=ToastNotifier()

notify.show_toast(
    title='Python World',
    msg=f'We are pulling this email: {email} from an json endpoint',
    threaded=True
)
#while notify.notification_active(): time.sleep(0.1)