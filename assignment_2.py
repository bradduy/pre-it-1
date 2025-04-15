# 🧠 Bài Tập Python – Sorting 
# -------------------------------------------

# Bài 1: Sắp Xếp Theo Tần Suất Xuất Hiện
# Sắp xếp danh sách theo tần suất xuất hiện (ít đến nhiều).
# Nếu bằng tần suất, số lớn hơn đứng trước.

def sort_by_frequency(nums: list[int]) -> list[int]:
    # 👉 TODO: Viết code ở đây
    pass


# Bài 2: Sắp Xếp Theo Chữ Số Cuối
# Sắp xếp theo chữ số cuối. Nếu trùng, sắp xếp theo giá trị tăng dần.

def sort_by_last_digit(nums: list[int]) -> list[int]:
    # 👉 TODO: Viết code ở đây
    pass


# Bài 3: Sắp Xếp Chuỗi Theo Độ Dài và Từ Điển
# Sắp xếp chuỗi theo độ dài (ngắn trước), nếu bằng thì theo alphabet

def sort_words(words: list[str]) -> list[str]:
    # 👉 TODO: Viết code ở đây
    pass


# -------------------------------
# ✅ TEST CASES
# -------------------------------

def check(expected, actual):
    if expected == actual:
        print("✅ ĐÚNG")
    else:
        print("❌ SAI")
        print("   Output đúng:", expected)
        print("   Hàm tự viết:", actual)


# Bài 1: Test
print("\n🧪 Bài 1: sort_by_frequency")
check([3, 6, 5, 5, 4, 4], sort_by_frequency([4, 5, 6, 5, 4, 3]))
check([1, 2, 2, 3, 3, 3], sort_by_frequency([1, 2, 2, 3, 3, 3]))

# Bài 2: Test
print("\n🧪 Bài 2: sort_by_last_digit")
check([42, 13, 25, 7, 9], sort_by_last_digit([25, 13, 9, 7, 42]))
check([22, 12, 31, 44], sort_by_last_digit([31, 22, 44, 12]))

# Bài 3: Test
print("\n🧪 Bài 3: sort_words")
check(["a", "bat", "cat", "apple", "banana"], sort_words(["apple", "bat", "banana", "cat", "a"]))
check(["hi", "yo", "hey", "hello"], sort_words(["hi", "hello", "hey", "yo"]))
