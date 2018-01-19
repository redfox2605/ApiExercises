# Data Engineer, take home test

Thank you for considering the Data Engineer position at GetYourGuide! We’ve
designed this take-home test to gather more information about your experience
and get a sense of how you approach problems we care about. 

You have three days to complete the assignment. It is due at 5pm on the third
day after receiving the assignment. Feel free to send questions directly to
mathieu.bastian@getyourguide.com if anything is unclear. 

N.B. Please acknowledge the receipt of the email.

Please record the time it takes you to complete the assignments. This is not an
evaluation criteria but just something we like to know so we can make sure our
take-home test aren’t neither too long nor too short.

## Data Product Code

For this exercise, we assume a shell bash (or bash like) environment, with
access to Git, Python, Curl and Make.

The app (app.py) included in this bundle is a service, which the
implementation is too simple to keep up with the expected growth of upcoming
years. We expect the traffic to double year-on-year, as well as the data served by 
the service. We’d like you to update the implementation, so that it will remain
stable for the next three years. Requirements are that it should serve at least 8 
times as many requests per second on a data set 8 times bigger than the current
dataset.

To get the dataset to work on, please run this command

    curl -w '\n' -s "https://www.getyourguide.com/-t62214/reviews.json?&count=50&page=[0-50]&rating=0&type=&sortBy=&direction=&remove=false" >> data.json

With the file `data.json` in place, please take a look at the [README](README.md)
included in the project. It explains how to run the service.

### Assignment

The improved implementation, should have these characteristics.

- It’s 8 times faster than the existing implementation, the comparison is based
  on the loadtest included in the project. 
- It must remain 8 times faster, when given a dataset 8 times the size of the
  current example.

It's perfectly fine to either improve the existing code base or rebuild it from
scratch in a difference programming language and/or framework. As long as the
HTTP API remain the same, and that ```make run``` will run the application on a
Linux or Mac OS X (in recent versions). 

## Data Product Design

In this exercise we aim to create a data product that helps GetYourGuide create
a personalized user experience. We’ll call this project the Visitor State
Machine. The goal is to categorize visitors into well-defined states (e.g. new
visitor, bounced, recent purchase, lapsed etc.) based on their behavior so the
product can adapt itself in real-time.

For instance, if the visitor has recently purchased an activity and comes back
we may want to put a higher emphasis on recommendations (e.g. here are a set of
other activities in your location) than activity discovery. Another example
would be to show a little “Need help?” prompt if the visitor came multiple
times recently but without purchases.

The states are based on the user’s behavior and time. Here are the states we
want to support:

- New Visitor: The default state for a visitor we’ve never seen.
- Bounced: A visitor that came and bounced (i.e. left the website or application right away). We consider a bounce state when the visitor hasn’t done any actions within the first 24h of arriving to the site.
- Active visitor: Had at least one activity in the last week.
- Lapsed visitor: Was an active visitor but didn’t have activity in the last 7 days.
- Recent purchase: Had a purchase in the last 48 hours.

A visitor is a user with a unique visitor identifier (visitor\_id). The unique
identifier persists in the user’s cookie so a user can be identified across
sessions.

### Assignment

- Design a solution that solves this problem and explain your choices. Imagine
  a scenario where you are the technical leader of this project and want to
  present to your colleagues the technical choices you’ve made. You can choose to
  write into something like Google Doc or build a presentation into something
  like Google Slide or Powerpoint.
- Don’t code! This assignment is about design and architecture, not coding.
- Do not hesitate to also discuss solutions you’ve thought about but finally
  dismissed.

### Deliverables

Consider the following deliverables and make sure your architecture design is
capable of supporting them.

- The ability to call the Visitor State Machine service from our backend and
  receive the “state” the visitor is in.
- A system that “refreshes” the state as quickly as possible. That said,
  because the state are only used for personalization we allow some delays.
- The system should scale horizontally so we can add additional resources
  without redesigning it.

#### Notes

- You can use any tools you want (RDBMS, NoSQL, Hadoop, Lucene, Spark etc.) but
  justify why they make sense in your architecture. If you’re not sure about
  other technologies do it in something you’re familiar with. There are many
  valid answers to this problem so don’t worry.
- Keep in mind your team has limited resources.

## Returning the solutions

Please include all changes in the project folder, and return is as one 
zip, tar, tar/gzip or similar. 


_Best of luck!_

