
from pages.Add_Remove_elements_page import AddRemoveElementsPage

def test_page_is_correct(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    # load the page
    add_remove_page.loadPage()
    # check title is correct
    assert add_remove_page.getTitlePage() == "Add/Remove Elements"
# testam butonul de add / apare del button
def test_add_element_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    #load page
    add_remove_page.loadPage()
    #click add
    add_remove_page.clickAddButton()
    #check delete button is displayed
    assert  add_remove_page.isDeleteButtonDisplyed() == True, "Error"
# Del button dispare
def test_delete_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    #load page
    add_remove_page.loadPage()
    add_remove_page.clickAddButton()
    add_remove_page.clickDelButton()
    assert add_remove_page.getNumberOfDelBotton() == 0, "Error"
# apasam de 10 ori AddElement
def test_delete_button_10(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.loadPage()
    for i in range(10):
        add_remove_page.clickAddButton()
    assert add_remove_page.getNumberOfDelBotton() == 10, "Error"
