"""RLED"""
def main():
    """RLED"""
    coding = input()
    encoded = ""
    count = 1
    for i in range(1, len(coding)):
        if coding[i] == coding[i-1]:
            count += 1
        else:
            encoded += str(count) + coding[i-1]
            count = 1
    encoded += str(count) + coding[-1]
    print(encoded)
main()

