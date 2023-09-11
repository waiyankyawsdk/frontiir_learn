import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8016
DB = 'rd-demo'
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,   
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)
print(url,uid)
# #create
# args = {
#     'name': 'Test Patient from JSONRPC',
#     'create_uid': uid,
# }
# patient_id = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'create', args)
# print("Test Created **********************",patient_id)

# #update
# vals= {
#     'age': 15
# }
# patient_id = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'write', [13],vals)
# print("Test Updated **********************",patient_id)

# #delete
# patient= call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'unlink', [11,12])
# print("Test Deleted **********************",patient)