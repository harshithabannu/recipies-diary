# Recipe Manager

## Overview

The Recipe Manager is a command-line application designed to help users manage their recipes. It allows users to add new recipes, view existing recipes, get cooking instructions for a specific recipe, and check which recipes they can make based on the ingredients they have.

## Features

- **Add a Recipe:** Add new recipes to the collection, including ingredients and cooking instructions.
- **View All Recipes:** Display a list of all available recipes.
- **Get Cooking Instructions:** Retrieve cooking instructions for a specific recipe.
- **Check Ingredients and Suggest Recipes:** Input available ingredients and get suggestions for recipes that can be made with those ingredients.
- **Exit:** Close the application.

## How to Run

1. **Save the Script:** Ensure the script is saved as `recipe_manager.py`.

2. **Run the Script:**
    ```sh
    python recipe_manager.py
    ```

3. **Interact with the Application:**
    - Follow the on-screen menu to choose an option.
    - Enter the required details for each operation as prompted.

## Code Explanation

### `display_menu()`

- **Purpose:** Displays the main menu options to the user.
- **Output:** Lists options for adding, viewing, getting instructions, checking ingredients, or exiting.

### `add_recipe(recipes)`

- **Parameters:**
  - `recipes` (dict): Dictionary holding recipe details.
- **Functionality:** 
  - Adds a new recipe if it doesn’t already exist.
  - Prompts the user for the recipe name, ingredients, and cooking instructions.
  
### `view_recipes(recipes)`

- **Parameters:**
  - `recipes` (dict): Dictionary holding recipe details.
- **Functionality:** 
  - Lists all available recipes.
  - Displays a message if no recipes are available.

### `get_instructions(recipes)`

- **Parameters:**
  - `recipes` (dict): Dictionary holding recipe details.
- **Functionality:** 
  - Retrieves and displays ingredients and cooking instructions for a specified recipe.
  - Shows an error message if the recipe is not found.

### `check_ingredients(recipes)`

- **Parameters:**
  - `recipes` (dict): Dictionary holding recipe details.
- **Functionality:** 
  - Takes a list of available ingredients and suggests recipes that can be made with those ingredients.

### `main()`

- **Purpose:** 
  - Manages the user interface and application flow.
  - Provides options to add, view, get instructions, or check recipes.
  - Continues to prompt for user input until the exit option is chosen.

## Example

**Run the application:**

```sh
python recipe_manager.py

**Sample Interaction:**
Recipe Manager
1. Add a Recipe
2. View All Recipes
3. Get Cooking Instructions
4. Check Ingredients and Suggest Recipes
5. Exit

Choose an option: 1
Enter the name of the recipe: Pancakes
Enter the ingredients (separated by commas): flour, eggs, milk
Enter the cooking instructions: Mix all ingredients and cook on a skillet.

Recipe 'pancakes' added successfully!

...

Choose an option: 3
Enter the name of the recipe you want to cook: pancakes

Ingredients for Pancakes:
- flour
- eggs
- milk

Instructions:
Mix all ingredients and cook on a skillet.

...

Choose an option: 5
Exiting the Recipe Manager. Goodbye!

#Additional Information
Menu Customization: You can modify the display_menu() function to change the menu options or add new features.
Recipe Storage: Recipes are stored in-memory during the runtime of the application. To persist recipes, consider implementing file or database storage.

##License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Thanks to Python documentation and the programming community for resources and support.
