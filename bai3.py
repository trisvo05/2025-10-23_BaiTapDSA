def solution(N, M, area, C):
    grid = [[0] * N for _ in range(N)]

    for i in range(M):
        r1, c1, r2, c2, color = area[i]
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 0:
                    grid[r][c] = color
                elif grid[r][c] != color and grid[r][c] != 3:
                    grid[r][c] = 3  # tô xám
                # nếu đã xám thì bỏ qua

    count = sum(row.count(C) for row in grid)
    return count


# --- Nhập dữ liệu từ người dùng ---
N = int(input("Nhập N: "))
M = int(input("Nhập M: "))
raw = input("Nhập area (ví dụ [[1,1,5,4,1],[2,3,6,6,2]]): ")

# Chuyển chuỗi -> danh sách list[list[int]]
rows = raw.strip('[]').split('],[')
area = []
for row in rows:
    numbers = row.replace('[', '').replace(']', '').split(',')
    area.append([int(num) for num in numbers if num.strip() != ''])

C = int(input("Nhập C (1=đỏ, 2=xanh, 3=xám): "))

# --- In kết quả ---
print("Kết quả:", solution(N, M, area, C))