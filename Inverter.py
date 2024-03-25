"""Inserter"""
def main():
    """Inverter"""
    bina = input()
    ans = ""
    for i in bina:
        if i == "0":
            ans += "1"
        elif i == "1":
            ans += "0"
    for i in range(len(ans)):
        if ans[i] == "1":
            print(ans[i:])
            break
main()
