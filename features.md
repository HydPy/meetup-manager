# Initial Features

The project will have a simple Django admin interface. The organizer can login to the admin dashboard and add the value in the Data Models. There will be some simple pages to enable the automation we wan

## Social Media Integration
- Add Social platform routes for creating posts
    1. meetup.com - This is the primary platform where we post the meetup event. Use the meetup api to create/update an event, post update to subscribed users of the group, add comment to a event
    2. Facebook - Use Facebook api to create a post in Facebook, add comment to a post
    3. Twitter- Use Twitter api to create a tweet, mention a tweet and post                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ook api to make a post in Facebook
    4. LinkdIn - Use LinkedIn api to create a post in LinkedIn, add comment to a post
    5. mailing list - Send email to mailing list of the community
    6. Telegram - Post a message in Telegram group
- Add a simple form to connect and post the events in different platforms

## Venue Directory
Add a view to list all the Venues and contacts. Venue details can be added in the Django Admin by the Organiser

## Speaker Directory
- Create a simple form that can be used by speakers to enter their details
- Add a view to parse a GitHub issue and add the CFP details to Speaker details

# Extended Features
- Compose a event description by reading GitHub Issues and Poster uploaded to GitHub repo
- Create Draft message
- Create a workflow for peer review of notifications to be sent out in social media
- Automate a way to upload slides/demo code from Speakers
- Archive data from meetups using meetup api
- Generate a report of past meetups - We can use this statistics in community presentations
- Create backend end points for generating views for Community website
    - Listing of the meetups
    - Past Speakers of meetups
    - Listing of Venue partners
