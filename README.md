These are my Python responses to the CodingBat site's python coding excercises available at http://codingbat.com/.

This repo also includes a handy script for downloading all of your solutions from the coding bat website. To execute the script:

### Downloading Your Solutions

1. Get beautifulsoup via 'pip install beautifulsoup4' or 'easy_install beautifulsoup4'
2. Get the 'jsessionid' value from the cookie once you are authenticated to codingbat.com. This value is needed in order to get your specifice solutions.
3. With the value from step one, paste it as a variable to jsessionid in 'PullExcercises.py'.
4. Execute 'python PullExcercises.py' from a command line

This script is designed to work with the Python excercises.  Pull requests are welcome to make it work with the java excercises too.  Please be respectful of the codingbat.com server when running this script. Tested on a mac with OSX 10.8.4 and python 2.7.2.