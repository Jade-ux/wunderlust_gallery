# Wunderlust Fine Art Gallery

## Index

- <a href="#overview">Project Overview</a>
- [User stories](static/wireframes_mockups/wunderlust-user-stories.pdf)
- [Wireframes](static/wireframes_mockups/wunderlust-wireframes.pdf)
...
---

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

[See my user stories here](static/wireframes_mockups/wunderlust-user-stories.pdf)

[See my wireframes here](static/wireframes_mockups/wunderlust-wireframes.pdf)

This is the end of my README currently. 

---


[See my user stories here](static/wireframes_mockups/wunderlust-user-stories.pdf)




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


|**Nr**|**As a/an**|**I want to be able to**|**So that I can**|
|:-----|:-----|:-----|:-----|
|1|Shopper|See what is on exhibition currently.|Decide if I want to attend, read up about the artist(s), find out about artwork.|

<span id="wireframes"></span>

## Wireframes

[See my user stories here](static/wireframes_mockups/wunderlust-wireframes.pdf)


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Pip3](https://pypi.org/project/pip/) - used to install Python packages
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - used to provide all account functionality including the ability to register for an account, verify, log in and out and reset a forgotten password.
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - used to speed up responsive design


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

### Pep 8 testing

- Fixed - in the Artworks view Pep8 picked up an error on the Lower() function from Django, with the error mesage: 'undefined name 'Lower''. Looking this up in the [Django documentation](https://docs.djangoproject.com/en/3.1/ref/models/database-functions/) I could see I needed to import Lower.
- Bug - in the Artworks view Pep8 picks up an error on all the models, giving an error message that 'Class Country/Category/Artist has no objects member'. Research on [Stack Overflow](https://stackoverflow.com/questions/45135263/class-has-no-objects-member) and [Reddit](https://www.reddit.com/r/django/comments/6nq0bq/class_question_has_no_objects_member/) confirms that this is not really an error as Django adds that property dynamically to all Models but the IDE is not able to see this.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The Boutique Ado project provided me with a lot of inspiration for this project. I used many of the lessons from that project to help me when planning out and building my own project and then added to it to make this site unique and fit for it's purpose.
Text for descriptions of artworks
- Andy Warhol: [The Tate Modern's website](https://www.tate.org.uk/art/artworks/warhol-muhammad-ali-by-andy-warhol-ar00394#:~:text=Warhol%20photographed%20the%20boxer%2C%20Muhammad,of%20his%20'Athletes'%20series.&text=In%20the%20screenprint%20reproduced%20here,concentration%20required%20during%20a%20fight.) and [Princeton University Art Museum](https://artmuseum.princeton.edu/collections/objects/)
- Gustav Klimt: [Google Arts](https://artsandculture.google.com/asset/nine-cartoons-for-the-execution-of-a-frieze-for-the-dining-room-of-stoclet-house-in-brussels-part-8-fulfillment-lovers-gustav-klimt/sQFM1ks6C1Lujg?hl=en)
- Leonardo da Vinci: [Wikipedia - The Vitruvian Man](https://en.wikipedia.org/wiki/Vitruvian_Man) and [Wikipedia - The Last Supper](https://en.wikipedia.org/wiki/The_Last_Supper_(Leonardo))
- Paul Cezanne [Wikipedia - Paul Cezanne](https://en.wikipedia.org/wiki/Paul_C%C3%A9zanne) 
- Wassily Kandinsky [Wassily Kandinsky](https://www.wassilykandinsky.net/work-50.php) 


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

### Acknowledgements

- I received inspiration for this project from X