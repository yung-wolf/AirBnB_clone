# AirBnB Clone

![AirBnB Image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T044552Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0921f33133d62d8b15fe3ce2116bc5015e9d8836fcc822a68bf8d01a3176fa3a)

## Purpose
The goal of the project is to deploy on our server a simple copy of the [AirBnB website](https://www.airbnb.com/).

We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Final product

![AirBnB Home page Image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T044552Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1f215671fc2360370a5d519369c68102c4bb37c6a50cff88a3767819922088b9)

![AirBnB Feature page Image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T044552Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5b7dbc4dd2a171f248855d0032c0ba45c86711736d9f82fc4d0146fc3795643a)

## Concepts to learn
* [Unittest](https://docs.python.org/3.8/library/uuid.html) - and please work all together on tests cases
* **Python packages** concept page
* Serialization/Deserialization
* \*args, \*\*kwargs
* datetime
* More coming soon!

## Steps

### The console
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### Web static
* learn HTML/CSS
* create the HTML of your application
* create template of each object

### MySQL storage
* replace the file storage by a Database storage
* map your models to a table in database by using an O.R.M.

### Web framework - templating
* create your first web server in Python
* make your static HTML file dynamic by using objects stored in a file or database

### RESTful API
* expose all your objects stored via a JSON web interface
* manipulate your objects via a RESTful API

### Web dynamic
* learn JQuery
* load objects from the client side by using your own RESTful API


## Execution
**description of the command interpreter:**
The program starts by running the command **./console.py** in the terminal. The program allows you to interact with your it by typing commands.
* The program displays a prompt. The prompt symbol is **(hbnb)**.
* The user types a command and presses Enter.
* The program parses the command into its component parts.
* The program finds function that implements the command.
* The program executes the command.
* The program displays the output of the command.
* The program returns to step 1. This happens until it's exited.

**Interactive mode**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
**Non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
