from cryptography.fernet import Fernet
#创建字节串
ci_key = Fernet.generate_key()
#创建密匙
ci = Fernet(ci_key)

#加密
text = b'189516189161asdqdqwdqdsadadasd'
encr_text = ci.encrypt(text)

#解密
decr_text = ci.decrypt(encr_text)
print(decr_text)



