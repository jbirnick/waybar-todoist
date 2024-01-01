# waybar-todoist

This script uses the [official Todoist API](https://developer.todoist.com/) to indicate the number of tasks of each priority level.

![screenshot_todoist_module](screenshots/module.png)

By default, it considers the tasks with filter `today | overdue | no due date`, but you can easily change that.

The same module is available for polybar [here](https://github.com/jbirnick/polybar-todoist).

## Installation

0. Download [waybar-todoist.py](https://raw.githubusercontent.com/jbirnick/waybar-todoist/master/waybar-todoist.py) from this repo.
1. Install the [official Todoist Python Module](https://github.com/Doist/todoist-api-python). (e.g. with `pip install todoist-api-python`)
2. [Configure the API Token retrieval](#api-token-retrieval).
3. Copy-paste the following example configuration into your waybar config:
   ```json
   "custom/todoist": {
     "exec": "python -u ~/Coding/waybar-todoist/waybar-todoist.py",
     "exec-on-even": false,
     "return-type": "json",
     "interval": 20,
     "on-click": "gtk-launch todoist",
     "tooltip": false
   }

   ```

Note that the Todoist API has [request limits](https://developer.todoist.com/rest/v2/#request-limits), so you shouldn't set the interval too low.

## API Token retrieval

To get your Todoist tasks, the python module uses the [Todoist API](https://developer.todoist.com/). This requires an API Token.
You can get one in the [Todoist Integrations Settings](https://todoist.com/prefs/integrations). (Todoist -> Settings -> Integrations)

Now the tricky part is how the `waybar-todoist.py` script gets access to your API token. For this, the script implements a `api_token()` function.
You are required to implement this method, such that it returns your API token.

The simplest way would be to hard-code it into the script (i.e. `return <YOUR_API_TOKEN>`), but I don't recommend this.
Rather, query it from your password manager / keyring, or read it from an external file.

By default, it asks [GNOME Keyring](https://wiki.archlinux.org/index.php/GNOME/Keyring) for a password with the uuid `todoist_api_token`. So if you use GNOME Keyring anyway, you can just execute
```
secret-tool store --label='Todoist API Token' uuid todoist_api_token
```
and type in your API Token. Then it works out of the box.

## Customization

The code is very short and simple. You can easily customize output style, task filter, and so on.
