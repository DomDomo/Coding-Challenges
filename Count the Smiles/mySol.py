def count_smileys(arr):
    result = 0
    list = [':)', ':D', ';)', ';D', ':-)', ':-D', ';-)', ';-D', ':~)', ':~D', ';~)', ';~D']
    for i in arr:
        if i in list:
            result += 1
    return result