class IndentMaker:
    def __init__(self):
        self.tab_num = -1

    def __enter__(self):
        self.tab_num += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tab_num -= 1
        if exc_type is not None or exc_val is not None or exc_tb is not None:
            return True

    def indent_print(self, msg):
        print(self.tab_num * "\t" + msg)


with IndentMaker() as indent:
    indent.indent_print('hi!')
    with indent:
        indent.indent_print('talk is cheap')
        with indent:
            indent.indent_print('show me the code ')
    indent.indent_print('Torvalds')
