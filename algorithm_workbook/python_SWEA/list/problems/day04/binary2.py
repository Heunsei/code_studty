def binary_serch(end_page, find_page):
    start_page = 1
    cnt = 0
    while start_page <= end_page:
        mid_page = (start_page + end_page)//2
        if mid_page == find_page:
            return cnt
        elif mid_page > find_page:
            end_page = mid_page
            cnt += 1
        elif mid_page < find_page:
            start_page = mid_page
            cnt +=1
    return cnt