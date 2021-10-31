import streamlit as st 
from login import *
from dashboard import *

############################## APP ##########################################

class App():

    def __init__(self):
        self.pages = {'login':login_page, 'home':home_page}
        self.currentPage = 'login'

    def update(self, newPage:str):
        self.currentPage = newPage

    def run(self):
        if self.currentPage == 'login':
            self.pages[self.currentPage]()
        if self.currentPage == 'home':
            self.pages[self.currentPage]()

################################ MAIN ##########################################

def main() -> None:
    app = App()
    app.run()
    
if __name__ == '__main__':
    main()
