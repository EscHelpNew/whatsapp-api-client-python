from os import environ

from whatsapp_api_client_python import API as API

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

greenApi = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    result = greenApi.sending.sendFileByUpload('79001234567@c.us', 
        'C:\Games\PicFromDisk.png', 
        'PicFromDisk.png', 'Picture from disk')
    print(result.data)

if __name__ == "__main__":
    main()