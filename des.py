import pyDes
import base64

# 1. 明文
data = "This is test text."
# 2. 密钥，生成加密器
k = pyDes.des("SchoolEx", pad=None, padmode=pyDes.PAD_PKCS5)
# 3. 加密得到密文
d = k.encrypt(data)
# 4. 打印密文
print("Encrypted: %r" % d)
# 5. 打印解密得到的明文
print("Decrypted: %r" % k.decrypt(d))
# 6. 密文 base64 加密
print("base64: %s" % base64.b64encode(d))
