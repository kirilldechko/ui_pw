

add_button = ("//a[@class='product-item-link' and contains(text(),'Ana Running Short')]"
              "//..//following-sibling::div[4]//div//div//form/button/span")
added_item_in_cart = "//span[@class='counter-number']"


def commodity_path(name):
    return f"//div[@class='product-item-info']//a[@class='product-item-link' and contains(text(), '{name}')]"


def size_button(size, commodity_name):
    return (f"//a[contains(text(), '{commodity_name}')]//..//following-sibling::div[3]//div//div//div"
            f"[@class='swatch-option text' and text()='{size}']")


def selected_size(size, commodity_name):
    return (f"//a[contains(text(), '{commodity_name}')]//..//following-sibling::div[3]//div//div//"
            f"div[@class='swatch-option text selected' and text()='{size}']")


def color_button(color, commodity_name):
    return (f"//a[contains(text(),'{commodity_name}')]//..//following-sibling::div[3]/div[2]"
            f"//div[@class='swatch-option color' and @aria-label='{color}']")


def selected_color(color, commodity_name):
    return (f"//a[contains(text(),'{commodity_name}')]//..//following-sibling::div[3]/div[2]//"
            f"div[@class='swatch-option color selected' and @aria-label='{color}']")


def success_text(text):
    return (f"//div[contains(@data-bind, 'html: $parent.prepareMessageForHtml(message.text)') "
            f"and contains(text(), 'You added {text} to your')]")
