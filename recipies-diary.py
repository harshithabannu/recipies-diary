def display_menu():
    print("\nRecipe Manager")
    print("1. Add a Recipe")
    print("2. View All Recipes")
    print("3. Get Cooking Instructions")
    print("4. Check Ingredients and Suggest Recipes")
    print("5. Exit")

def add_recipe(recipes):
    name = input("\nEnter the name of the recipe: ").strip().lower()
    if name in recipes:
        print(f"Recipe '{name}' already exists. Please choose a different name.")
        return
    ingredients = input("Enter the ingredients (separated by commas): ").split(',')
    ingredients = [ingredient.strip().lower() for ingredient in ingredients]
    instructions = input("Enter the cooking instructions: ")
    
    recipes[name] = {
        "ingredients": ingredients,
        "instructions": instructions
    }
    print(f"Recipe '{name}' added successfully!")

def view_recipes(recipes):
    if not recipes:
        print("\nNo recipes available.")
        return
    
    print("\nAvailable Recipes:")
    for recipe_name in recipes.keys():
        print(f"- {recipe_name.capitalize()}")

def get_instructions(recipes):
    name = input("\nEnter the name of the recipe you want to cook: ").strip().lower()
    recipe = recipes.get(name)
    
    if not recipe:
        print(f"Recipe '{name}' not found.")
        return
    
    print(f"\nIngredients for {name.capitalize()}:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient}")
    
    print("\nInstructions:")
    print(recipe["instructions"])

def check_ingredients(recipes):
    available_ingredients = input("\nEnter the ingredients you have (separated by commas): ").split(',')
    available_ingredients = [ingredient.strip().lower() for ingredient in available_ingredients]

    print("\nRecipes you can make:")
    for recipe_name, recipe_details in recipes.items():
        if all(ingredient in available_ingredients for ingredient in recipe_details["ingredients"]):
            print(f"- {recipe_name.capitalize()}")

def main():
    recipes = {}
    
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            add_recipe(recipes)
        elif choice == '2':
            view_recipes(recipes)
        elif choice == '3':
            get_instructions(recipes)
        elif choice == '4':
            check_ingredients(recipes)
        elif choice == '5':
            print("Exiting the Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()