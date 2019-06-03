# from os_handling_modules import return_logged
from os_handling_modules import *

print(return_logged_in_user())

secret_encoded_files = encode_file('README.md')
print(secret_encoded_files)

secret_decoded_files = decode_file(secret_encoded_files)
print(secret_decoded_files)





