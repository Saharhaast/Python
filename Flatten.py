"""FLATTER"""
import json
def main(value: list):
    """Flatten"""
    ans = []
    for raw in value:
        if isinstance(raw, list):
            ans += main(raw)
        else:
            ans.append(raw)
    ans.sort(reverse=True)
    return ans
print(main(json.loads(input())))
