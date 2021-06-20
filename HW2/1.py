def reverseStr(input_str):
    mylist = list(input_str)
    mylist.reverse()
    return "".join(mylist)

def is_pal(input_str):
    return True if reverseStr(input_str) == input_str else False

in_str = input()
print(reverseStr(in_str))
print(is_pal(in_str))
