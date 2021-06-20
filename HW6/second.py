def str_calculator(string:str):
    try:
        res=eval(string)
        return res
    except SyntaxError as se:
        return f"[{string}] ----> Python_SytaxError"

input_str= input("Input you String: ")
print(str_calculator(input_str))



