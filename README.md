## Python Project Template

Generally with data projects the exiciting or memorable outcome is a visualization, analysis, report or prediction. Something that you can tangibly look at and share with your teammates and customers.  A lot of effort is often spent making the end-product look good at the expense of the quality of code that generates the product. While that may serve the purpose for a one-time analytic, a lack of focus on quality and maintainablity will make it difficult when revisiting the project or if the scope of analysis changes. Making an initial investment on modular, testable and documented code will pay dividends later on. 



This project structure builds upon the Cookiecutter Data Science Project structure. 

[Cookiecutter Data Science Project]: https://drivendata.github.io/cookiecutter-data-science/

tldr the goals of this template are to: 

* Collobrate more easily with others on this analysis 
* Feel more confident in the conclusions you are able to draw 
* Ensuring that your analysis is reproducible 

### Best Practices 

* Your project must use git for source control and be hosted on GitHub 
  * This will help you collobrate with others on the team and provide more visiblity into the analysis process.

  * Even if you are working alone, using git gives you a greater ability for experimentation by allowing you to quickly implement new ideas without worrying about breaking functionality. You will always have the ablity to go back to the last working state. 

  * The git commit log also can be used as a on-going diary of the progress of your project. 

* Notebooks should mainly be used for exploration and communication of results 
  * Its okay to start off working mainly in the notebook enviornment, but make sure to refactor the good parts into the package for your project.

* Project source code should contained within a Python Package

  * Packaging your source code as a package allows you to ensure that your code is testable and be confident that your results are reproducible.
  * It will be easier to share functionality between projects rather than repeatedly creating the same functionality. Don't reinvent the wheel.   

* All projects will use a conda environment to package project dependencies

  * Keeping track of your project dependencies will allow you to ensure that your analysis can be reproduced irregardless of the system that it was initially run on. 

* Python 3.x is encouraged for new projects unless 2.7.x is absolutely neccessary

  * It's 2017 just use 3.x

* Your project should be unit-tested



### Tool Installation 

* Make sure git is installed for your system: 
  * https://git-scm.com
  * If you are on windows, make sure to install git bash for windows
* Install Anaconda on your system
  * https://www.continuum.io/downloads
  * Prefer the 3.6 version unless you specifically need Python 2.7.x 
* Install an IDE of your choice. Some options are:
  * https://www.jetbrains.com/pycharm/
  * https://www.sublimetext.com
  * https://atom.io
  * https://code.visualstudio.com
  * Vim 



### Environment Setup 

Once the appropriate tools are installed. 

*  Open the terminal application on your system. 
   *  If you are on Windows use the Command Prompt application that is included with the Anaconda Installation. 
*  Run the following command:

    `conda env create -f environment.yml`

This command will instantiate the conda python enviornment for this project. Creating a  project specific python interpreter and downloading all the listed dependencies.  The standard template enviornment.yml contains the following: 

```yaml
name: boston_analytics
channels: !!python/tuple
- !!python/unicode
  'defaults'
dependencies:
- openssl=1.0.2j=0
- pip=9.0.1=py36_1
- python=3.6.0=0
- readline=6.2=2
- setuptools=27.2.0=py36_0
- sqlite=3.13.0=0
- tk=8.5.18=0
- unixodbc=2.3.4=0
- wheel=0.29.0=py36_0
- xz=5.2.2=1
- zlib=1.2.8=3
- pip:
  - arrow==0.10.0
  - attrs==16.3.0
  - cerberus==1.0.1
  - hypothesis==3.6.1
  - jsonpickle==0.9.4
  - kombu==4.0.2
  - numpy==1.12.0
  - pandas==0.19.2
  - pyaml==16.12.2
  - pyodbc==3.1.1
  - python-dateutil==2.6.0
  - pyyaml==3.12
  - requests==2.12.4
```

Once your initial enviornment is initialized you can "activate" the project environment by running `source activate <module_name>`. 

You can add new dependencies to the environment by running 

* `pip install <package_name>`
* `conda install -c <channel_name> <package_name>`
    * https://conda.io/docs/using/pkgs.html#install-a-package-from-anaconda-org

You can delete unecessary dependences by running:

* `conda remove --name <environment_name> <package_name>`

After installing all necessary dependences you can update the environment.yml file by running `conda env export > environment.yml` and make sure to commit these changes by running `git commit -am "updated dependencies"`



### Development Workflow Tips 
####  Iteratively Install Python Package
Generally during development I'll run pip in editable mode with: 
`pip install -e .`
after runnning this command pip will continiously monitor the directory for changes in the source code and reinstall your module when necessary. 







