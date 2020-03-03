from .Base_Page import Base_Page
from utils.Wrapit import Wrapit

#locators


@Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_restaurant(self):
        try:
            self.click_element(self.popup_close)
        except NoSuchElementException:
            pass

        "Click on Create task button"
        result_flag = self.click_element(self.create_task_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "create task" button',
            negative='Failed to click on "create task" button',
            level='debug')

        return result_flag