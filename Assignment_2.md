# 🧠 Bài Tập Python – Sorting
---

## Bài 1: Sắp Xếp Theo Tần Suất Xuất Hiện

Viết function sắp xếp danh sách theo **tần suất xuất hiện** của từng số (tần suất thấp hơn đứng trước). Nếu hai số có cùng tần suất, số nào **lớn hơn** thì đứng trước.

### Function is defined as:
```python
def sort_by_frequency(nums: list[int]) -> list[int]:
```

## Bài 2: Sắp Xếp Theo Chữ Số Cuối

Cho một danh sách các số nguyên, hãy viết function để trả về danh sách đó sau khi đã được sắp xếp theo **chữ số cuối cùng** của từng số.

- Nếu hai số có cùng chữ số cuối, hãy sắp xếp chúng theo **giá trị tăng dần**.

---

### Function is defined as:
```python
def sort_by_last_digit(nums: list[int]) -> list[int]:
```

---

### **Bài 3: Sắp Xếp Chuỗi Theo Độ Dài và Từ Điển**

Viết một function nhận vào một danh sách các chuỗi và trả về danh sách đó sau khi được sắp xếp theo quy tắc:

1. Chuỗi **ngắn hơn** đứng trước chuỗi dài hơn
2. Nếu hai chuỗi có cùng độ dài, thì sắp xếp **theo thứ tự từ điển (alphabet)**

---

### Function is defined as:
```python
def sort_words(words: list[str]) -> list[str]:
