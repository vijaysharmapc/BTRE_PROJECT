DJANGO: It's job is to receive http request and send responses. WHat response it sends is your job

What this learning path covers
Module 1, Getting Started with Python Data Analysis, shows how to work with time oriented data in Pandas. How do you clean, inspect, reshape, merge, or group data –these are the concerns in this chapter. The library of choice in the course will be Pandas again.

Module 2, Python Data Analysis Cookbook, demonstrates how to visualize data and mentions frequently encountered pitfalls. Also, discusses statistical probability distributions and correlation between two variables.

Module 3, Mastering Python Data Analysis, introduces linear, multiple, and logistic regression with in-depth examples of using SciPy and stats models packages to test various hypotheses of relationships between variables.

NumPy 1.9.2,Pandas 0.16.2, matplotlib 1.4.3, tables 3.2.2, pymongo 3.0.3, redis 2.10.3, and scikit-learn 0.16.1. As these packages are all hosted on PyPI, the Python package index, they can be easily installed with pip. To install NumPy, you would write:

$ pip install numpy

steps in data analysis:
collecting data
organizing
summarizing
analysis
synthesis (the combination of ideas to form a theory or system.)
decision making
feedback


AI knowledge
Domain Knowledge
Comp science knowledge
Stats and Maths knowledsge magic quadrants

There are numerous data analysis libraries that help us to process and analyze data. They use different programming languages, and have different advantages and disadvantages of solving various data analysis problems. Now, we will introduce some common libraries that may be useful for you. They should give you an overview of the libraries in the field. However, the rest of this book focuses on Python-based libraries.

Some of the libraries that use the Java language for data analysis are as follows:

Weka: This is the library that I became familiar with the first time I learned about data analysis. It has a graphical user interface that allows you to run experiments on a small dataset. This is great if you want to get a feel for what is possible in the data processing space. However, if you build a complex product, I think it is not the best choice, because of its performance, sketchy API design, non-optimal algorithms, and little documentation (http://www.cs.waikato.ac.nz/ml/weka/).
Mallet: This is another Java library that is used for statistical natural language processing, document classification, clustering, topic modeling, information extraction, and other machine-learning applications on text. There is an add-on package for Mallet, called GRMM, that contains support for inference in general, graphical models, and training of Conditional random fields (CRF) with arbitrary graphical structures. In my experience, the library performance and the algorithms are better than Weka. However, its only focus is on text-processing problems. The reference page is at http://mallet.cs.umass.edu/.
Mahout: This is Apache's machine-learning framework built on top of Hadoop; its goal is to build a scalable machine-learning library. It looks promising, but comes with all the baggage and overheads of Hadoop. The homepage is at http://mahout.apache.org/.
Spark: This is a relatively new Apache project, supposedly up to a hundred times faster than Hadoop. It is also a scalable library that consists of common machine-learning algorithms and utilities. Development can be done in Python as well as in any JVM language. The reference page is at https://spark.apache.org/docs/1.5.0/mllib-guide.html.
Here are a few libraries that are implemented in C++:

Vowpal Wabbit: This library is a fast, out-of-core learning system sponsored by Microsoft Research and, previously, Yahoo! Research. It has been used to learn a tera-feature (1012) dataset on 1,000 nodes in one hour. More information can be found in the publication at http://arxiv.org/abs/1110.4198.
MultiBoost: This package is a multiclass, multi label, and multitask classification boosting software implemented in C++. If you use this software, you should refer to the paper published in 2012 in the JournalMachine Learning Research, MultiBoost: A Multi-purpose Boosting Package, D.Benbouzid, R. Busa-Fekete, N. Casagrande, F.-D. Collin, and B. Kégl.
MLpack: This is also a C++ machine-learning library, developed by the Fundamental Algorithmic and Statistical Tools Laboratory (FASTLab) at Georgia Tech. It focusses on scalability, speed, and ease-of-use, and was presented at the BigLearning workshop of NIPS 2011. Its homepage is at http://www.mlpack.org/about.html.
Caffe: The last C++ library we want to mention is Caffe. This is a deep learning framework made with expression, speed, and modularity in mind. It is developed by the Berkeley Vision and Learning Center (BVLC) and community contributors. You can find more information about it at http://caffe.berkeleyvision.org/.
Other libraries for data processing and analysis are as follows:

Statsmodels: This is a great Python library for statistical modeling and is mainly used for predictive and exploratory analysis.
Modular toolkit for data processing (MDP): This is a collection of supervised and unsupervised learning algorithms and other data processing units that can be combined into data processing sequences and more complex feed-forward network architectures (http://mdp-toolkit.sourceforge.net/index.html).
Orange: This is an open source data visualization and analysis for novices and experts. It is packed with features for data analysis and has add-ons for bioinformatics and text mining. It contains an implementation of self-organizing maps, which sets it apart from the other projects as well (http://orange.biolab.si/).
Mirador: This is a tool for the visual exploration of complex datasets, supporting Mac and Windows. It enables users to discover correlation patterns and derive new hypotheses from data (http://orange.biolab.si/).
RapidMiner: This is another GUI-based tool for data mining, machine learning, and predictive analysis (https://rapidminer.com/).
Theano: This bridges the gap between Python and lower-level languages. Theano gives very significant performance gains, particularly for large matrix operations, and is, therefore, a good choice for deep learning models. However, it is not easy to debug because of the additional compilation layer.
Natural language processing toolkit (NLTK): This is written in Python with very unique and salient features.
Here, I could not list all libraries for data analysis. However, I think the above libraries are enough to take a lot of your time to learn and build data analysis applications. I hope you will enjoy them after reading this book.

Library: is a collection of functions & methods that help perform a function without writing any code

Python libraries in data analysis
Python is a multi-platform, general-purpose programming language that can run on Windows, Linux/Unix, and Mac OS X, and has been ported to Java and .NET virtual machines as well. It has a powerful standard library. In addition, it has many libraries for data analysis: Pylearn2, Hebel, Pybrain, Pattern, MontePython, and MILK. In this book, we will cover some common Python data analysis libraries such as Numpy, Pandas, Matplotlib, PyMongo, and scikit-learn. Now, to help you get started, I will briefly present an overview of each library for those who are less familiar with the scientific Python stack.

NumPy
One of the fundamental packages used for scientific computing in Python is Numpy. Among other things, it contains the following:

A powerful N-dimensional array object
Sophisticated (broadcasting) functions for performing array computations
Tools for integrating C/C++ and Fortran code
Useful linear algebra operations, Fourier transformations, and random number capabilities
Besides this, it can also be used as an efficient multidimensional container of generic data. Arbitrary data types can be defined and integrated with a wide variety of databases.

Pandas
Pandas is a Python package that supports rich data structures and functions for analyzing data, and is developed by the PyData Development Team. It is focused on the improvement of Python's data libraries. Pandas consists of the following things:

A set of labeled array data structures; the primary of which are Series, DataFrame, and Panel
Index objects enabling both simple axis indexing and multilevel/hierarchical axis indexing
An intergraded group by engine for aggregating and transforming datasets
Date range generation and custom date offsets
Input/output tools that load and save data from flat files or PyTables/HDF5 format
Optimal memory versions of the standard data structures
Moving window statistics and static and moving window linear/panel regression
Due to these features, Pandas is an ideal tool for systems that need complex data structures or high-performance time series functions such as financial data analysis applications.

Matplotlib
Matplotlib is the single most used Python package for 2D-graphics. It provides both a very quick way to visualize data from Python and publication-quality figures in many formats: line plots, contour plots, scatter plots, and Basemap plots. It comes with a set of default settings, but allows customization of all kinds of properties. However, we can easily create our chart with the defaults of almost every property in Matplotlib.

PyMongo
MongoDB is a type of NoSQL database. It is highly scalable, robust, and perfect to work with JavaScript-based web applications, because we can store data as JSON documents and use flexible schemas.

PyMongo is a Python distribution containing tools for working with MongoDB. Many tools have also been written for working with PyMongo to add more features such as MongoKit, Humongolus, MongoAlchemy, and Ming.

The scikit-learn library
The scikit-learn is an open source machine-learning library using the Python programming language. It supports various machine learning models, such as classification, regression, and clustering algorithms, interoperated with the Python numerical and scientific libraries NumPy and SciPy. The latest scikit-learn version is 0.16.1, published in April 2015.

NumPy is the fundamental package supported for presenting and computing data with high performance in Python. It provides some interesting features as follows:

Extension package to Python for multidimensional arrays (ndarrays), various derived objects (such as masked arrays), matrices providing vectorization operations, and broadcasting capabilities. Vectorization can significantly increase the performance of array computations by taking advantage of Single Instruction Multiple Data (SIMD) instruction sets in modern CPUs.
Fast and convenient operations on arrays of data, including mathematical manipulation, basic statistical operations, sorting, selecting, linear algebra, random number generation, discrete Fourier transforms, and so on.
Efficiency tools that are closer to hardware because of integrating C/C++/Fortran code.
NumPy is a good starting package for you to get familiar with arrays and array-oriented computing in data analysis. Also, it is the basic step to learn other, more effective tools such as Pandas, which we will see in the next chapter. We will be using NumPy version 1.9.1.

An overview of the Pandas package
Pandas is a Python package that supports fast, flexible, and expressive data structures, as well as computing functions for data analysis. The following are some prominent features that Pandas supports:
Let's first get acquainted with two of Pandas' primary data structures: the Series and the DataFrame. They can handle the majority of use cases in finance, statistic, social science, and many areas of engineering.
A Series is a one-dimensional object similar to an array, list, or column in table. Each item in a Series is assigned to an entry in an index:

Data structure with labeled axes. This makes the program clean and clear and avoids common errors from misaligned data.
Flexible handling of missing data.
Intelligent label-based slicing, fancy indexing, and subset creation of large datasets.
Powerful arithmetic operations and statistical computations on a custom axis via axis label.
Robust input and output support for loading or saving data from and to files, databases, or HDF5 format.
Related to Pandas installation, we recommend an easy way, that is to install it as a part of Anaconda, a cross-platform distribution for data analysis and scientific computing. You can refer to the reference at http://docs.continuum.io/anaconda/ to download and install the library.

After installation, we can use it like other Python packages. Firstly, we have to import the following packages at the beginning of the program:


classes have properties associated with them

#Open a file, this will create a new file and keep it in w or write mode
myFile = open('myfile.txt', 'w')

print(myFile.name)
print(myFile.closed)
print(myFile.mode)

#write to the file
myFile.write('I love Python')
myFile.write('I love data too')
myFile.close()


# JASON TO DICT
import json

#sample jason
userJSON = '{"name" : "vijay", "age" : "34", "height" : "5.8"}'

#parse to dict
user = json.loads(userJSON)
print(user)
print(user['name'])

in py35
pip install django
(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment$ pip install django
django-admin help
pip freeze # all pip instalations


(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ pip freeze
alabaster==0.7.10
anaconda-client==1.6.3
anaconda-navigator==1.6.2
anaconda-project==0.6.0
asn1crypto==0.22.0
astroid==1.4.9
astropy==1.3.2
azureml==0.2.7
Babel==2.4.0
backports.shutil-get-terminal-size==1.0.0
beautifulsoup4==4.6.0
bitarray==0.8.1
blaze==0.10.1
bleach==1.5.0
bokeh==0.12.5
boto==2.46.1
Bottleneck==1.2.1
cffi==1.10.0
chardet==3.0.3
click==6.7
cloudpickle==0.2.2
clyent==1.2.2
colorama==0.3.9
contextlib2==0.5.5
cryptography==1.8.1
cycler==0.10.0
Cython==0.25.2
cytoolz==0.8.2
dask==0.14.3
datashape==0.5.4
decorator==4.0.11
distributed==1.16.3
Django==2.2.9
docutils==0.13.1
entrypoints==0.2.2
et-xmlfile==1.0.1
fastcache==1.0.2
Flask==0.12.2
Flask-Cors==3.0.2
gevent==1.2.1
google-api-python-client==1.6.2
greenlet==0.4.12
h5py==2.7.0
HeapDict==1.0.0
html5lib==0.999
httplib2==0.10.3
idna==2.5
imagesize==0.7.1
ipykernel==4.6.1
ipython==5.3.0
ipython-genutils==0.2.0
ipywidgets==6.0.0
isort==4.2.5
itsdangerous==0.24
jdcal==1.3
jedi==0.10.2
Jinja2==2.9.6
json-lines==0.3.1
jsonschema==2.6.0
jupyter==1.0.0
jupyter-client==5.0.1
jupyter-console==5.1.0
jupyter-core==4.3.0
lazy-object-proxy==1.2.2
line-profiler==2.0
llvmlite==0.18.0
locket==0.2.0
lockfile==0.12.2
luigi==2.7.3
lxml==3.7.3
MarkupSafe==0.23
matplotlib==2.0.2
memory-profiler==0.50.0
mistune==0.7.4
mpmath==0.19
msgpack-python==0.4.8
multipledispatch==0.4.9
navigator-updater==0.1.0
nbconvert==5.1.1
nbformat==4.3.0
networkx==1.11
nltk==3.2.3
nose==1.3.7
notebook==5.0.0
numba==0.33.0
numexpr==2.6.2
numpy==1.12.1
numpydoc==0.6.0
oauth2client==4.1.2
odo==0.5.0
olefile==0.44
openpyxl==2.4.7
packaging==16.8
pandas==0.20.1
pandocfilters==1.4.1
partd==0.3.8
pathlib2==2.2.1
patsy==0.4.1
pep8==1.7.0
pexpect==4.2.1
pickleshare==0.7.4
Pillow==4.1.1
ply==3.10
prompt-toolkit==1.0.14
psutil==5.2.2
ptyprocess==0.5.1
py==1.4.33
pyasn1==0.3.2
pyasn1-modules==0.0.11
pycosat==0.6.2
pycparser==2.17
pycrypto==2.6.1
pycurl==7.43.0
pydot==1.2.4
pydotplus==2.0.2
pyflakes==1.5.0
Pygments==2.2.0
pylint==1.6.4
pyodbc==4.0.16
pyOpenSSL==17.0.0
pyparsing==2.1.4
pyspark==2.1.0+hadoop2.7
pytest==3.0.7
python-daemon==2.1.2
python-dateutil==2.6.0
pytz==2017.2
PyWavelets==0.5.2
PyYAML==3.12
pyzmq==16.0.2
QtAwesome==0.4.4
qtconsole==4.3.0
QtPy==1.2.1
requests==2.14.2
rope-py3k==0.9.4.post1
rsa==3.4.2
scikit-image==0.13.0
scikit-learn==0.18.1
scipy==0.19.0
seaborn==0.7.1
simplegeneric==0.8.1
singledispatch==3.4.0.3
six==1.10.0
snowballstemmer==1.2.1
sortedcollections==0.5.3
sortedcontainers==1.5.7
Sphinx==1.5.6
spyder==3.1.4
SQLAlchemy==1.1.9
sqlparse==0.3.0
statsmodels==0.8.0
sympy==1.0
tables==3.3.0
tblib==1.3.2
terminado==0.6
testpath==0.3
textblob==0.15.1
toolz==0.8.2
tornado==4.5.1
traitlets==4.3.2
treeinterpreter==0.2.1
unicodecsv==0.14.1
uritemplate==3.0.0
wcwidth==0.1.7
Werkzeug==0.12.2
widgetsnbextension==2.0.0
wordcloud==1.3.1
wrapt==1.10.10
xlrd==1.0.0
XlsxWriter==0.9.6
xlwt==1.2.0
zict==0.1.2
You are using pip version 9.0.1, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ djano
djano: command not found
(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ django-admin help

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environmen

ngs.).
(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ django-admin startproject btre .
(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ manage.py help
manage.py: command not found
(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ python manage.py help

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver


Django- comes withd ev server
used to develop locally


(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

January 04, 2020 - 20:23:26
Django version 2.2.9, using settings 'btre.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

wsgi web serv communicates with web applications & how web apps can be chained together?


(py35) vijay@vijay-VirtualBox:~/Python_Django_dev_to_deployment/BTRE_PROJECT$ python manage.py startapp pages
add this app pages to settings.py
create urls.py in pages app
link pages.url in urls.py-->btre

pages, templates n base layout
next tell Django where to look for templates

# handle static files & impliment bootstarp
python manage.py collectstatic
creates static
