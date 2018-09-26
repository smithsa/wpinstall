## wpinstall
A shell script that will automate the creation of a custom installation of a Wordpress setup with a Foudnationpress theme. Connects to local database, install plugins, and the Foundationpress Theme. Additionally, the script adds a python script that will automate page and template creation within a theme via the command line.

## Motivation
This decreases the time and steps involved in a tedious setup for wordpress builds. 

## Prerequisites
*	[WP CLI](https://wp-cli.org/)
*	[WGET](https://www.gnu.org/software/wget/) - used to retrieve file via HTTP
*	[Python](https://www.python.org/) - for the python script
*	[python-wordpress-xmlrpc](http://python-wordpress-xmlrpc.readthedocs.io/en/latest/) - template page creation

## Installation
1. Clone the repository
```
git clone git@github.com:smithsa/wpinstall.git
```

2. In your terminal navigate to the directory where the file "wpinstall.sh" lives. Simply run the command below and follow the proceeding prompts.
```
. wpinstall.sh
```

## Usage
Once the build is complete, you will have access to automate the creation of template php files in the Foundationpress theme as well as pages in wordpress connected to the template just created, image folders for the template, and sass files (ready to be compiled) for the template.


** Python Script Commands **
*To use these commands navigate to the theme level.*

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