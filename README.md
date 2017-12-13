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

## SSL Certificates

#### Install letsencrypt-webfaction
Use the library https://github.com/will-in-wi/letsencrypt-webfaction to setup up SSL keys. Install using the instructions for **System Ruby** to install the necessary gems and setup up a command alias in `~/.bashrc`.

#### Setup up config and run the script
See the example configuration file in this repo and use as `letsencrypt-webfaction --config ~/le_config/example-letsencrypt-config.yml.`.

When the command is being run a key file is placed in a public folder being served by the domain. Lets Encrypt needs to be able to access that key using HTTP, to prove that you are responsible for the domain. So make sure the initial creation of the certificate is carried out before routing all HTTP calls to HTTPS (see below).

#### Reroute all HTTP to HTTPS
Add the domain(unsecured) to the website **https_redirect** in Webfaction control panel. This will simply swap the http to https of any request that is received and redirect.

#### Change the website to HTTPS
Change the website to HTTPS (Secure) in the Webfaction UI, select the newly created certificate from the list. Make sure any domains for the website are also added to the redirect website.

#### Setup a cron job
The certifciate is valid for 3 months and then must be renewed. This can be carried out periodically using a cron job.
```shell
0 2 1 */2 * . $HOME/.bashrc; letsencrypt_webfaction --config /home/ukfit/le_config/mydomain_org.config.yml
```

## Debugging cronjobs
There is a cron running that exports it's environment to a file `* * * * * /usr/bin/env > $HOME/.cron-env`. So it's possible to test backup scripts in the same environment using ```env - `cat ~/.cron-env` bash example-script.sh```. Prefixing cron jobs with `. $HOME/.bashrc;` or `source $HOME/.bashrc;` should create a similar environment to the Webfaction shell.

## Using Rails commands in Webfaction

 - Use these commands from `~/webapps/<application-name>/` folder to run Rails related commands in Webfaction.
    ```shell
     export PATH=$PWD/bin:$PATH
     export GEM_HOME=$PWD/gems
     export RUBYLIB=$PWD/lib
     ```
