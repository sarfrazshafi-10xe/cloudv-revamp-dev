{
    "name": "Website Hello World",
    "version": "1.0",
    "summary": "Simple Hello World Website Module",
    "category": "Website",
    "author": "Muhammad Sarfraz Shafi",
    "depends": ["website"],
    "data": [
        "views/hello_temp.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "website_hello_world/static/src/css/style.css",
        ],
    },
    "installable": True,
    "application": True,
}
