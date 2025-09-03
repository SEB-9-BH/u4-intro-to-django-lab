<h1>
  <span class="headline">Intro to Django Lab</span>
  <span class="subhead">Setup</span>
</h1>

## Setup

Open your Terminal application and navigate to your `~/code/ga/labs` directory:

```bash
cd ~/code/ga/labs
```

## Django Tutorial Setup

### Create a Database for the Project

PostgreSQL requires that a database be created manually before it can be used in projects. For our Django tutorial, we will create a database named `polls`.

Here's how to create the `polls` database using PostgreSQL:

```bash
createdb polls
```

Alternatively, you can use the PostgreSQL interactive terminal to create the database:

```bash
psql
CREATE DATABASE polls;
\l  # Lists all databases to confirm 'polls' has been created
\q  # Exit the psql shell
```

Make sure to note the username displayed next to the database name in the list, as you might need it depending on your PostgreSQL setup.

## Initialize a Django Project Environment

### Step 1: Set Up Your Project Directory

Navigate to your desired directory (e.g., `~/code/ga/lectures`) and create a new directory for your Django project:

```bash
mkdir my-django-project
cd my-django-project
```

### Step 2: Install Django Using Pipenv

Initialize a new virtual environment and install Django:

```bash
pipenv install django
```

This command creates a new `Pipfile` and `Pipfile.lock` in your project directory, specifying Django as a dependency.

> Look Familiar? This step is similar to `npm init` and `npm install` all in one.

### Step 3: Activate the Virtual Environment

Activate the pipenv shell, which is a subshell for your project:

```bash
pipenv shell
```

Your terminal prompt will change to indicate that you are working within a virtual environment.

### Step 4: Start Your Django Project

Now that your environment is ready, you can begin the actual Django tutorial for creating your first Django app:

- Follow the tutorial steps for setting up your Django project. Make sure to use the Django admin commands within the environment you just activated.

## Deactivating the Virtual Environment

When you're done working in the virtual environment, you can deactivate it by typing:

```bash
exit
```

This will return you to your normal shell environment.
