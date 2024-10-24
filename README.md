<div align="center">
    <h1 align="center">pycat</h1>
    <p align="center">
        A clone of a simple Linux cmd tool
        <br/>
    </p>
</div>


### Introduction

A small effort to clone the `cat` tool that is present in Linux.
Previously I have built a clone of the `wc` commandline tool. You can find it [here](https://github.com/sayantandasgupta/wcclone).

A guide to building this `cat` tool clone can be found in the Coding Challenges [website](https://codingchallenges.fyi/challenges/challenge-cat)

### cat - What is it?

The `cat` tool is a very simple tool in Unix / Linux systems which helps us to print the contents of the file on the shell.

The syntax for `cat` is as follows

```bash
> cat test.json
  {
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}
> |
```

### Tech Stack

I have purely used Python to build this simple cmd tool. There are a lot of other languages I could have used but as I mentioned that I wanted to revise Python and to learn it in more depth I decided to build my next set of projects using Python.

Since this is a cmd tool, I had to ensure that we could use a package such that the script may be called from the command-line, with addition to certain options and arguments be provided through the cmd. There are a lot of very useful packages to achieve this but I decided to go with `click` as it provided very flexible funcitonalities.

Also, I have used the `setuptools` library which helps to build Python packages. This part was for my own learning and fun ✌️.

Enough talks, let us now understand how you can also build and run this tool in your own system.

### Build the Tool

#### 1. Fork the Repo

Fork the repo into your own account

#### 2. Clone the forked Repo

Use the following command in your Git Bash or your Bash Shell to clone the forked repo

```bash
> git clone https://github.com/<YOUR-GITHUB-USERNAME>/pycat.git
```

#### 3. Checkout a new branch

Don't do anything on the MAIN branch. Instead checkout a new branch and conduct all your tests there. Use the following command

```bash
> git checkout -m <BRANCH-NAME>
```

#### 4. Create a Python virtual environment

You don't need any extra packages to do this. If you have python installed on your machine, you can use the following command.

```bash
> python3 -m venv venv
```

or

```powershell
> py -m venv venv
```

I have written `python3` if you have both Python 2.x and 3.x versions installed on your system or if the `python` command does not work for you. (This is for Linux/Unix systems)

The second option is for Windows

Activate the environment,

In Unix / Linux,

```bash
> source venv/bin/activate
```

In Windows,

```powershell
> venv\Scripts\activate
```

#### 5. Setup the tool

After the virtual environment has been created, it is pretty straightforward from that. Since most of the code has already been written, all you need to do is just run the `setup.py` file to setup the tool pre-installation.

The command to do this is

```bash
> python setup.py sdist
```

This will create a dist folder and setup your tool there.

#### 6. Install the Tool

Once you have setup the tool, you need to install so that you can properly use the tool just like cmd command. 

Use the following command to install the tool,

```bash
> pip install dist/pycat-0.1.0.tar.gz
```

The `tar.gz` zipped file contains all the setup information and installation instructions to install the tool required. After the command stops executing, your tool shall be installed.

#### 7. Test the tool

If you have followed all the steps, you can now test the tool.

Use the following command

```bash
> pycat test.json
  {
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
  }
```

If the command does not give you the necessary output as you expected, do follow the installation steps properly. 

If you want to add any more functionalites please feel free to raise issues. I shall try to add those features.

Cheers!

![Made with love in India](https://madewithlove.now.sh/in?template=for-the-badge)