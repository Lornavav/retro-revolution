# Testing
## Code Validation
### CSS Validation

CSS files were passed through jigsaw [Jigsaw](https://jigsaw.w3.org/css-validator/) there were no issues.

|Page  |Image  |
|--|--|
|Base.css  |![Base](/documentation/images/base_css.png)|
|Checkout.css  |![checkout](/documentation/images/checkout_css.png)|
|Profile.css  |![Profile](/documentation/images/profile_css.png)|

### Python Validation

Python files were passed through the Code Institute [PEP8](https://pep8ci.herokuapp.com/) validator. All issues were cleared.

| Page |Image  |
|--|--|
| Bag Contexts |![PEP8](/documentation/images/bag_contexts.py.png)|
| Bag Urls|![PEP8](/documentation/images/bag_urls.py.png)|
| Bag Views |![PEP8](/documentation/images/bag_views.py.png)|
| Checkout Admin |![PEP8](/documentation/images/checkout_admin.py.png)|
| Checkout Forms |![PEP8](/documentation/images/checkout_forms.py.png)|
| Checkout Models|![PEP8](/documentation/images/checkout_models.py.png)|
| Checkout Models|![PEP8](/documentation/images/checkout_signals.py.png)|
| Checkout Urls |![PEP8](/documentation/images/checkout_urls.py.png)|
| Checkout Views |![PEP8](/documentation/images/bag_contexts.py.png)|
| Checkout Webhook Handler |![PEP8](/documentation/images/checkout_webhook_handler.py.png)|
| Checkout Webhooks |![PEP8](/documentation/images/checkout_webhooks.py.png)|
| Home Urls |![PEP8](/documentation/images/home_urls.py.png|)
| Home Views |![PEP8](/documentation/images/home_views.py.png|)
| Products Admin |![PEP8](/documentation/images/products_admin.py.png)|
| Products Forms |![PEP8](/documentation/images/products_forms.py.png)|
| Products Models |![PEP8](/documentation/images/products_models.py.png)|
| Product Urls |![PEP8](/documentation/images/products_urls.py.png)|
| Products Views |![PEP8](/documentation/images/views)|

### JavaScript Validation

JS files were passed through JSHint [JSHint](https://jshint.com/) validator. No major issues were reported.

| Page |Image  |
|--|--|
| Profiles countryfield.js|![JSHint](/documentation/images/profiles_countryfield_js_validator.png)|
| Checkout stripe elements |![JSHint](/documentation/images/checkout_stripe_elements_validator.png)|

### Lighthouse Testing

Lighthouse testing was carried out on the site using Chrome developer tools. There are a few improvements needed, mainly around images and some colour contrasting.

| Page |Image  |
|--|--|
| Bag with items|![Lighthouse](/documentation/images/bag_with_items_lighthouse.png)|
| Empty shopping bag|![Lighthouse](/documentation/images/empty_shopping_bag_lighthouse.png)
| Index Page |![Lighthouse](/documentation/images/index_page_lighthouse.png)|
| My Profile|![Lighthouse](/documentation/images/my_profile_lighthouse.png)|
| Reviews |![Lighthouse](/documentation/images/reviews_lighthouse.png)|
| Sell a Collectable |![Lighthouse](/documentation/images/sell_a_collectable_lighthouse.png)|
| Sign In |![Lighthouse](/documentation/images/sign_in_lighthouse.png)|
| Sign Up |![Lighthouse](/documentation/images/sign_up_lighthouse.png)|

### HTML Validation

HTML validation was carried out on Chrome by viewing the page source in a hope to limit the errors due to Jinja templating. The fikes were passed through W3C ![W3C](https://validator.w3.org/)

I tested the follow pages:

* profile
* reviews
* sell_collectable
* edit_collectable
* collectable_detail
* index_page
* bag
* add_collectable
* collecatbles

The same error and warning were appearing for most around aria labels and table headers. I tried fixing the aria label but i kept getting errors and needed to move on, this is something I will need to become more familiar with.

| Issue |Image  |
|--|--|
| Aria Label |![HTML](/documentation/images/profile_html_validator.png)|
| Href Issue - templating |![HTML](/documentation/images/sell_a_collectable_html_validator.png)|
| Table Issue |![HTML](/documentation/images/bag_html_validator.png)|

### Responsive Design

Responsive design testing was carried out on the Chrome dev tools responsive decviese. No major issues were returned although user experience coulde defintely improve for mobile with more thought and time put into it. 



