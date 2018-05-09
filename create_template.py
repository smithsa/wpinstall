import os
import sys
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPage

site_host = 'http://localhost:8888/'
image_directory = 'assets/images/'
sass_directory = 'assets/scss/templates/'
page_template_directory = 'page-templates/'
username = 'admin'
password = 'password'

def create_template_files(file_name):

	#1. create scss file
	#assets/scss/templates/_[name].scss
	try:
	    fh = open(sass_directory + '_'+ file_name + '.scss','r')
	except:
	# if file does not exist, create it
	    fh = open(sass_directory + '_'+ file_name + '.scss','w')

	#2. Import newly created Sass file to global one
	#assets/scss/templates/app.scss
	with open('assets/scss/foundation.scss', 'a') as f:
	    f.write('\n@import "templates/' + file_name + '";')
		    #f.writelines(lines)

	#3. create image folder
	#assets/images/[name]
	if not(os.path.exists(image_directory + file_name)):
		os.makedirs(image_directory + file_name)

	#4a. Create page template
	if not(os.path.exists(page_template_directory + file_name) ):
		with open(page_template_directory + file_name + '.php', 'a') as f:
			f.writelines(['<?php \n', '/* Template Name: '+ file_name.capitalize() +' */\n', '  get_header();\n', '?>', '\n\n', '<?php get_footer();'])
		#4b. Create page in wordpress and connect to the template page
		client = Client(site_host + 'xmlrpc.php', username, password)
		page = WordPressPage()
		page.title = file_name.capitalize()
		page.content = ''
		page.post_status = 'publish'
		page.template = 'page-templates/about.php'
		page.id = client.call(posts.NewPost(page))

def remove_template_files(file_name):
	try:
		os.remove(sass_directory + '_'+ file_name + '.scss')
	except:
		print sass_directory + '_'+ file_name + '.scss already deleted'
	try:
		os.removedirs(image_directory + file_name)
	except:
		print image_directory + file_name + ' already deleted'
	try:
		os.remove(page_template_directory + file_name + '.php')
	except:
		print page_template_directory + file_name + '.php already deleted'

	file_lines = []
	with open('assets/scss/foundation.scss') as f:
		content = f.readlines()
		for line in content:
			if('@import "templates/'+file_name+'"' in line):
				continue
			else:
				file_lines.append(line)

	f = open('assets/scss/foundation.scss','w')
	f.writelines(file_lines)
	f.close()
	page_id = find_id(file_name.capitalize())
	client = Client(site_host + 'xmlrpc.php', username, password)
	client.call(posts.DeletePost(page_id))


def find_id(title):
    offset = 0
    increment = 10
    client = Client(site_host + 'xmlrpc.php', username, password)
    while True:
        filter = {'post_type': 'page'}
        p = client.call(GetPosts(filter))
        if len(p) == 0:
                break 
        for post in p:
            if post.title == title:
                return(post.id)
        offset = offset + increment
    return(False)


if __name__ == '__main__':
    if(len(sys.argv) == 3):
        file_name = sys.argv[2]
        if(sys.argv[1] == 'create'):
            create_template_files(file_name)
        elif(sys.argv[1] == 'delete'):
            remove_template_files(file_name)
        else:
            print "second argument should be 'delete' or 'create'"

    else:
        print "3 arguments are required"
