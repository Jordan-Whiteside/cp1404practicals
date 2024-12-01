# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

My estimates for my practical tasks were fairly accurate in the sense that they were with 20 minutes of my estimated time.
Except for the wimbledon task which took me an extra 1 hour and 7 minutes than my expected time of 1 hour.

### How did your estimate accuracy improve or change during the course of the subject?

My estimate accuracy definitely changed after the wimbledon because on that task I definitely overestimated my programing ability.
So instead I always overestimated the time it would take than what I initially thought. This turned out good because as I said 
above my estimates would then always be within 20 minutes of actual time

### What did you learn from doing these estimates?

I learned that it takes long than you would initially think ot do a task.

## Code Reviews

### What have you learned from being reviewed by other people?

I have learned that I miss doctrings sometimes but I am getting better at just adding them straight away into my code.

### What have you learned from doing code reviews of other people?

I have learning that I really like doing code reviews. It gives me a chance to review what I know about coding and hopefully
help someone else out too. Doing code reviews has made me realise that I really like finding things different from what it should be.
Now whether this is a good or bad thing I don't know yet but either way code reviews has help me become a better programmer.

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

[Good Code Review 1](https://github.com/jc972214/cp1404practicals/pull/2)

### Explanation

This was my first code review that I did, but it was good for a couple of reasons.
First, all my messages were in a 'nice' tone where I hopefully moved him to consider other ways to do things.
It also helped me better understand why variable naming is so important and how bad variables names can make you think one thing but its actually another.


It was also a good review because one line was from the solution "print(", ".join(country for country in sorted(countries)))" 
which I asked if it could be done better like this "print(", ".join(sorted(countries))" instead. It helped me not just blindly follow solutions
and to think for myself and ask if it should be this way.

### Good Code Review 2

[Good Code Review 2](https://github.com/Moggie269/cp1404practicals/pull/3)

### Explanation

This code review was about classes which was a brand new concept for me so it was good to review someone's code to see if I understood classes
Again in this review I used language that tried to steer them in the right direction for example "Did you consider what self.get_age() >= 50 returns to the if statement? Maybe try it out in the python console?"
This one was also a good review because after the code, but I also noticed his commit messages were a bit ambiguous, so I gave him some suggestions on what he could write instead in the overall comment.
There was another part where he used enumerate but added +1 to every i value. This made me remember that the function can change the start index as an extra parameter like this enumerate(value, start_index).
So for that I suggested that they check what the enumerate function can do so he doesn't have to +1 to every i

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

I really like the practicals overall. I don't have any suggestions for change.

### What did you do really well for practicals in this subject?

I did really well in most areas. Docstrings, variable names and some of my coding patterns can be improved.
However, what I did really well was getting them done before the due date so that it gave me time to submit my code review and receive a code review before the due date
