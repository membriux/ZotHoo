# ZotHoo!
Search Engine web app using Flask framework that searches through UC Irvine's school Information and Computer Sciences' (ICS) directory.


## How it works

User types search input. The web app stems the input and uses it to find search results. The search time is very fast since we use a dictionary to store our index and use the stemmed search input as a key. If the key exists, that result will be returned.  

Search results are ranked using tf_idf scores and are displayed by showing the header and link of the result.

## Video Walkthrough/Example

![Walkthrough Video](https://github.com/membriux/ZotHoo/blob/master/walkthrough.gif)

## Built With

* [Flask](http://flask.pocoo.org/) - Web development framework for Python
* [Flask Paginate](https://pythonhosted.org/Flask-paginate/) - Microframework that adds pagination to web app
* [nltk](https://www.nltk.org/) - Text processing/Word Stemming/Tokenizer
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - File parser
* [Heroku](https://www.heroku.com/) - Platform for deploying web app

## Authors

* **Guillermo Sanchez** - [Membriux](https://github.com/membriux)
    - Initial deign/planning/prototying
    - MVC Architecture design + implementation
    - Parsing with BeatifulSoup4 
    - Flask/Flask-paginate framework implementation
    - Deployment configuration for Heroku
* **Eduardo Corona** - [jecorona97](https://github.com/jecorona97)
    - Design & implementation
    - Index construction, compression

## License

    Copyright 2019 Guillermo Sanchez & Eduardo Corona

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
