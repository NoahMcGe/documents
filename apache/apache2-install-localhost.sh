#!/bin/bash
# make sure you are in the same folder as localhost.conf
# chmod a+x apache2-install-localhost.sh
# run this script as sudo
# sudo ./apache2-install-localhost.sh
cp -f localhost.conf /etc/apache2/sites-available/;
cd /etc/apache2/sites-enabled/;
rm *.conf;
cd /etc/apache2/sites-available/;
a2ensite localhost.conf;
systemctl reload apache2;
