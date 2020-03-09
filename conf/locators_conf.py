#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

# Locators for create task object
popup_close= "xpath,//i[contains(@class,'cSxoYv')]"
create_task = "xpath,//button[contains(text(),'Create a Task')]"

# Locators to set pick up and drop address
pick_up_click= "xpath,//p[contains(text(),'Search pickup location')]"
drop_click = "xpath,//p[contains(text(),'Search drop location')]"

partial_address = "xpath,//input[@id='places-autocomplete']"
area_location = "xpath,//div[contains(@class,'ccewWU')]"
flat_number = "xpath,//input[@name='apartmentAddress']"
continue_button= "xpath,//button[contains(text(),'Continue')]"

# Locator to fetch the expected shipping amount
amount_to_pay= "xpath,//div[contains(@class,'bbMAot')]/div/p/descendant::font"

# Locators for options in home page
restaurant = "xpath,//p[contains(text(),'Restaurants')]"
alert_message = "xpath,//p[contains(text(),'Please select a location')]"
bangalore_location = "xpath,//a[contains(text(),'Bangalore')]"
bangalore_restaurants = "xpath,//h1[contains(text(),'Restaurants in')]"

# Locators for Partners
sign_me_up = "xpath,//a[contains(text(),'Sign me up')]"
partner_button = "xpath,//button[contains(text(),'Dunzo for partners')]"

name_field = "xpath,//input[@name='name']"
city_field = "xpath,//input[@name='city']"
number_field = "xpath,//input[@name='number']"
submit_button = "xpath,//a[contains(text(),'Submit')]"
phone_number_message = "xpath,//p[contains(text(),'Please enter a valid number')]"