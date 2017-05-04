# unify-challenge

## Summary

Overall, this challenge was a humbling experience. I've been focusing my studies so much
on algorithms and data structures with Python over the couple of months that I haven't
actually been practicing my Ruby skills as much as I should. Because of this, as I tried
to work on this assignment, I found myself challenged by parts that I believed would be
simple to implement.

Rather than waste any more time trying to force myself to refresh my Rails skills while
simultaneously solving the problems, I decided the best use of my time was to simply begin
again using a Python script.

After doing so, I was able to very quickly write a script that could make a request to the
random.org server to get an array of numbers to use for the various assignments. The first
problem I came across was that random.org limits you to 10,000 numbers per request, which
meant I needed to either a) pseudo-random the numbers I needed after the 10,000th, or b)
generate a second request once I ran out of numbers. I decided to go with option b, mainly
because that appeared to be more in the spirit of the assignment.

Once I had the requests down, I needed to actually turn those numbers into useful
information, and then into a color. Luckily, random.org lets you set a minimum and a
maximum for your requests, so I decided I could use HSL to quickly get random colors from
an array of numbers between 0 and 359. Easy enough. The problem now was how to actually
draw those colors onto some sort of canvas.

One tool I've seen before for a similar graphical implementation of Python is called pygame.
Although I myself have never used pygame, I decided I would try it out real quick (<15
minutes was my limit) to see if it would do what I needed it to do.

After about 5 minutes of reading through the docs, I realized it would, in fact, do what I was
trying to do, although I would have to refactor the code a bit to work with pygame. Luckily,
this was not too difficult, and I was able to quickly get pygame running. Unfortunately,
pygame's HSL implementation is a bit lacking, so I refactored the code a bit to serve up
values from 0-255, and then to use 3 values at a time instead of only using the one value for
HSL.


## Instructions

Unfortunately, at this time, I have not yet completed the script, but invite you to take a look
at where I have gotten over the last hour or so trying to implement pygame.

Thank you for the opportunity. I wish you all the best!
