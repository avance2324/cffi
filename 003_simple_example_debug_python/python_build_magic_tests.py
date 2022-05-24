from magic_tests import ffi, lib


for i in range(5):
    print(f"[{i}] 3+{i} = {lib.add(3,i)}")

print("completed!")