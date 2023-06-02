import json
import base64

def decrypt_dpapi(dpapi_file):
    parameter_load = json.load(dpapi_file)
    encrypted_key = parameter_load['os_crypt']['encrypted_key']
    decrypted_key = base64.b64decode(encrypted_key)
    open("dpapi.blob",'wb').write(decrypted_key[5:])

if __name__ == "__main__":
    dpapi_file = open('AppData/Local/Google/Chrome/User Data/Local State', 'rb')
    decrypt_dpapi(dpapi_file)