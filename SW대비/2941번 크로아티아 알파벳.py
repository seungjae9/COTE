# 2941번 크로아티아 알파벳


croa = input()
change = ["lj", "c=", "c-", "nj", "dz=", "d-", "z=", "s="]

for i in change:
    croa = croa.replace(i, "*")


print(len(croa))

# if "lj" in croa:
#     croa = croa.replace("lj", "*")
# if "c=" in croa:
#     croa = croa.replace("c=", "*")
# if "s=" in croa:
#     croa = croa.replace("s=", "*")
# if "c-" in croa:
#     croa = croa.replace("c-", "*")
# if "nj" in croa:
#     croa = croa.replace("nj", "*")
# if "dz=" in croa:
#     croa = croa.replace("dz=", "*")
# if "d-" in croa:
#     croa = croa.replace("d-", "*")
# if "z=" in croa:
#     croa = croa.replace("z=", "*")
