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
popup_close= "xpath,//i[contains(@class,'sc-3wfzb0-0 sc-13gg6g2-2 cSxoYv')]"
create_task = "xpath,//button[contains(text(),'Create a Task')]"

# Locators to set pick up address
pick_up_click= "xpath,//p[contains(text(),'Search pickup location')]"
partial_address = "xpath,//input[@id='places-autocomplete']"
area_location = "xpath,//div[@class='sc-bdVaJa sc-bwzfXH eejohd-0 ccewWU']"
flat_number = "xpath,//input[@name='apartmentAddress']"
pick_adress_continue_button= "xpath,//button[contains(text(),'Continue')]"

# Locators to set drop address
drop_click = "xpath,//p[contains(text(),'Search drop location')]"
partial_drop_address = "//xpath,input[@id='places-autocomplete']"
drop_area_location = "xpath,//div[@class='sc-bdVaJa sc-bwzfXH eejohd-0 ccewWU']"
drop_flat_number = "xpath,//input[@name='apartmentAddress']"
drop_adress_continue_button= "xpath,//button[contains(text(),'Continue')]"

# Locator to fetch the expected shipping amount
amount_to_pay= "xpath,//div[contains(@class,'sc-bdVaJa sc-bwzfXH bbMAot')]/div/p/font"

# Locators for options in home page
restaurant = "xpath,//p[contains(text(),'Restaurants')]"
alert_message = "xpath,//p[contains(text(),'Please select a location before proceeding.')]"
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