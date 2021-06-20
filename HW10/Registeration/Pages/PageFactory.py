# here we make our pages in order to have our pages
from .Page import *

intro_Page = GeneralPage(page_view_file="/home/humanbeing/2021/Work/Maktab-Sharif/Homeworks/HW10/Registeration/Pages"
                                        "/IntroPage.txt", parent_page=None, preview="Home")
register_Page = WorkerPages(func=Register.Register.register_user, parent_page=intro_Page, preview="registration Page")
upload_page = WorkerPages(func=Register.Register.load_user_from_json_file, parent_page=intro_Page, preview="register "
                                                                                                           "by "
                                                                                                           "uploading "
                                                                                                           "file")
Exit_Page = ExitPage(preview="End Of Program")
show_all_Page = WorkerPages(func=Register.Register.show_all_users, preview="users list", parent_page=intro_Page)
intro_Page.add_children(register_Page, upload_page, show_all_Page)
# notice add exit page at the end of adding all the pages
# this is very important
intro_Page.add_children(Exit_Page)





