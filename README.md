# Smart Prep
## Ahead of your weekly shopping list

Developed by Nathalie von Heyl

[Placeholder: I am responsive]

[Placeholder: Live website]

## About

Smart Prep - 4th Portfolio Project for the Diploma in Full Stack Software Development with Code Institute. It is a full-stack website built with Django to help users stay on top of their weekly grovery list. A personal staples list allows to keep track of the user's all-time-staples and the personal shopping list allows the user to select which of those staples have to be on this weeks grocery shopping list. 

## Project Goals 

### User Goals

TBD
(linked to user stories)

### Business Site Owner Goals

TBD
(linked to user stories)

## User Experience 

### Target Audience

- People who would like to reduce costs of living by avoiding buying groceries in excess
- Users who would like shop more efficiently and less often (having an organised shopping list with staples to select from makes sure people can go grocery shopping once a week and therefore save time)
- People who like to plan their grocery shopping to easier buy what is needed

### User Requirements and Expectations

- Accessible and responsive website
- Intuitive website with a layout allowing to easily navigate through it
- Easy access to Create, Read, Update & Delete (CRUD) functionalities
- Links and features that function in accordance with their intended purpose
- A contact form to contact the website owner

### User Stories

#### Epic: Homepage / Landing page

As a visitor, I can ...  
- ... initially see the home page that introduces the idea of Smart Prep so that I can understand its purpose and benefits. 
- ... see a clear call to action to register/log in so that I am encouraged to create an account to access personalized features.

As a user, I can ... 
- ... see my login state reflected in the homepage UI so that I can confirm whether I am logged in or logged out.

#### Epic: User / Authentication

As a user, I can ...

- ... register an account so that I can access personalized features like creating and managing staple list items.
- ... log in to my account so that I can access my personal staples list.
- ... log out of my account so that I can ensure my personal data remains private.

As a superuser, I can ... 
- ... verify registered users in the admin panel so that I can ensure only legitimate accounts are accessing the website and using its features.

#### Epic: Personal Staples

As a superuser, I can ... 

- ... access the admin panel so that I can check the staples model is working and staple items can be added or modified.

As a user, I can ... 

- ... add individual staple items so that I can track my frequently purchased items and favorites.
- ... view my personal staples list so that I can see all the items I’ve added in one place.
- ... edit my own staple items so that I can update details like name, quantity, measurement unit, or category when needed.
- ... delete staple items from my own list so that I can keep my list of staples up to date.

## Features

### MVP: Must-have features

- User Authentication:
  - Users can create accounts, log in and log out
  - Users have access to interactive features on the site only when logged it (interactive feature: CRUD staple items in a personal staples list)
  - Features like the personal staples with functionality of adding and editing items are not accessible to visitors
  - Login state must be reflected in the UI of homepage
- Personal Staples (CRUD)
  - Users can create, read, update and delete individual staple items
  - These staple items are stored in a persistent personal list of staples (personal meaning each user sees their own list of staples) that is editable by the user

### Should-have features

- Shopping List
  - With login each user has access to their personal shopping list
  - Users can add items from the Personal Staples to the Shopping List
- Recipe Blog
  - The website contains a Recipe Blog
  - A superuser can create, edit, and delete Recipes on the blog
  - The recipes are displayed to the user: Each recipe has a specified list of grocery items per serving

### Could-Have features

- Each recipe has predefined grocery items (ingredients) with specified quantities per serving
  - Users can select a recipe and the number of servings
  - Grocery items for selected recipes in the quantity defined by selected servings is added to the shopping list
- Recipe Request Form
  - Users can suggest new recipes or provide feedback to the admin via a form
- Categorized Shopping List
  - Group grocery items into categories (e.g., produce, dairy, grains) in the shopping list
- Bulk action: Deselect all recipes/delete all items on the shopping list

### Won’t-Have features

- For now: one-to-one relationship between a user and their shopping list. Future feature: Shared Shopping Lists! (refactor the model for a many-to-many relationship model for multiple users being linked to one shopping list)
- User profile page apart from shopping list
- Comments and likes for recipes
- Portion size options for recipes (small, regular, large)
- Customizable weekly meal plans (drag-and-drop recipe servings)

## Data

### ERD for models

<details>
<summary>Staple Items Model</summary>

![Model StapleItems](docs/wireframes/erd_model_1.png)

</details>

## Agile Methodologies

Github Project + Link

User Stories + Link to Issues

## Design 

### Wireframes 

<details>
<summary>Homepage Wireframes</summary>

<details>
<summary>Desktop Home page</summary>

![Desktop Home page](docs/wireframes/Home%20Desktop.png)

</details>

<details>
<summary>Tablet Home page</summary>

![Tablet Home page](docs/wireframes/Home%20Tablet.png)

</details>

<details>
<summary>Mobile Home page</summary>

![Mobile Home page](docs/wireframes/Home%20Mobile.png)

</details>

<details>
<summary>Mobile Home page with Dropdown Menu</summary>

![Mobile Home page dropdown](docs/wireframes/Home%20Mobile%20Dropdown.png)

</details>

</details>
