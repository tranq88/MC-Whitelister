# MC Whitelister
### A simple tool for mass whitelisting players on a Minecraft server.

I had to whitelist 20+ players on an SMP and didn't feel like entering `/whitelist add <name>` over and over again, so I searched for a way to mass whitelist and came across [this post](https://gaming.stackexchange.com/a/199426).

### How to use:
1. Download and run MC Whitelister.
2. You'll need a comma-separated list of all the players you want to whitelist. It should be in this format: `Notch,jeb_,Technoblade`. If you don't feel like typing each username out, a workaround is to [create a Google form](https://forms.new) where the players submit their own usernames. Then, you can export the responses to a Google spreadsheet and use the `=JOIN` formula to convert the column of usernames into one long string. [This article](https://www.highviewapps.com/blog/google-sheets-tip-generate-comma-separated-list-of-values-from-a-column/) explains it a lot better.
3. Paste the string into the program and hit OK. It will then generate a `whitelist.json` file in the same directory. If a username is invalid it'll be skipped. There may also be times when a valid username won't work; blame the [PlayerDB API](https://playerdb.co/) (although it's the backbone of this project).
4. Make sure the whitelist on your Minecraft server is enabled with `/whitelist on`. Replace the `whitelist.json` file in your server directory with the newly generated one and that's it!
