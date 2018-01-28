<center><h1>Udacity Intro to Programming Nano-Degree Final Project</center></h1>

## Introduction

The final project for this nano-degree is a postgresql-backed python app that replicates a swiss style tournament.  This document will walk you through setting up and running the application.

## Changelog

* 03/05/2016 - first submission as a test (lets see how far I got..).
* 03/05/2016 - second submission fixing the following bugs
	* Included with statements broken between Python 2.7.5 and 2.7.6, see details [here](http://stackoverflow.com/questions/32379147/understanding-the-python-with-statement) 
	* Included sql file now generates the project database instead of being created manually
	* README file included

## Usage

To test this project, first pull down this repository:

```bash
git clone https://github.com/akio-outori/udacity.git
```

Then navitage to the final_project directory:

```bash
cd udacity/final_project
```

Import the database:

```bash
psql < tournament.sql
```

And finally run the unit tests:

```bash
python ./tournament_test.py
``` 
