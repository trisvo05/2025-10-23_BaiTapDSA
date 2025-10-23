def solution(N, M, watering_can):
    # Khởi tạo ma trận vườn N x N với giá trị 0 (chưa tưới)
    garden = [[0] * N for _ in range(N)]

    # Duyệt qua từng vòi phun
    for r, c, power in watering_can:
        # Tưới vị trí chính
        garden[r][c] = 1

        # 4 hướng: lên, xuống, trái, phải
        for i in range(1, power + 1):
            # Trên
            if r - i >= 0:
                garden[r - i][c] = 1
            # Dưới
            if r + i < N:
                garden[r + i][c] = 1
            # Trái
            if c - i >= 0:
                garden[r][c - i] = 1
            # Phải
            if c + i < N:
                garden[r][c + i] = 1

    # Đếm số ô chưa được tưới (vẫn = 0)
    dry_count = sum(row.count(0) for row in garden)

    return dry_count

watering_can_input = input("Nhập watering_can (ví dụ [[2,2,2],[0,0,1]]): ")

# Tự chuyển chuỗi thành list 
watering_can = []
rows = watering_can_input.strip('[]').split('],[')
for row in rows:
    numbers = row.replace('[', '').replace(']', '').split(',')
    watering_can.append([int(num) for num in numbers if num.strip() != ''])

N = int(input("Nhập N: "))
M = int(input("Nhập M: "))

print(solution(N, M, watering_can))