import os, base64, requests
from nacl import public, encoding
tok=os.environ["DEST_PAT"]; val=os.environ["VAL"]; repo="omerorucu/merqur_relase"
h={"Authorization":"token "+tok,"Accept":"application/vnd.github+json"}
k=requests.get(f"https://api.github.com/repos/{repo}/actions/secrets/public-key",headers=h).json()
box=public.SealedBox(public.PublicKey(k["key"].encode(), encoding.Base64Encoder))
enc=base64.b64encode(box.encrypt(val.encode())).decode()
r=requests.put(f"https://api.github.com/repos/{repo}/actions/secrets/MACOS_CERT_P12_BASE64",headers=h,json={"encrypted_value":enc,"key_id":k["key_id"]})
print("PUT",r.status_code,r.text[:150])
