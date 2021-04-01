# politicsbot

A bot to watch the ads.

## Getting started

First install the dependencies : `pip3 install -r requirements`.

#### Linux

Then, install the shitty geckodriver : 
* `wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`
* `cd /tmp && tar -zxvf geckodriver.tar.gz && chmod +x geckodriver`
* `sudo mv geckodriver /usr/local/bin`

#### Windows

Download and install : https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-win64.zip

Finally copy the `.env.example` file to `.env` and edit the variables to reflect your needs.

## Coming soon

- Windows executable for no0bz
