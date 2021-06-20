from .PageFactory import *


def page_router():
    current_page = intro_Page
    while True:
        if isinstance(current_page, GeneralPage):
            # if it is general page some this should be done
            current_page.show_page()
            current_page = current_page.router()
        elif isinstance(current_page, WorkerPages):
            current_page = current_page.do_action()
        else:
            ExitPage.Exit()

