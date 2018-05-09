#!/bin/bash
echo "****************************************************"
echo "*********** Custom Wordpress Installation **********"
echo "****************************************************"
# echo "starting server"
# mysql.server start
echo ""
echo "Enter Project Name:"
read projectname
echo "Enter Wordpress Password:"
read password
echo "Enter your email for wordpress installation:"
read useremail
echo "Enter databse password (host:localhost and user:root) :"
read dbpass
echo "***** Installing Wordpress Installation and Databse *****"
wp core download --path=$projectname
cd $projectname
wp core config --dbname=$projectname --dbuser=root --dbpass=$dbpass --dbhost=127.0.0.1:8889
wp db create
title=`echo ${projectname:0:1} | tr  '[a-z]' '[A-Z]'`${projectname:1}
wp core install --url=$projectname --title=$title --admin_user=wpmaser --admin_password=$password --admin_email=$useremail
echo ">> Username: wpmaser"
echo ">> Password: $password"
echo "Removing unused themes"
cd wp-content/themes/
rm -rf twentyfifteen
rm -rf twentyseventeen
rm -rf twentysixteen
echo "***** Installing FoundationPress *****"
git clone https://github.com/olefredrik/FoundationPress.git
cd FoundationPress
echo "***** Installing NPM *****"
npm install
echo "***** Activating the FoundationPress theme *****"
wp theme activate FoundationPress
echo "***** Adding create template script *****"
wget "https://gist.githubusercontent.com/smithsa/3d83cf580a1adc329894df4fba763999/raw/4c76436b976b7d04b0ad277fbdc9925523477361/create_template.py"
echo "***** Installing Types plugin *****"
wp plugin install companion-auto-update
echo "***** Activating Companion Auto Update plugin *****"
wp plugin activate companion-auto-update
echo "***** Installing Companion Auto Update plugin *****"
wp plugin install types
echo "***** Activating Types plugin *****"
wp plugin activate types
echo "***** Installing xml-rpc-modernization plugin *****"
wp plugin install xml-rpc-modernization
echo "***** Activating xml-rpc-modernization plugin *****"
wp plugin activate xml-rpc-modernization
echo "***** Installing wordfence plugin *****"
wp plugin install wordfence
echo "***** Activating wordfence plugin *****"
wp plugin activate wordfence
RED='\033[0;31m'
NC='\033[0m'
printf "${RED}Warning: Remeber to deactivate xml-rpc-modernization in production environment${NC}\n"
