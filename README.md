# Webfaction Tools

A few tools for working with the Webfaction API and automatic deploys from Travis and Github

## Github keys

  - `ssh-keygen -t rsa -b 4096 -C "my-email@gmail.com"`
    - save as `~/.ssh/github`
    - leave passphrase blank
  - `eval "$(ssh-agent -s)"`
  - `ssh-add ~/.ssh/github`
  - add entry to `~/.ssh/config`
    ```
        Host github.com
            IdentityFile ~/.ssh/github
    ```
  - `cat ~/.ssh/github.pub`
  - copy and paste the key from terminal to Github using their web UI
  - if there is an issue with permissions
    - `chmod 600 ~/.ssh/*`
    - `chmod 700 ~/.ssh`  

## Sending emails

  - Setup an email mailbox using the Web UI

  - Copy the example `email-config.json` file and modify as necessary.

  - Set environment variables for `SMTP_USER` and `SMTP_PASSWORD`
    - These can be added to `~/.bashrc` e.g.

       `export SMTP_USER="username"`<br>
       `export SMTP_PASSWORD="password"`

  - Call the `sendmail.py` script with the full path to the config file as the 1st parameter and files to attach as subsequent parameters
    - `python3 sendmail.py ~/email/config.json file1.txt file2.txt`

## Setting up a Rails environment in Webfaction

 - Use Webfaction control panel(or api) to create a hello_world rails application.

 - Set the environment variables in Travis with the application folder name from Webfaction (see `dfbrails-vars.txt`).

 - Run build in Travis (or push a commit).

 - Goto the URL that was set up in Webfaction.

 - See `webfaction-rails-deploy.sh` for more details.

 - Use these commands from `~/webapps/<application-name>/` folder to run Rails related commands in Webfaction.
    ```
     export PATH=$PWD/bin:$PATH
     export GEM_HOME=$PWD/gems
     export RUBYLIB=$PWD/lib
     ```
