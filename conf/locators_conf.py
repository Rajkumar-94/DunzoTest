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
amount_to_pay= "xpath,//div[contains(@class,'bbMAot')]/descendant::font"

# Locators for options in home page
restaurant = "xpath,//p[contains(text(),'Restaurants')]"
alert_message = "xpath,//p[contains(text(),'Please select a location')]"
bangalore_location = "xpath,//a[contains(text(),'Bangalore')]"
bangalore_restaurants = "xpath,//h1[contains(text(),'Restaurants in')]"

# Locators for Partners page
sign_me_up = "xpath,//a[contains(text(),'Sign me up')]"
name_field = "xpath,//input[@name='name']"
city_field = "xpath,//input[@name='city']"
number_field = "xpath,//input[@name='number']"
submit_button = "xpath,//a[contains(text(),'Submit')]"
phone_number_message = "xpath,//p[contains(text(),'Please enter a valid number')]"
redirect_header_logo = "xpath,//header[contains(@class,'app-header')]/descendant::a[contains(@class,'logo')]"
partner_specification = "xpath,//ul[contains(@class,'icon-content-list')]"
partner_feedback = "xpath,//section[contains(@class,'section-testimonials')]"
partner_sign_up_form = "xpath,//section[contains(@class,'section-signup')]"
redirect_footer_div = "xpath,//footer[contains(@class,'app-footer')]"

# Locators for Business page
about_dunzo_business = "xpath,//section[contains(@class,'section-banner')]"
sign_up_button = "xpath,//a[contains(text(),'Sign me up')]"
business_specification = "xpath,//section[contains(@class,'section-specifications')]"
video_feedback_section = "xpath,//section[contains(@class,'section-video-testimonials')]"
business_feedback_section = "xpath,//section[contains(@class,'section-testimonials')]"

# Locators for Home page objects
home_header_logo = "xpath,//img[contains(@class,'iAhUPW')]"
dunzo_partner_button = "xpath,//button[contains(text(),'Dunzo for partners')]"
dunzo_business_button = "xpath,//button[contains(text(),'Dunzo for business')]"
app_link = "xpath,//a[@href='#appLink']"
sign_in = "xpath,//p[contains(@class,'jqmf1i-1') and contains(text(),' Sign in ')]"
location_input = "xpath,//input[@id='autocomplete']"
proceed_button = "xpath,//button[contains(text(),'Proceed')]"
available_locations = "xpath,//div[contains(@class,'twfs7q-5')]"
available_options = "xpath,//div[contains(@class,'p8ys56-2')]"
download_app = "xpath,//p[contains(@class,'fhlEyu') or contains(text(),'Download App')]"
google_play_link = "xpath, //a[@href='https://play.google.com/store/apps/details?id=com.dunzo.user&hl=en']"
apple_store_link = "xpath, //a[@href='https://itunes.apple.com/in/app/dunzoit/id1032391728?mt=8']"
mobile_num = "xpath, //input[@name='number']"
get_app_link_button = "xpath,//button[contains(text(),'Get App Link')]"
become_dunzo_partner_button = "xpath,//button[contains(text(),'Become a Dunzo partner')]"
get_dunzo_business_button = "xpath,//button[contains(text(),'Get your business on Dunzo')]"
dunzo_feedback = "xpath,//div[contains(@class,'hMKJXo')]"
home_footer_division = "xpath,//div[contains(@class,'gsDEQL')]"

