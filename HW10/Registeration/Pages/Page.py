from Registeration import Register
import time


class inputException(Exception):
    def __init__(self, msg):
        self.msg = msg


class BasePage:
    def __init__(self, page_view_file=None, preview=None, parent_page=None):
        self.page_view_file = page_view_file
        self.children_pages = []
        self.preview = preview
        self.parent_page = parent_page

    def add_children(self, *args):
        for i in range(len(args)):
            self.children_pages.append(args[i])


class GeneralPage(BasePage):
    def __init__(self, page_view_file, preview, parent_page=None):
        super().__init__(page_view_file, preview, parent_page)

    def show_page(self):
        with open(self.page_view_file, 'r') as view_page:
            page_content = view_page.read()
            print(page_content)

    def router(self):
        # this function gonna return a page which we are going to
        # and by this architecture we can make the page easily
        # in the next version we suspend the thread until any thing except CTRL+C is entered
        return_page = self.load_options()
        if return_page:
            GeneralPage.loading_page(return_page)
            return return_page
        while True:
            self.show_page()
            return_page = self.load_options()
            if return_page:
                GeneralPage.loading_page(return_page)
                return return_page

    def load_options(self):
        try:
            option = int(input("Enter your Option by number of each feature: "))
            if not isinstance(option, int):
                raise inputException("wrong Input option")
            else:
                if option >= len(self.children_pages) or option < 0:
                    raise inputException("wrong Input option")
        except (inputException, ValueError) as ie:
            GeneralPage.loading_page()
            return None
        else:
            if option >= len(self.children_pages):
                return self.parent_page
            else:
                return self.children_pages[option]

    @staticmethod
    def loading_page(return_page=None):
        if return_page:
            print(f"moving to {return_page.preview}", end=" ")
        else:
            print("OOps: Wrong Number Entered", end=" ")
        for i in range(3):
            print("!", end=" ")
            time.sleep(1)
        Register.clear_Terminal()


class WorkerPages(BasePage):
    def __init__(self, page_view_file=None, preview=None, func=None, parent_page=None):
        super().__init__(page_view_file, preview, parent_page)
        self.func = func

    def do_action(self):
        try:
            # the function itself handle the problems
            self.func()
            return self.parent_page
        except Exception:
            return self.parent_page


class ExitPage(BasePage):
    @classmethod
    def Exit(cls):
        exit(0)

