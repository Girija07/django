=====
Usage
=====

To use django_private_chat3 in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_private_chat3.apps.DjangoPrivateChat3Config',
        ...
    )

Add django_private_chat3's URL patterns:

.. code-block:: python

    from django_private_chat3 import urls as django_private_chat3_urls


    urlpatterns = [
        ...
        url(r'^', include(django_private_chat3_urls)),
        ...
    ]
