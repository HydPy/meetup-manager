# Project Architecture

The main focus of the first version will be to integrate social media handling abilities to the app. We will have a basic event structure. Each event will have multiple speakers and a Venue. For each event we need to manage multiple social media platforms. So there will be 2 modules - `event` and `social`

Here is a probable project directory structure

```
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

### Autofill feature
The Autofill feature will support the auto generation of posts in various platfroms from the content in meetup.com. The user has to enter the text in the meetup.com textbox and when the user clicks autofill it will populate the content in other textboxes with some added intelligence, e.g. Truncating content for Twitter to 150 characters, making inline links bulleted at the end for mailing lists. The Autofill features will be a JS functionality which will happen in the client side. The user can then tweak the posts instead of manually filling each and every post.

**Urls**
```
/events             - Event listing page
/events/<id>        - Event details
/events/<id>/notify - Create social media posts
```

## Social Module

The social module is the one that will actually create all the social media posts by calling the social media APIs. It will act as a wrapper for the social media APIs and act as a middleman to invoke the APIs. When a post is created successfully it will store the necessary details of the post in the DB. The module will have the social media models for each platform.

It will use `django-rest-framework` to expose rest urls for making the social media requests. To keep separation of concern between each social media API we will utilising Viewsets from DRF which will be organised in separate files under `views` module. This module will only serve as the API for making the posts. So it will not have any templates.

**Urls**
```
# Meetup.com
/meetup - [POST] Create a meetup.com event
/meetup/<id> - [PATCH] Update a event in meetup.com
/meetup/<id>/comment - [POST] - Create a comment
/meetup/<id>/email - [POST] - Send email to subscribers

# Mailing list
/email - [POST] Send email to mailing list
```
