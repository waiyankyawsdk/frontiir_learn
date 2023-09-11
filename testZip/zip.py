import zipfile
import io
with open('/home/waiyankyaw3/ff3b/', 'rb') as file:
    odoo_binary_content = file.read()

zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
    zip_file.write('ff3b10af78148ffa58aae0b95ba688446167cff2_69896:', odoo_binary_content)
zip_buffer.seek(0)

print(zip_file)
