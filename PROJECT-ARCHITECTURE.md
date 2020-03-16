# Project Architecture

The main focus of the first version will be to integrate social media handling abilities to the app. We will have a basic event structure. Each event will have multiple speakers and a Venue. For each event we need to manage multiple social media platforms. So there will be 2 modules - `event` and `social`

Here is a probable project directory structure

``` Directory structure
meetup-manager
├── meetup-manager
│   ├── meetup-manager
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── event
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── static
│   │   │   └── event
│   │   │       └── hydpy_icon.png
│   │   ├── templates
│   │   │   └── events
│   │   │       └── index.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── social
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views
│   │       ├── __init__.py
│   │       ├── meetup_viewset.py
│   │       ├── twitter_viewset.py
│   │       └── mailer_viewset.py
│   └── manage.py
├── LICENSE
└── README.md
```

## Event Module

The event module will contain the Event, Venue and Speaker models. It will have 3 pages - Event lisiting page, Event details that will have a list of all the social media posts made for the event and the event notify page that will be used to create the posts. The notify page and list of social media posts will only be visible to the organiser.

The mockup of the noify page is attached. It will use Ajax requests to make the various posts from the page.

There will be no Venue or Speaker page in the initial version. It will be available in django admin where the organise can add them.

### Autofill feature

The Autofill feature will support the auto generation of posts in various platfroms from the content in meetup.com. The user has to enter the text in the meetup.com textbox and when the user clicks autofill it will populate the content in other textboxes with some added intelligence, e.g. Truncating content for Twitter to 150 characters, making inline links bulleted at the end for mailing lists. The Autofill features will be a JS functionality which will happen in the client side. The user can then tweak the posts instead of manually filling each and every post.

#### URLs

``` Routes
/events             - Event listing page
/events/<id>        - Event details
/events/<id>/notify - Create social media posts
```

## Social Module

The social module is the one that will actually create all the social media posts by calling the social media APIs. It will act as a wrapper for the social media APIs and act as a middleman to invoke the APIs. When a post is created successfully it will store the necessary details of the post in the DB. The module will have the social media models for each platform.

It will use `django-rest-framework` to expose rest urls for making the social media requests. To keep separation of concern between each social media API we will utilising Viewsets from DRF which will be organised in separate files under `views` module. This module will only serve as the API for making the posts. So it will not have any templates.

### SM URLs

``` Routes
# Meetup.com
/meetup - [POST] Create a meetup.com event
/meetup/<id> - [PATCH] Update a event in meetup.com
/meetup/<id>/comment - [POST] - Create a comment
/meetup/<id>/email - [POST] - Send email to subscribers

# Mailing list
/email - [POST] Send email to mailing list
```

## GitHub Issue Parser

The idea is to write a simple parser which will go over all the `eligible[1]` GitHub issues, i.e., the talk / workshop proposals
and generate the content for the Meetup.

Control Flow:

1. Organizer(s) goes over the GitHub issues and add labels to the issues scheduled with a label for the date for which the talk is scheduled for.
    (Same as what's being done today)

1. From the Meetup Manager home page, we'll have 2 options.
    - Create a Placeholder event
    - Create a Meetup event

1. For updating the final details, on the Meetup Manager event page, the user will provide the date value of the Label to pick the talks for.
1. This parser will then fetch the issues from GitHub with the `scheduled` label as well as the given `date` label - eligible proposals[1]
1. Since all the GitHub issues will be following the template format, it'll be easier to parse the title, abstract and speaker details.
1. It'll then store this information in the meetup manager `talk` table with a FK association to `id` in event table
1. This will be an on-demand job from the UI via API

## Dockerizing the Application

The application should be dockerized from the beginning and preference should be for containerized development to reduce the amount of
issues with multiple devs collaborating on same piece

## Users

We should create individual user accounts for auditing purposes to later check who made what changes just in case of any anomalies.

## Notifications Scheduler

Integrate Celery workers into the application for scheduling reminders about the event, 4 days to the event, 2 days to the event, etc.

Similarly to send post event feedback collection forms so that this project's scope can be extended to Conferences as well.

## Notification Channels

There will be multiple channels, i.e., Facebook, Twitter, LinkedIn, Instagram, WhatsApp, Telegram, Email, etc.

The idea is to have a common Service layer acting as the interface for these channels.

The Application will be integrated as per the APIs defined in this Service layer and individual channel implementations will have the details
about establishing connection and event related operations.

This would make it easier to Plug N Play newer channels

We'll try to add more details to this, maybe some pseudo code as well for illustration.
