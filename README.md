# politicsbot

A bot to watch the ads on Politics&War

## Getting started

First install the dependencies : `pip3 install -r requirements`.

Then, install the shitty geckodriver : 
* `wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`
* `cd /tmp && tar -zxvf geckodriver.tar.gz && chmod +x geckodriver`
* `sudo mv geckodriver /usr/local/bin`

Finally copy the `.env.example` file to `.env` and edit the variables to reflect your needs.
