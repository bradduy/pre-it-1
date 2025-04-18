def sort_by_frequency(nums: list[int]) -> list[int]:
    # Đầu tiên: đếm tần suất các số xuất hiện
    frequency = {}
    for num in nums:
        # num = 3
        if num in frequency:
            frequency[num] = frequency[num] + 1
        else:
            frequency[num] = 1

    # Tạo một danh sách chứa các cặp số và tần suất: [(số, tần suất),...]
    pairs = []
    for num in nums:
        pairs.append((num, frequency[num]))

    # Duyệt qua tất cả phần tử
    # [(4, 2), (5, 2), (6, 1), (5, 2), (4, 2), (3, 1)]
    for i in range(6): # 4 
        # Mỗi lần duyệt sẽ đưa phần tử lớn nhất (theo điều kiện) xuống cuối danh sách
        for j in range(5):
            print(f"{i} and {j}")
            # Lấy tần suất và số ra để dễ hiểu
            so_hien_tai = pairs[j][0]
            tan_suat_hien_tai = pairs[j][1]

            so_tiep_theo = pairs[j + 1][0]
            tan_suat_tiep_theo = pairs[j + 1][1]

            # Bắt đầu so sánh để đổi chỗ
            can_doi_cho = False

            # Nếu tần suất hiện tại lớn hơn tần suất tiếp theo thì phải đổi chỗ
            if tan_suat_hien_tai > tan_suat_tiep_theo:
                can_doi_cho = True
            elif tan_suat_hien_tai == tan_suat_tiep_theo: # Nếu hai tần suất bằng nhau, thì số lớn hơn đứng trước
                if so_hien_tai < so_tiep_theo:
                    can_doi_cho = True

            # Nếu cần đổi chỗ thì đổi 2 phần tử
            if can_doi_cho:
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp

    result = []
    for pair in pairs:
        result.append(pair[0])

    return result


print(sort_by_frequency([4, 5, 6, 5, 4, 3]))