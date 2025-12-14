#키보드로 입력된 숫자는 문자로 인식하므로 숫자로 변환해야 한다.
num = int(input("시작 곱의 숫자를 입력하세요. : "))
end = int(input("마지막 곱의 숫자를 입력하세요. : ")) + 1
while num < end:
    print(f"8 * {num} = {8 * num}")
    num = num + 1