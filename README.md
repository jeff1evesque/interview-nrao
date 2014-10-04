interview-nrao
=====================
I had an interview with [NRAO](http://www.nrao.edu/) (National Radio Astronomy Observatory) for a *Software Engineer II* position, and was given a coding exercise to calculate the amount of time spent performing observations. This code was written in Python, and was emphasized to be object oriented code.

###Definition

###Overview

##Configuration

###GIT
Fork this project in your GitHub account, then clone your repository:

```
cd /var/www/html/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/interview-nrao.git interview-nrao
```

Then, add the Remote Upstream, this way we can pull any merged pull-requests:

```
cd /var/www/html/interview-nrao/
git remote add upstream https://github.com/[YOUR-USERNAME]/interview-nrao.git
```

###File Permission
Change the file permission for the entire project by issuing the command:

```
cd /var/www/html/
sudo chown -R jeffrey:sudo interview-nrao
```

**Note:** change 'jeffrey' to the user account YOU use.
