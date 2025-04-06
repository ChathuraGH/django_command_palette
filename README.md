# django_command_palette
Command palette to the Django Admin Interface





![a](https://github.com/ChathuraGH/django_command_palette/blob/f701b9b43c882587fdb2ae52e796e38399cd7596/feature_previews/logo.svg)

![c](https://github.com/ChathuraGH/django_command_palette/blob/f701b9b43c882587fdb2ae52e796e38399cd7596/feature_previews/685unxpkksrvfugu-360.png)

[//]: # (https://github.com/ChathuraGH/django_command_palette/blob/f701b9b43c882587fdb2ae52e796e38399cd7596/feature_previews/unnamed.png)




![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)




![Command palette to the Django Admin Interface.](https://github.com/ChathuraGH/django_command_palette/blob/e3da3b468d715f6ac2314c72191de934f708713e/feature_previews/command_palette-4.png)




# django_command_palette

# Version : test version 1

- User name : admin
- Password : admin

# Environment

  - Django version 3.0.8


# how to 
- run the server
- go to index page or `/admin`
- press `Ctrl + k` or press the `#` button



# Available Key Combos 



- Complexity : Level of command complexity("normal" or "complex" )

    - Normal  :-  Function on combo
    - Complex  :-  Function on `Enter`
  
- Availability : Command trigger location("specific page" or "global") 


#### Palette manage
| Shortcut Function                | Key Combo                        |   Complexity-Availability            |   Execution method    |
|----------------------------------|----------------------------------|--------------------------------------|-----------------------|
| Open the command palette modal   | `Ctrl+K`                         |   Normal-Global                      |   On Combo            |
| Close the command palette modal  | `Esc`                            |   Normal-Global                      |   On Combo            |
| Go up in command list            | `Up arrow`                       |   Normal-Global                      |   On Combo            |
| Go down in command list          | `Down arrow`                     |   Normal-Global                      |   On Combo            |


#### Navigation
| Shortcut Function                | Key Combo                        |  Complexity-Availability           |   Execution method    |
|----------------------------------|----------------------------------|------------------------------------|-----------------------|
| Go to the admin index page       | `Ctrl+I`                         |   Normal-Global                    |   On Combo            |
| View site / Go to the `/`        | `Ctrl+Z`                         |   Normal-Global                    |   On Combo            |
| Go to the Logout page            | `Ctrl+L`                         |   Normal-Global                    |   On Combo            |
| Go to the next page              | `Ctrl+B`                         |   Normal-Change list               |   On Combo            |
| Go to the previous page          | `Ctrl+V`                         |   Normal-Change list               |   On Combo            |
| Go to the nth page               | `Ctrl+X` + page number           |   Complex-Change list              |   On `Enter`          |


#### Object manage
| Shortcut Function                | Key Combo                        |  Complexity-Availability           |   Execution method    |
|----------------------------------|----------------------------------|------------------------------------|-----------------------|
| Add new object                   | `Alt+A`                          |   Normal-Change list               |   On Combo            |
| Save & Add                       | `Alt+A`                          |   Normal-Change form               |   On Combo            |
| Save & Editing                   | `Alt+E`                          |   Normal-Change form               |   On Combo            |
| Save                             | `Alt+S`                          |   Normal-Change form               |   On Combo            |
| Delete                           | `Alt+D`                          |   Normal-Change form               |   On Combo            |
| Delete confirmation / Yes        | `Alt+Y`                          |   Normal-Change form               |   On Combo            |
| Delete cancel / No               | `Alt+N`                          |   Normal-Change form               |   On Combo            |


#### Search
| Shortcut Function                | Key Combo                        | Complexity-Availability           |   Execution method    |
|----------------------------------|----------------------------------|-----------------------------------|-----------------------|
| Search Focus                     | `Ctrl+/`                         |    Normal-Change list             |   On Combo            |
| Search filter(filter comm list)  | `Ctrl+S`                         |    Normal-Global                  |   On Combo            |




#### Special
| Shortcut Function     | Key Combo                                        | Complexity-Availability                |   Execution method    |
|-----------------------|--------------------------------------------------|----------------------------------------|-----------------------|
| Search(without query) |  `Ctrl+K` + "?" + "model" +  `Enter`             |   Complex-Global                       |    On `Enter`         |
| Search(with query)    |  `Ctrl+K` + "?" + "model" + "query" +  `Enter`   |   Complex-Global                       |    On `Enter`         |
| Update(without query) |  `Ctrl+K` + ">" + "model" +  `Enter`             |   Complex-Global                       |    On `Enter`         |
| Update(with query)    |  `Ctrl+K` + ">" + "model" + "query" +  `Enter`   |   Complex-Global                       |    On `Enter`         |
| Delete(without query) |  `Ctrl+K` + "<" + "model" +  `Enter`             |   Complex-Global                       |    On `Enter`         |
| Delete(with query)    |  `Ctrl+K` + "<" + "model" + "query" +  `Enter`   |   Complex-Global                       |    On `Enter`         |
| Add(without query)    |  `Ctrl+K` + "+" + "model" +  `Enter`             |   Complex-Global                       |    On `Enter`         |
| Add(with query)       |  `Ctrl+K` + "+" + "model" + "query" +  `Enter`   |   Complex-Global                       |    On `Enter`         |


Example :-

```"Ctrl+K" + "?" + "model selection" + "query string" + "Enter"```


- Each command part will be separated by "|" character for eazy recognition and to split a given command. So full command will look like below.

Example look :- 

```"Ctrl+K" + "?" + "|" + "model selection" + "|" + "query string" + "Enter"```

Visual appearance :- 

```"?" + "|" + "model selection" + "|" + "query string"```

Example appearance :- 

```?|Post|hello```



# Note 
- No dependency (js, python or django)
- Customisable through `settings.py`
  

