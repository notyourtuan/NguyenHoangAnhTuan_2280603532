print ("Nhập các dòng văn bản (Nhập 'done' để kết thúc:)")
lines = []
while True:
    line = input()
    if line.lower() == "done":
        break
    lines.append(line)
print("\n Các dòng đã nhập sau khi chuyển thành chữ hoa: ")
for line in lines:
    print(line.upper())