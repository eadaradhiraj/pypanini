import json
from test_dhatu import validate_dhatu

matched, total = validate_dhatu("03.0001", verbose=True, prefix="pra")
print(f"\nResult: {matched}/{total}")
