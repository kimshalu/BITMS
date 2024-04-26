def reversecharacters(ip):
    char_list = list(ip)
    start = 0
    end = len(char_list) - 1
    while start < end:
        if not char_list[start].isalpha():
            start += 1
        elif not char_list[end].isalpha():
            end -= 1

        else:
            char_list[start], char_list[end] = char_list[end], char_list[start]
            start += 1
            end -= 1

    return ''.join(char_list)

ip = "bitm college's located in ballari? is't rihgt!!!"
revstr = reversecharacters(ip)
print(revstr)  