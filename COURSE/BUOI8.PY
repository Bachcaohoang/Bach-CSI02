# class Browser:
#     def __init__(self):
#         self.back_stack = []
#         self.forward_stack = []
#         self.current_page = None

#     def visit_page(self, item):
#         if self.current_page:
#             self.back_stack.append(self.current_page)
#         self.current_page = item
#         self.forward_stack = []

#     def back(self):
#         if self.back_stack:
#             self.forward_stack.append(self.current_page)
#             self.current_page = self.back_stack.pop()
#         return self.current_page

#     def forward(self):
#         if self.forward_stack:
#             self.back_stack.append(self.current_page)
#             self.current_page = self.forward_stack.pop()
#         return self.current_page
# #example
# if __name__ == "__main__":
#     my_browser = Browser()
    
#     my_browser.visit_page("www.example1.com")
#     my_browser.visit_page("www.example2.com")
    
#     print(my_browser.back())  
#     print(my_browser.back())  
    
#     print(my_browser.forward())
