url = "http://localhost:8016/"
db = 'rd-demo'
username = 'admin'
password = 'b9ecd11827b9cff403250a323828dc0c127abf6e'

import xmlrpc.client
info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = info['host'], info['database'], info['user'], info['password']

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print(version)

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
res = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
print(res)

#search
partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]],{'offset': 10, 'limit': 5})
print(partner_ids)

#search_count
partner_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
print(partner_count)

#read
ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 1})
[record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
print(len(record))

#read with only 3 fields
record = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
print(record)

#field_get
partner_fields = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
print(partner_fields)

#search_read
partners = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print(partners)

for partner in partners:
    print(partner)

#create
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "XMLRPC New Partner"}])
print("created success partner_id : ", id)

#write
res = models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
print("Is it updated? : ",res)
# get record name after having changed it
update_partner = models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
print(update_partner)

# #unlink
# res = models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[59]])
# print("Is it deleted? : ", res)
# # check if the deleted record is still in the database
# partner = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', 59]]])
# print(partner)

# id = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
#     'name': "Custom Model_12",
#     'model': "x_custom_model_12",
#     'state': 'manual',
# }])
# print(id)
# fget = models.execute_kw(db, uid, password, 'x_custom_model', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
# print(fget)

id = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
    'name': "Custom Model 123",
    'model': "x_custom_123",
    'state': 'manual',
}])

res = models.execute_kw(db, uid, password, 'ir.model.fields', 'create', [{
    'model_id': id,
    'name': 'x_description',
    'ttype': 'char',
    'state': 'manual',
    'required': True,
}])
print(res)
record_id = models.execute_kw(db, uid, password, 'x_custom', 'create', [{'x_name': "test record"}])
res = models.execute_kw(db, uid, password, 'x_custom', 'read', [[record_id]])
print(res)