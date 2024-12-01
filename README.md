Django Private Chat3
======================

![https://badge.fury.io/py/django_private_chat3](https://badge.fury.io/py/django_private_chat3.svg)

![https://github.com/Bearle/django_private_chat3/actions](https://github.com/millerf/django_private_chat3/actions/workflows/test.yml/badge.svg?branch=master)

![https://codecov.io/gh/millerf/django_private_chat3](https://codecov.io/gh/millerf/django_private_chat3/branch/master/graph/badge.svg)

New and improved  https://github.com/Bearle/django-private-chat2

Chat app for Django, powered by Django Channels, Websockets & Asyncio

![screenshot](https://github.com/millerf/django_private_chat3/blob/master/screenshots/screen.jpg?raw=true)

Documentation
-------------

The full documentation **will be** at <https://django-private-chat2.readthedocs.io>.

Quickstart
----------

Install django_private_chat2:

    pip install django_private_chat3

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'django_private_chat3.apps.DjangoPrivateChat2Config',
    ...
)
```

Add django_private_chat2's URL patterns:

```python
from django.urls import re_path, include


urlpatterns = [
    ...
    re_path(r'', include('django_private_chat3.urls', namespace='django_private_chat3')),
    ...
]
```

Add django_private_chat2's websocket URLs to your `asgi.py`:
```python

django_asgi_app = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django_private_chat3 import urls
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(urls.websocket_urlpatterns)
    ),
})

```


**Important:**

django_private_chat3 doesn't provide any endpoint to fetch users (required to start new chat, for example)
It's up to you to do so. The example app does it in `urls.py` so feel free to copy the handler from there if you wish.

Support
--------

It's important for us to have `django_private_chat3` thoroughly tested.

Using github actions, we're able to have `django_private_chat3` tested against python3.6, python3.7, python3.8, python3.9, python3.10 with Django 3.0, Django 3.1,  Django 3.2, Django 4.0

You can view the builds here:

https://github.com/millerf/django_private_chat2/actions

The builds are composed of officially supported Django & Python combinations.

Please file an issue if you have any problems with any combination of the above. 


Features
--------

__Django-related__

-✅ Fully-functional example app

-✅ Uses Django admin

-✅ Supports pluggable User model (and accounts for non-integer primary keys, too)

-✅ Doesn't require Django Rest Framework (views are based off django.views.generic)

-✅ Configurable via settings

-✅ Fully translatable 

-✅ Uses Django storage system & FileField for file uploads (swappable)


__Functionality-related__

-✅ Soft deletable messages

-✅ Read/unread messages

-✅ Random id (send message first, write to database later)

-✅ Supports text & file messages

-✅ Gracefully handles errors

-✅ Support 'typing' statuses

-✅ Upload the file first, send the message later (async uploads) - potential for file ref re-use later

... and more


Example app frontend features
-----------------------------

1. Auto reconnected websocket
2. Toasts about errors & events
3. Send text messages
4. Search for users
5. Create new chat with another user
6. Online/offline status
7. Realtime messaging via websocket
8. Last message
9. Auto-avatar (identicon) based on user id
10. Connection status display
11. `Typing...` status
12. Message delivery status (sent, received, waiting, etc.)
13. Message history
14. Persistent chat list
15. Read / unread messages
16. Unread messages counters (updates when new messages are received)
17. Send file messages (upload them to server)

TODO 
----

Frontend (example app) & backend

1. Pagination support on frontend
    1. For messages 
    2. For dialogs
2. Example app only - user list
    1. ✅ Endpoint
    2. ✅ UI
3. ✅ New dialog support
4. Online's fetching on initial load
5. Last message
    1. ✅ In fetch
    2. ✅ In new dialog
    3. ✅ On arriving message
6. ✅ Read / unread/ unread count
7. Last seen
8. Send photo
9. ✅ Send file
10. Reply to message
11. Delete message
12. Forward message
13. Search for dialog (username)
    1. ✅ Frontend (local)
    2. ~~Server based~~ - won't do, out of the scope of the project
14. ✅ Fake data generator (to test & bench) - done via factories in tests
15. Cache dialogs (get_groups_to_add) - ?
16. Move views to async views - ?
17. Add some sounds
    1. New message
    2. New dialog
    3. Sent message received db_id
18. Optimize /messages/ endpoint
19. ✅Some tests
20. Full test coverage
21. Migration from v1 guide
22. Documentation
23. self-messaging (Saved messages)

Running Tests
-------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Development commands
--------------------

    pip install -r requirements_dev.txt
    invoke -l

Credits
-------

Tools used in rendering this package:

-   [Cookiecutter](https://github.com/audreyr/cookiecutter)
-   [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)

Paid support
------------

If you wish to have professional help from the authors of django_private_chat3, or simply hire Django experts to solve a particular problem,
please contact us via email `fab` **at** `millerf.com`
