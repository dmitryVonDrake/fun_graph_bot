import re


get_args_num = lambda f: len(set(re.findall(r'[a-z]', f)))
get_args = lambda f: list(dict.fromkeys(re.findall(r'[a-z]', f)))

def fun_to_py(func: str) -> str:
    lambda_str = '(lambda'
    args: list = get_args(func)
    for arg in args:
        lambda_str += ' %s,'%(arg)
    lambda_str = lambda_str[:-1] + ': ' + func + ')'
    return lambda_str

eval_clojure = lambda x: lambda y: eval(x + '(' + str(y) + ')')