es-api-tools
============

Philosophy
~~~~~~~~~~

See the `philosophy <https://enstratus.fogbugz.com/default.asp?W242>`_ from great master.

List of Tools
~~~~~~~~~~~~~

Servers
-------

+----------------------------+---------------------------------------------+
| Filename                   | Description                                 |
+============================+=============================================+
| es-list-servers.py         | List servers.                               |
+----------------------------+---------------------------------------------+
| es-create-server.py        | Create a new server from a machine image.(x)|
+----------------------------+---------------------------------------------+
| es-pause-server.py         | Pause a server.                             | 
+----------------------------+---------------------------------------------+
| es-terminate-server.py     | Terminate a server.                         |
+----------------------------+---------------------------------------------+

Volumes and Snapshots
---------------------

+----------------------------+---------------------------------------------+
| Filename                   | Description                                 |
+============================+=============================================+
| es-list-volumes.py         | List volumes.                               |
+----------------------------+---------------------------------------------+
| es-create-volume.py        | Create a new volume.                        |
+----------------------------+---------------------------------------------+
| es-delete-volume.py        | Delete a volume.(x)                         |
+----------------------------+---------------------------------------------+
| es-list-snapshots.py       | List snapshots.                             |
+----------------------------+---------------------------------------------+

Machine Images
--------------

+----------------------------+---------------------------------------------+
| Filename                   | Description                                 |
+============================+=============================================+
| es-list-machine-images.py  | List machine images.                        |
+----------------------------+---------------------------------------------+

Users and Groups
----------------

+----------------------------+---------------------------------------------+
| Filename                   | Description                                 |
+============================+=============================================+
| es-list-users.py           | List users.                                 |
+----------------------------+---------------------------------------------+
| es-list-groups.py          | List groups.                                |
+----------------------------+---------------------------------------------+

Etc
---

+----------------------------+---------------------------------------------+
| Filename                   | Description                                 |
+============================+=============================================+
| es-list-regions.py         | List regions.                               |
+----------------------------+---------------------------------------------+
| es-list-datacenters.py     | List datacenters.                           |
+----------------------------+---------------------------------------------+
| es-list-billing-codes.py   | List billing codes.                         |
+----------------------------+---------------------------------------------+
| es-list-jobs.py            | List status of jobs.                        |
+----------------------------+---------------------------------------------+

Common modules
~~~~~~~~~~~~~~

``esid.py``
-----------
ID translation in enStratus API.

``resource_filter.py``
----------------------
Useful when you search particular resources such as servers from a list of resources.

Dependencies
~~~~~~~~~~~~

To make the tools work, you have to install dependent modules. Currently, it works with the latest version of mixcoatl that is in Github repository, not in pypi.

.. code-block:: bash

        sudo pip install prettytable

        git clone https://someurl.to.mixcoatl/
        sudo python setup.py install

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

enStratus API tools work with `enStratus REST API. <https://www.enstratus.com/page/1/API-Specifications.jsp>`_ Since the tools are dependent on `mixcoatl <https://github.com/enStratus/mixcoatl>`_, you have to set environment variables.

.. code-block:: bash

        export ES_ACCESS_KEY=abcmyaccesskeycba
        export ES_SECRET_KEY=12345mysecretkey67890
        unset ES_ENDPOINT

If you are not in enStratus SaaS environment, you also need to configure ES_ENDPOINT. For instance, you need to set ES_ENDPOINT as below in development environment.

.. code-block:: bash

        export ES_ENDPOINT=http://dev.api.enstratus.com:15000/api/enstratus/2012-06-15
