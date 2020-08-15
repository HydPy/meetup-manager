# Meetup Manager

## Context

A lot of tasks and preparation involved before organising Community meetups are repetitive and can be automated using software.

One of the major tasks include making announcement to various social media platforms and mailing lists. Hence we need a good way to handle these announcements so that when the organiser makes an announcement it gets announced across various social media platforms.

We also need contacts of various speakers who are willing to present at the meetups. Many times it happens meetups fall short of speakers and we want to reach out to speakers in our contact for presenting in the meetup. Instead of finding all over we can use the past speakers list and shoot them an email.

For meetups we also need a list of Companies and PoCs whom we can contact for hosting the meetup. We can store this data in a central place for easy accessibility. This will enable the easy transfer of responsibilities between organisers of the meeup.

## Scope

The meetup manager aims to solve the problem of announcing meetup notifications in different platform from one place without having to know the credentials of each platforms. Additonally it will serve as a common location for getting data about speakers, venue and meetups.

## Purpose of the Project

The purpose of the project is to Automate most common tasks for meetup Organizers and also provide a Workflow for the tasks. Based on that here is a list of user stories which can be useful to describe various use cases.

### Social media Integration/Announcement system

The application will have an Admin dashboard where in if the Organiser creates an announcement it will be scheduled as an event in meetup.com and shared to all social media platforms (Facebook, Linkedin, Twitter, Telegram) and mailing list.

Before the event it can make announcements for opening Call for Proposals for the next meetup.

After the event if we want some updates to be posted in meetup.com or any other social media platform it will post a comment in the respective channels.

Further enhancements can be done to introduce a peer review workflow that will notify co-organizers to review the content before posting.

### Speaker Directory

When a speaker submits a proposal in the CFP platform it should be able to save the speaker contact and categorize them on their area of expertise for further usage as need be.

### Venue Directory

The organiser will be able to save the Venue and contact details of  a particular Venue for future meetups.

### Updating meetup resources to repository

Once the meetup is over we can automatically post the resources (slides, code repo) from CFP platform to the meetup repository in GitHub. (This is something new I came up with) Since we are using GitHub as our CFP platform we can use the GitHub API to achieve this. But for that we need to come up with a structured comment that we can use that for uploading resources.

## Future scope of the Project

1. Backend service for Community website - The meetup manager can serve as the backend of HydPy website. Currently the website is a static website which need to be updated manually. We can create some dynamic pages based on the data stored in the meetup manager. This can be

    - Listing of the meetups
    - Past Speakers of meetups
    - Listing of Venue partners
2. Creating Workflow for peer review of notifications posted on social media platforms

## Running the app locally

You need to have Docker installed to run the app locally

After docker is installed, run the command on the terminal:

```$ docker-compose up --build -d```

This command will build the docker image on your local system using the Dockerfile and other configuration specified.

And finally launch all services defined in the `docker-compose.yml` file, create its own network, etc.
