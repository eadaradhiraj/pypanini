import pypanini.pada_rules as pr
print("01.1096 in pr?", "01.1096" in pr.PADA_MAP_ID)
print("vi override:", pr.PADA_MAP_ID["01.1096"].get("vi"))
