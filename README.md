interview-nrao
=====================
I had an interview with the [NRAO](http://www.nrao.edu/) (National Radio Astronomy Observatory) for a *Software Engineer II* position, and was given a coding exercise to calculate the amount of time spent performing astronomical observations. This exercise was written in [Python](http://en.wikipedia.org/wiki/Python_(programming_language)), and emphasized to be [object oriented](http://en.wikipedia.org/wiki/Object-oriented_programming).

###Definition

Azimuth: is the angular distance along the horizon to the location of the object.  By convention, *azimuth* is measured from north towards the east along the horizon.

Elevation: sometimes called *altitude*, is the distance of an object appears to be above the horizon.  The angle is measured up from the closest point on the horizon.

- http://astrosun2.astro.cornell.edu/academics/courses/astro201/alt_az.htm

Flux density:  is a non-SI unit (jansky, or Jy) of spectral flux density.  One jansky is equivalent to  10−26 watts per square meter per hertz.  It was created for and is still most frequently used in referenceto electromagnetic energy, especially in the context of radio astronomy.The brightest astronomical radio sources have flux densities of the order of one to one hundred janskys.Note: The Sun at 10 GHz has 4,000,000 Jansky (JY).

**Note:** The Sun *at 10 GHz* has *4,000,000* Jansky (JY).

- http://en.wikipedia.org/wiki/Jansky

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
