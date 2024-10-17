import hashlib

# md5

result1 = hashlib.md5(b'BNN College')
result2 = hashlib.md5(b'bnn college')

print(result1.digest())
print(result2.digest())

# sha1

message = "This is Raj."

result = hashlib.sha1(message.encode())
final = result.hexdigest()

print(final)