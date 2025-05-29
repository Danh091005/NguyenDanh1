import hashlib

# Dữ liệu ban đầu
data = "Xin chào, đây là dữ liệu gốc.".encode()

# Tính băm SHA-256
hash_sha256 = hashlib.sha256(data).hexdigest()

# Tính băm SHA-512
hash_sha512 = hashlib.sha512(data).hexdigest()

print("Dữ liệu gốc:", data.decode())
print("SHA-256:", hash_sha256)
print("SHA-512:", hash_sha512)
# Dữ liệu đã bị thay đổi
data_modified = "Xin chào, đây là dữ liệu đã bị sửa.".encode()

# Tính lại băm SHA-256 và SHA-512
hash_sha256_modified = hashlib.sha256(data_modified).hexdigest()
hash_sha512_modified = hashlib.sha512(data_modified).hexdigest()

print("\n--- Dữ liệu đã bị sửa ---")
print("Dữ liệu mới:", data_modified.decode())
print("SHA-256 mới:", hash_sha256_modified)
print("SHA-512 mới:", hash_sha512_modified)

# So sánh để kiểm tra tính toàn vẹn
print("\n--- So sánh băm SHA-256 ---")
if hash_sha256 == hash_sha256_modified:
    print("DỮ LIỆU KHÔNG BỊ THAY ĐỔI (SHA-256)")
else:
    print("⚠️ DỮ LIỆU ĐÃ BỊ THAY ĐỔI (SHA-256)")

print("\n--- So sánh băm SHA-512 ---")
if hash_sha512 == hash_sha512_modified:
    print("DỮ LIỆU KHÔNG BỊ THAY ĐỔI (SHA-512)")
else:
    print("⚠️ DỮ LIỆU ĐÃ BỊ THAY ĐỔI (SHA-512)")
