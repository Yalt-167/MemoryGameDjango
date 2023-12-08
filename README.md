# MemoryGameDjango

architecture summary:
- the urls.py is used to link files together
- the views.py is used to create views; views being functions that define how a site should be rendered based on a template -> .html files that hold logic for further customization (by providing a .json to the template and including django logic using {% stmt %})
- the models.py is used to create models aka the table template that django uses
- the admin.py allows us to register tables (or model) in the admin panel, enabling the admin to edit them manually
- the folder templates holds the templates of the website's pages (template being blueprint that can hold logic written in python using the django syntaxe)