from selenium.webdriver.common.by import By
import allure
from mainObject import MainObject
from cartObject import CartObject
from productObject import ProductObject
from registrationObject import RegistrationObject
from adminObject import AdminObject

#################################1##################################
@allure.feature("First test")
@allure.title("screenshot")
def test_screenshot(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.open_product()
    driver.implicitly_wait(1)
    product_page.image_click()
    driver.implicitly_wait(1)
    product_page.next_image()
    driver.implicitly_wait(1)
    product_page.next_image()
    driver.implicitly_wait(1)

#################################2##################################
@allure.feature("Second test")
@allure.title("cart")
def test_cart(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    cart_page = CartObject(driver, logger)
    driver.implicitly_wait(1)
    cart_page.add_to_cart_button()
    driver.implicitly_wait(1)
    cart_page.open_cart()
    driver.implicitly_wait(1)
    cart_items = cart_page.get_cart_items()
    driver.implicitly_wait(1)
    if cart_items:
        print("Тест пройден")
    driver.implicitly_wait(1)

#################################3##################################
@allure.feature("Third test")
@allure.title("category")
def test_category(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.open_pc_category()
    driver.implicitly_wait(1)
    product_items = main_page.get_pc_items()
    driver.implicitly_wait(1)
    if product_items:
        print("Тест пройден")

#################################4##################################
@allure.feature("Fourth test")
@allure.title("registration")
def test_registration(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    register_page = RegistrationObject(driver, logger)
    driver.implicitly_wait(1)
    register_page.open_registration_page()
    driver.implicitly_wait(1)
    register_page.registration_user("aaaaaa", "aaaaaa", "aaaaaa@gmail.com", "5214125", "aaAAaa@")
    driver.implicitly_wait(1)

#################################5##################################
@allure.feature("Fifth test")
@allure.title("input")
def test_main_input(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.search("Iphone")
    driver.implicitly_wait(1)

#################################6##################################
@allure.feature("Sixth test")
@allure.title("wishlist")
def test_add_to_wishlist(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_to_wishlist(2)
    driver.implicitly_wait(1)

#################################7##################################
@allure.feature("Seventh test")
@allure.title("camera")
def test_add_camera(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.camera()
    driver.implicitly_wait(1)
    product_page.add_to_cart_camera()
    driver.implicitly_wait(1)
#################################8##################################
@allure.feature("Eigth test")
@allure.title("clipboard")
def test_add_clipboard(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.open_category("Планшеты")
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_to_cart_clipboard()
    driver.implicitly_wait(1)

#################################9##################################
@allure.feature("Ninth test")
@allure.title("htc")
def test_add_htc(driver,logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    driver.implicitly_wait(1)
    main_page.open_category("Телефоны")
    driver.implicitly_wait(1)
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1)
    product_page.add_to_cart_htc()
    driver.implicitly_wait(1)

#################################10##################################
@allure.feature("Tenth test")
@allure.title("review")
def test_submit_review(driver,logger):
    main_page = MainObject(driver, logger)
    driver.implicitly_wait(1)
    main_page.go()
    driver.implicitly_wait(1)
    search_item = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")
    search_item.click()
    product_page = ProductObject(driver, logger)
    driver.implicitly_wait(1.5)
    product_page.open_review_form()
    driver.implicitly_wait(1.5)
    product_page.submit_review("aaaaaaa", "ааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")
    driver.implicitly_wait(1.5)

@allure.feature("Eleventh test")
@allure.title("Login")
def test_login_admin(driver, logger):
    admin_page = AdminObject(driver, logger)
    admin_page.login("user", "bitnami")


@allure.feature("Twelfth test")
@allure.title("Category")
def test_create_category(driver, logger):
    admin_page = AdminObject(driver, logger)
    admin_page.create_category("Devices", "Devices", "Devices")


@allure.feature("Thirteenth test")
@allure.title("Product")
def test_create_product(driver, logger):
    admin_page = AdminObject(driver, logger)
    admin_page.create_product("Computer mouse 1", "Computer mouse 1", "Computer mouse 1", "Devices", "Computer_mouse_1")
    admin_page.create_product("Computer mouse 2", "Computer mouse 2", "Computer mouse 2", "Devices", "Computer_mouse_2")
    admin_page.create_product("Keyboard 1", "Keyboard 1", "Keyboard 1", "Devices", "Keyboard_1")
    admin_page.create_product("Keyboard 2", "Keyboard 2", "Keyboard 2", "Devices", "Keyboard_2")



@allure.feature("Fourteenth test")
@allure.title("Check")
def test_check_created_products(driver, logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    main_page.search("Mouse")
    product_items = main_page.get_product_items()
    assert len(product_items) == 2, f"Ожидалось 2 мышки, но найдено {len(product_items)}"
    main_page.search("Keyboard")
    product_items = main_page.get_product_items()
    assert len(product_items) == 2, f"Ожидалось 2 клавиатуры, но найдено {len(product_items)}"


@allure.feature("Fifteenth test")
@allure.title("Delete")
def test_delete_created_products(driver, logger):
    admin_page = AdminObject(driver, logger)
    admin_page.go_admin_page()
    admin_page.login("user", "bitnami")
    admin_page.delete_product()


@allure.feature("Sixteenth test")
@allure.title("Check deleted")
def test_check_deleted_products(driver, logger):
    main_page = MainObject(driver, logger)
    main_page.go()
    main_page.search("Mouse")
    product_items = main_page.get_product_items()
    assert len(product_items) == 1, f"Ожидалась 1 мышка, но найдено {len(product_items)}"

    main_page.search("Keyboard")
    product_items = main_page.get_product_items()
    assert len(product_items) == 1, f"Ожидалась 1 клавиатура, но найдено {len(product_items)}"