def solution(s):
    n = len(s)
    if n < 2:
        return n
    answer = 0

    def get_length(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = get_length(i, i)
        len2 = get_length(i, i + 1)

        answer = max(answer, len1, len2)

    return answer

if __name__ == "__main__":
    user_input = input("문자열을 입력하세요:")
    if len(user_input) > 2500:
        print("입력 길이는 2,500 이하여야 합니다.")
    else:
        print(solution(user_input))