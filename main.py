import requests

# api url
url = os.getenv("URL")
token = os.getenv("TOKEN")
# phone send whatsapp
movil  = [os.getenv("PHONE_1"), os.getenv("PHONE_2")]
# message
body = "BOT_ADDAMS-EVA :=> msg test testing DJANGO-PYTHON"

for i in movil:
    # THIS PAYLOAD IS IN API ultramsg.com
    payload = f"token={token}&to=%2B{i}&body={body}&priority=1&referenceId="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)