Title: GitHub - alufers/mitmproxy2swagger: Automagically reverse-engineer REST APIs via capturing traffic

URL Source: https://github.com/alufers/mitmproxy2swagger

Markdown Content:
mitmproxy2swagger
-----------------

[](https://github.com/alufers/mitmproxy2swagger#mitmproxy2swagger)

[![Image 9: PyPI version](https://camo.githubusercontent.com/18c1534b2b1e7a23bf322f06d52749c1a511f391fb6cb7153339e71fa93a3b97/68747470733a2f2f62616467652e667572792e696f2f70792f6d69746d70726f787932737761676765722e737667)](https://badge.fury.io/py/mitmproxy2swagger) [![Image 10: Arch Linux repository](https://camo.githubusercontent.com/65853a26d224252b94a0df6938cab3da25f7afa499508cdb9df96fbbeae00b7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f617263686c696e75782d6d69746d70726f787932737761676765722d626c7565)](https://archlinux.org/packages/extra/any/mitmproxy2swagger/)

video.mp4A tool for automatically converting [mitmproxy](https://mitmproxy.org/) captures to [OpenAPI 3.0](https://swagger.io/specification/) specifications. This means that you can automatically reverse-engineer REST APIs by just running the apps and capturing the traffic.

* * *

**🆕 NEW!**

Added support for processing HAR exported from the browser DevTools. See [Usage - HAR](https://github.com/alufers/mitmproxy2swagger#har) for more details.

* * *

Installation
------------

[](https://github.com/alufers/mitmproxy2swagger#installation)

First you will need python3 and pip3.

$ pip install mitmproxy2swagger
# ... or ...
$ pip3 install mitmproxy2swagger
# ... or ...
$ git clone git@github.com:alufers/mitmproxy2swagger.git
$ cd mitmproxy2swagger
$ docker build -t mitmproxy2swagger .

Then clone the repo and run `mitmproxy2swagger` as per examples below.

Usage
-----

[](https://github.com/alufers/mitmproxy2swagger#usage)

### Mitmproxy

[](https://github.com/alufers/mitmproxy2swagger#mitmproxy)

To create a specification by inspecting HTTP traffic you will need to:

1.  Capture the traffic by using the mitmproxy tool. I personally recommend using mitmweb, which is a web interface built-in to mitmproxy.
    
    $ mitmweb
    Web server listening at http://127.0.0.1:8081/
    Proxy server listening at http://\*:9999
    ...
    
    **IMPORTANT**
    
    To configure your client to use the proxy exposed by mitm proxy, please consult the [mitmproxy documentation](https://docs.mitmproxy.org/stable/) for more information.
    
2.  Save the traffic to a flow file.
    
    In mitmweb you can do this by using the "File" menu and selecting "Save":
    
    [![Image 11: A screenshot showing the location of the "Save" option in the "File" menu](https://github.com/alufers/mitmproxy2swagger/raw/master/docs/mitmweb_save.png)](https://github.com/alufers/mitmproxy2swagger/blob/master/docs/mitmweb_save.png)
    
3.  Run the first pass of mitmproxy2swagger:
    
    $ mitmproxy2swagger -i <path\_to\_mitmptoxy\_flow\> -o <path\_to\_output\_schema\> -p <api\_prefix\>
    # ... or ...
    $ docker run -it -v $PWD:/app mitmproxy2swagger mitmproxy2swagger -i <path\_to\_mitmptoxy\_flow\> -o <path\_to\_output\_schema\> -p <api\_prefix\>
    
    Please note that you can use an existing schema, in which case the existing schema will be extended with the new data. You can also run it a few times with different flow captures, the captured data will be safely merged.
    
    `<api_prefix>` is the base url of the API you wish to reverse-engineer. You will need to obtain it by observing the requests being made in mitmproxy.
    
    For example if an app has made requests like these:
    
    https://api.example.com/v1/login
    https://api.example.com/v1/users/2
    https://api.example.com/v1/users/2/profile
    
    The likely prefix is `https://api.example.com/v1`.
    
4.  Running the first pass should have created a section in the schema file like this:
    
    x-path-templates:
      # Remove the ignore: prefix to generate an endpoint with its URL
      # Lines that are closer to the top take precedence, the matching is greedy
      - ignore:/addresses
      - ignore:/basket
      - ignore:/basket/add
      - ignore:/basket/checkouts
      - ignore:/basket/coupons/attach/{id}
      - ignore:/basket/coupons/attach/104754
    
    You should edit the schema file with a text editor and remove the `ignore:` prefix from the paths you wish to be generated. You can also adjust the parameters appearing in the paths.
    
5.  Run the second pass of mitmproxy2swagger:
    
    $ mitmproxy2swagger -i <path\_to\_mitmptoxy\_flow\> -o <path\_to\_output\_schema\> -p <api\_prefix\> \[--examples\]
    # ... or ...
    $ docker run -it -v $PWD:/app mitmproxy2swagger mitmproxy2swagger -i <path\_to\_mitmptoxy\_flow\> -o <path\_to\_output\_schema\> -p <api\_prefix\> \[--examples\]
    
    Run the command a second time (with the same schema file). It will pick up the edited lines and generate endpoint descriptions.
    
    Please note that mitmproxy2swagger will not overwrite existing endpoint descriptions, if you want to overwrite them, you can delete them before running the second pass.
    
    Passing `--examples` will add example data to requests and responses. Take caution when using this option, as it may add sensitive data (tokens, passwords, personal information etc.) to the schema. Passing `--headers` will add headers data to requests and responses. Take caution when using this option, as it may add sensitive data (tokens, passwords, personal information etc.) to the schema.
    

### HAR

[](https://github.com/alufers/mitmproxy2swagger#har)

1.  Capture and export the traffic from the browser DevTools.
    
    In the browser DevTools, go to the Network tab and click the "Export HAR" button.
    
    [![Image 12: A screenshot showing where the export har button is located](https://github.com/alufers/mitmproxy2swagger/raw/master/docs/export_har_button.png)](https://github.com/alufers/mitmproxy2swagger/blob/master/docs/export_har_button.png)
    
2.  Continue the same way you would do with the mitmproxy dump. `mitmproxy2swagger` will automatically detect the HAR file and process it.
    

Example output
--------------

[](https://github.com/alufers/mitmproxy2swagger#example-output)

See the [examples](https://github.com/alufers/mitmproxy2swagger/blob/master/example_outputs). You will find a generated schema there and an html file with the generated documentation (via [redoc-cli](https://www.npmjs.com/package/redoc-cli)).

See the generated html file [here](https://raw.githack.com/alufers/mitmproxy2swagger/master/example_outputs/lisek-static.html).

Development and contributing
----------------------------

[](https://github.com/alufers/mitmproxy2swagger#development-and-contributing)

This project uses:

*   [poetry](https://python-poetry.org/) for dependency management
*   [pre-commit](https://pre-commit.com/) for code formatting and linting
*   [pytest](https://docs.pytest.org/en/stable/) for unit testing

To install the dependencies:

Run linters:

pre-commit run --all-files

Install pre-commit hooks:

Run tests:

Run tests with coverage:

poetry run pytest --cov=mitmproxy2swagger

License
-------

[](https://github.com/alufers/mitmproxy2swagger#license)

MIT
