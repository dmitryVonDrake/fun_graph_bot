from lib import *

class Func:
    def __init__(self, func: str) -> None:
        self.func = func
        self.args = get_args(func)
        self.args_num = len(self.args)

    def func_to_python(self) -> None:
        self.lambda_str = fun_to_py(self.func)
    
    def exec_func(self, values: list) -> None:
        if self.lambda_str == None: raise Exception('No lambda string. Call func_to_python before this.')
        values_tuple_str = '('
        for value in values:
            values_tuple_str = values_tuple_str + str(value) + ', '
        values_tuple_str = values_tuple_str + ')'
        self.executable_func = self.lambda_str + values_tuple_str
        self.executable_func = (lambda x: eval_clojure(x))(self.executable_func)
    def get_func_exec(self):
        if self.lambda_str == None: raise Exception('No lambda string. Call func_to_python before this.')
        return eval_clojure(self.lambda_str)


if __name__ == '__main__':
    f: Func = Func('3*x**2 + 5*x - 7')
    f.func_to_python()
    fu = f.get_func_exec()
    print(fu(2))
