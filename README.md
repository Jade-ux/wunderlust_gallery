# Wunderlust Fine Art Gallery

[View live site](https://wunderlust.herokuapp.com/)

## Index

- <a href="#overview">Project Overview</a>
- [User stories](static/wireframes_mockups/wunderlust-user-stories.pdf)
- [Wireframes](static/wireframes_mockups/wunderlust-wireframes.pdf)
- <a href="#database">Database design</a>
- <a href="#features">Features</a>
- <a href="#technologies">Technologies used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>
- <a href="#contents">Contents</a>
- <a href="#media">Media</a>
- <a href="#acknowledgements">Acknowledgements</a>

<hr>


<span id="overview"></span>

## Overview

Wunderlust is an online fine art gallery which exhibits and sells art from around the World. Our gallery showcases art from well-established and traditional artists as well as emerging artists breaking through the norms of the art world.

Users may be looking for an artwork to remind them of a place they once visited,they may want to buy a piece from an artist they admire or could simply be looking for an item that will bring them joy. 

As a user I want to be able to browse art by artist, category, country and price, in order to select items to purchase. I want to be able to see details about each artwork I am interested in and be able to add items to my shopping cart, customise my purchases and check out. 

I want to be able to sign up for an account, manage my account and sign up for events.

Artists will exhibit their art exclusively at Wunderlust for a number of months. As an artists I want to be able to 'consign work in' by uploading the image to the site, and 'consign work out' by removing the item after the exhibition/display term.

As an artist I want to be able to edit items I have on the site and manage my own artist biography on the site.

As a site owner I want to attract potential buyers to the website and allow them to easily browse through all the work available. I want to be able to sell artwork through the website and therefore receive a commission on any sales. I also want to encourage site users to sign up for an account so that I can easily market our artworks to them.

I want to allow artists to sign up for accounts so that they can manage their artwork and information, but I want to be able to approve the changes they make.

---

<span id="ux"></span>

## UX

*Shopping cart terminology*

When choosing between the words 'bag', 'basket' and 'cart' I thought about the mental model the shoppers would build when shopping for art. It is likely you would imagine putting large artworks into a cart rather than a basket or a bag. I looked up use cases for the terminology and also found that the word 'cart' is easier to localize as it translates well into other languages. One good resource is the article: [Shopping cart, bag or basket](https://uxdesign.cc/shopping-cart-bag-or-basket-fd7360c9413a). Therefore I have gone with 'cart'. I have used an 'Open Cart' icon as I think the flair fits in well with this website's products. Once the user begins adding items to their cart a total will appear which will make the purpose of the icon obvious.
 
[See my user stories here](static/wireframes_mockups/wunderlust-user-stories.pdf)

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

<span id="userstories"></span>

## User Stories 

[See my user stories here](static/wireframes_mockups/wunderlust-user-stories.pdf)


<span id="wireframes"></span>

## Wireframes

[See my user stories here](static/wireframes_mockups/wunderlust-wireframes.pdf)

<span id="features"></span>

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

- Create an account: users can create an account, signing up with their email address.
- Add artwork to cart - users can add artworks they wish to purchase to their cart.
- View cart - users can view their shopping cart and all the items in it before proceeding to checkout.
- Checkout - users can pay for their items and the site will process their order and take payment via Stripe.
- View profile - users can view their profile and update their shipping details or see their order history.
- Filter artwork - users can filter artwork by Artist, Country, Category or Price.
- Search - users can search the site for art that contains their search query in the name or description of the artwork.
- Featured collection - users can view the artwork currently featured in the store.
- Admin - admin users can log into the admin portal to manage artwork, artists, categories, countries, orders and users.


### Features Left to Implement
- Framing options

<span id="technologies"></span>

## Technologies Used

- [Django](https://docs.djangoproject.com/en/3.2/)
    - This website is built on the Django framework, and is currently running version 3.1.7.
- [HTML](https://en.wikipedia.org/wiki/HTML) - the front-end structure of this app is written in HTML
- [CSS](https://en.wikipedia.org/wiki/CSS) - this app is styled with CSS
- [JavaScript](https://www.javascript.com/) - used for DOM manipulation
- [JQuery](https://jquery.com) - used to simplify DOM manipulation
- [Python](https://www.python.org/) - the app functionality and data manipulation is written in Python.
    - The project uses **JQuery** to simplify DOM manipulation.
- [Pip3](https://pypi.org/project/pip/) - used to install Python packages
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - used to provide all account functionality including the ability to register for an account, verify, log in and out and reset a forgotten password.
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - used to speed up responsive design
- [Stripe](https://stripe.com/) - is used as the payment system for the store
- [Balsamiq](https://balsamiq.com/) - wireframes for this app were created with the Balsamiq wireframing tool.
- [Amazon S3](https://docs.aws.amazon.com/s3/index.html?nc2=h_ql_doc_s3) - this project uses Amazon S3 to store images uploaded by users 
- [Heroku](https://dashboard.heroku.com/apps) - is the cloud platform used to host the deployed app.

<span id="testing"></span>

## Testing

## Technologies used for testing:

- [W3C Markup Validation Service](https://validator.w3.org/) - used to validate HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - used to test CSS code validation
- [JSHint](https://jshint.com/) - used to test for JavaScript code validity
- [Lighthouse](https://developers.google.com/web/tools/lighthouse_) - used for testing front-end best practice
- [Pep8 checker](http://pep8online.com/) - used for testing Python code against Pep8 guidelines


### Pep 8 testing

- Fixed - in the Artworks view Pep8 picked up an error on the Lower() function from Django, with the error mesage: 'undefined name 'Lower''. Looking this up in the [Django documentation](https://docs.djangoproject.com/en/3.1/ref/models/database-functions/) I could see I needed to import Lower.
- Bug - in the Artworks view Pep8 picks up an error on all the models, giving an error message that 'Class Country/Category/Artist has no objects member'. Research on [Stack Overflow](https://stackoverflow.com/questions/45135263/class-has-no-objects-member) and [Reddit](https://www.reddit.com/r/django/comments/6nq0bq/class_question_has_no_objects_member/) confirms that this is not really an error as Django adds that property dynamically to all Models but the IDE is not able to see this.

### Testing user stories


|**User story**|**Expected outcome**|**Actual outcome**|
|:-----|:-----|:-----|
|**As a user I want to:**|||
|Browse all artwork | I expect to easily be able to navigate to a page that will show all the artwork| I find the 'All artwork' link on the navigation bar which is clear and clicking that reveals a drop-down. From there I can select 'All art' to view all.|
|Filter artwork by certain criteria | I expect to easily filter artwork by artist, category or country| I find the filters along the top navigation which allow me to easily choose the filter I want. When I click on one of the choices I am taken to a page that shows only the art relevant to the category I chose.|
|Add items to my cart | I expect to be able to add items that I wish to purchase to my cart. | I find a button on the 'artwork detail' page that allows me to add an item to my cart. |
|View cart| I expect to be able to view my cart and see all items and a total for my purchase before I checkout.| Navigating to the cart via the cart icon on the nav bar I can see all the items in the cart before I checkout.|
| Check out | I want to be able to pay for my items and have my order processed. | When I click 'Secure checkout' the order is processed and I receive a confirmation message that my order has been processed. |


<span id="database"></span>

## Database design

I took time to plan out my database in Excel. I created all database tables in csv files and then converted those to json to allow me to add my fixtures.

[See my database diagram here](static/wireframes_mockups/db_visual.PNG)

<span id="deployment"></span>

## Deployment

**Differences between development site and deployed site:**

There are no differences between the development site and deployed site. The development site is deployed on the Master branch and I have tested the deployed site to ensure it looks the same and functions in the same way as the development site.

**If you would like to run my code locally you can clone the site by following these steps:**

1. Visit the main page of my repository on [GitHub here](https://github.com/Jade-ux/wunderlust_gallery).
2. Click 'Clone or download'
3. Click the icon to the right of the URL. This will allow you to clone the repository using HTTPS.
4. If you would like to clone it using SSH, click 'Use SSH'
5. On your computer open Git Bash
6. Change the directory to the folder where you would like to run the cloned directory
7. Type 'Git clone' and then paste the URL you copied from my repository in GitHub
8. Press enter and your local clone of my site will be created.
9. Install each of the requirements from the requirements.txt file or run the following code:

                pip -r requirements.txt

12. Run the initial migrations with:
                
                python3 manage.py migrate

13. Load the data from the JSON files in this order and with this code:
                
                python3 manage.py loaddata categories
                python3 manage.py loaddata countries
                python3 manage.py loaddata artists
                python3 manage.py loaddata artworks

14. To create a superuser you can use in development type the command:

                python3 manage.py createsuperuser
    
    Follow the prompts to set up your superuser.
15. To view the live preview of the site in development, use the command:
                python3 manage.py runserver

16. Set up your Amazon AWS account <a href="#amazonaws">following the steps above</a>.
17. You will then need to create your own app on Heroku, <a href="#heroku">steps for Heroku</a> below.

**Setting up your Amazon S3 account to host uploads**

<span id="amazonaws"></span>

I used Amazon S3 to host images and fixtures. These are the steps I took and the steps you can take when cloning my site:

1. Create an Amazon AWS account
2. Create a bucket within your account
3. Attach a CORS policy
4. Attach a bucket policy
5. In IAM create a new user group
6. Attach an S3 bucket policy to your user group and set the permissions to only allow access to your project bucket
7. Create a new user and add to the group you created before
8. Download the access key file and keep it safe, you will not be able to download it again. 
9. Add the settings to your IDE

**In Heroku**

<span id="heroku"></span>

1. In Heroku create a new app and add your config vars (in the 'settings' tab > click 'Reveal config vars')

|**Key**|**Value**|
|:-----|:-----|
|SECRET_KEY| `<your secret key>`|
|DATABASE_URL|`<your postgres database URL found in Heroku>`|
|STRIPE_PUBLIC_KEY| `<your Stripe public key>`
|STRIPE_SECRET_KEY|`<your Stripe public key, do not reveal in repo>`|
|STRIPE_WH_SECRET|`<your Stripe Webhook secret>`|
|USE_AWS| True |
|AWS_ACCESS_KEY_ID|`<your Amazon Key ID downloaded from Amazon IAM>`|
|AWS_SECRET_ACCESS_KEY|`<your Amazon Secret Key downloaded from Amazon IAM>`|
|EMAIL_HOST_PASS|`<your email account's host password>`|
|EMAIL_HOST_USER|`<your email address that will be used to send email>`|

2. Connect your app to your Github repository and then enable automatic deploys.

<div class="right"><a href="#index"><button class="btn-small">Back to index &#8593;</button></a></div>

<span id="bugs"></span>

## Bug fixes

- 404 page: I followed the [Django documentation](https://docs.djangoproject.com/en/3.2/ref/exceptions/) for guidance on setting up the 404 page. The site now has a '404 - Page not found' error page which is displayed when a user tries to navigate to a page that does not exist on the website.
- 500 error page: I followed the [Django documentation](https://docs.djangoproject.com/en/3.2/ref/exceptions/) for help on setting up the 500 error handling. The site now displays a 500 error page if there is a server error.

<span id="credits"></span>

## Credits

### Code

I included code from the [Code Institute Boutique Ado project](https://github.com/ckz8780/boutique_ado_v1) as a guide for many of the pages and where I have utilised full blocks of code from the project I have attributed it inline.

<span id="contents"></span>

### Content
- The Boutique Ado project provided me with a lot of inspiration for this project. I used many of the lessons from that project to help me when planning out and building my own project and then added to it to make this site unique and fit for it's purpose.

**Text for descriptions of artworks:**

- Andy Warhol: [The Tate Modern's website](https://www.tate.org.uk/art/artworks/warhol-muhammad-ali-by-andy-warhol-ar00394#:~:text=Warhol%20photographed%20the%20boxer%2C%20Muhammad,of%20his%20'Athletes'%20series.&text=In%20the%20screenprint%20reproduced%20here,concentration%20required%20during%20a%20fight.) and [Princeton University Art Museum](https://artmuseum.princeton.edu/collections/objects/)
- Gustav Klimt: [Google Arts](https://artsandculture.google.com/asset/nine-cartoons-for-the-execution-of-a-frieze-for-the-dining-room-of-stoclet-house-in-brussels-part-8-fulfillment-lovers-gustav-klimt/sQFM1ks6C1Lujg?hl=en)
- Leonardo da Vinci: [Wikipedia - The Vitruvian Man](https://en.wikipedia.org/wiki/Vitruvian_Man) and [Wikipedia - The Last Supper](https://en.wikipedia.org/wiki/The_Last_Supper_(Leonardo))
- Paul Cezanne [Wikipedia - Paul Cezanne](https://en.wikipedia.org/wiki/Paul_C%C3%A9zanne) 
- Wassily Kandinsky [Wassily Kandinsky](https://www.wassilykandinsky.net/work-50.php) 

<span id="media"></span>

### Media

- All artwork images are from [the Kaggle collection here](https://www.kaggle.com/ikarus777/best-artworks-of-all-time?select=artists.csv)

Artist self-portraits:

- Andy Warhol's self-portrait is from [the Kaggle collection here](https://www.kaggle.com/ikarus777/best-artworks-of-all-time?select=artists.csv)
- Caravaggio's self portrait is from [the Kaggle collection here](https://www.kaggle.com/ikarus777/best-artworks-of-all-time?select=artists.csv)
- Paul Cezanne's portrait is from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Paul_C%C3%A9zanne_-_Self-Portrait_-_Google_Art_Project.jpg)
- Vincent van Gogh's portrait is from [Wikimedia commons](https://commons.wikimedia.org/wiki/Self-portrait_paintings_by_Vincent_van_Gogh)
- Wassily Kandinsky's portrait is from [Wikimedia commons](https://www.google.com/url?sa=i&url=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FWassily_Kandinsky&psig=AOvVaw3NiSxIgWiShBiDnKNn57iR&ust=1618174605016000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCJii9qXI9O8CFQAAAAAdAAAAABAG)
- Gustav Klimt's portrait is from Wassily Kandinsky's portrait is from [Wikimedia commons](https://)
- Leonardo da Vinci's self-portrait is from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Leonardo_self.jpg)

-The image placeholder is from [Wikimedia commons](https://commons.wikimedia.org/wiki/File:Placeholder_view_vector.svg)


<span id="media"></span>

### Acknowledgements

- Thank to you my mentor for guiding me.