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

HTML validation was carried out on Chrome by viewing the page source in a hope to limit the errors due to Jinja templating. The fikes were passed through [W3C](https://validator.w3.org/)

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

### Manual Testing

| Action | Expected | Result |
| --- | --- | --- |
| As a **user** I want to see a homepage so I can see what the website is about and view categories. | When the user navigates to the home page they can see the Genre and Platform categories, | Works as expected. | |
| As a **user** I want to see a header so I navigate to where I want to go.  | When I navigate to the website I will see the home page. Then I will see a header with a business logo, a search bar, a user icon and a shopping bag icon.  | Works as expected. | |
| As a **user** I want to see a favicon so I can identify the website I am on.| The user can see a favicon when they visit the website | Works as expected. | |
| As a **user** I want to sign out of my account when I am logged in. | When I am signed into my account and I am finished browsing. Then I will click on the profile icon and will have the option to sign out  | Works as expected. | |
| As a **user** I want to see a message to confirm my action.| When I have completed an action on the website. Then I will see a message validating the action I have taken | Works as expected. | |
| As a **staff member** I want to be able to add products through the website. | As a **staff member** I want to be able to add products through the website. Then I will be able to access the product management area where I can add a product for sale.  | Works as expected. | |
| As a **staff member** I want to be able to delete products through the website. | When I navigate to the website and sign in with my staff username/password. Then I will be able to access the product management area where I can delete an existing product.  | Works as expected. | |
| As a **staff member** I want to be able to edit products through the website. | When I navigate to the website and sign in with my staff username/password. Then I will be able to access the product management area where I can edit an existing product | Works as expected. | |
| As a **user** I want to see products on the website that I can browse and purchase. | When I navigate to the website. Then I will see products to browse/purchase | Works as expected. | |
| As a **user** I want to sign up to receive a newsletter. | When I navigate to the website footer. Then I will see the option to enter my email address to subscribe to the newsletter | Works as expected. | |
| User hovers the cursor over the product card | The product card gets overlay with a semi-transparent layer and "Click for more" button appears. | Works as expected. | |
| As a **user** I want to sign in or sign up depending on my account status. | When I navigate to the website and I don't already have an account. Then I will use the register option to sign up for an account | Works as expected. | |
| As a **user** I want to see a homepage so I can see what the website is about and view categories. | When I navigate to the website I will see the home page. Then I will see the home page with a logo, categories, sign in options, header, footer, a hero image and site information text| Works as expected. | |
| As a **user** I want to see a footer containing useful information about the website. | When I navigate to the website I will see the home page. Then I will see a footer containing a privacy policy, contact us, delivery information hyperlinks and social media hyperlinks.  | Works as expected. | |
| As a **user** I want to see a 404 page when I have come across a page that is not found. | When I try to access an incorrect URL. Then I will see a message telling me the page is not available | Works as expected. | |
| As a **user** I want to see a form where I can submit a review.| The product card gets overlay with a semi-transparent layer and "Click for more" button appears. | Works as expected. | |
| As a **user** I want to see a form where I can submit a review.| When I navigate to the website I will see the home page. Then I will see an option for reviews | Works as expected. | |
| As a **user** I want to see a form where I can contact the site owner so that I can sell my own collectables. | When I navigate to the website I will see the home page, then I will see an option under the my account tab to sell a collectable. When I click on sell collectable, Then I will be redirected to a page with a form where I can fill out details about the collectable I want to sell.   | Works as expected. | |
| As a **user** when I click on a product I want to see further details of that product. | When I click on a product, then I am brought to a new page with the single product displayed. | Works as expected. | |
| As a **user** I want to purchase an item using Stripe. | When I add an item to my cart. Then I will be able to purchase the item using Stripe. | Works as expected. | |


## Bugs

### Known Bugs

* When an item is beeing removed from the cart the toast is no longer displaying, it was working at one point and then disappeared, i think around the time I added the 'sold ot' functionality. I ran out of time to imvestigate but will look at it in the future.

### Bugs encountered along the way 

* Big issues with Stripe webhooks, on one occasion it was because I didn't have my gitpod space set to public. The I had a typo in the secret key at another point.



