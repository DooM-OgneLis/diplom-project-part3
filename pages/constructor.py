from pages.head_panel import HeadPanel
from locators.constructor import ConstructorLocators as CL

class Constructor(HeadPanel):

    def click_ingredients_in_list(self, ingred_locator):
        self.scroll_to_element(CL.BUN_CRATOR_N_200I)
        self.click_element_with_wait(CL.BUN_CRATOR_N_200I)