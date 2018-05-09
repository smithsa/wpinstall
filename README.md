## wpinstall
A shell script that will automate the creation of a custom installation of a Wordpress setup with a Foudnationpress theme. Additionally, the script adds a python script that will automate page and template creation within the Foudnationpress theme.

## Motivation
This decreases the time and steps involved in a tedious setup for a wordpress build.

## Dependencies
Wordpress Installation Script
[WP CLI](https://wp-cli.org/)

Template Creation Script
[python-wordpress-xmlrpc](http://python-wordpress-xmlrpc.readthedocs.io/en/latest/)

## Installation
In your terminal navigate to the same level of the file "wpinstall.sh." Simply run the command below and follow the proceeding prompts.
```
. wpinstall.sh
```

## Usage
Once the build is complete, you will have access to automate the create of template php files in the Foundationpress theme as well as pages in wordpress connected to the template just created, image folders for the template, and sass files (ready to be compiled) for the template.

Create a template php file in the foundationpress theme, image folder, and sass file ready to be compiled
```
create [insert template name here]
```

Remove the template php file in the foundationpress theme, image folder, and sass file ready to be compiled
```
remove [insert template name here]
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
MIT © [Sade Smith](http://sadesmith.com)