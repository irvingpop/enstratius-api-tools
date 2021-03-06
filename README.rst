Documentation
-------------

Please visit the `enstratius API tools <http://api-tools.enstratius.com>`_ documentation
site.

Dependencies
------------

Dependencies should be automagically satisfied. But if you need to fetch them manually:


.. code-block:: bash

   sudo easy_install requests
   sudo easy_install argparse
   sudo easy_install mixcoatl
   sudo easy_install prettytable


Environment Variables
---------------------

Enstratius API tools work with `Enstratius REST API.
<https://www.enstratius.com/page/1/API-Specifications.jsp>`_ Since the tools are dependent
on `mixcoatl <https://github.com/enstratus/mixcoatl>`_, you have to set environment
variables.

.. code-block:: bash

        export ES_ACCESS_KEY=abcmyaccesskeycba
        export ES_SECRET_KEY=12345mysecretkey67890
        unset ES_ENDPOINT

If you are not in Enstratius SaaS environment, you also need to configure ES_ENDPOINT. For
instance, you need to set ES_ENDPOINT as below in development environment.

.. code-block:: bash

        export ES_ENDPOINT=http://dev.api.enstratius.com:15000/api/enstratus/2012-06-15

Common modules
--------------

``esid.py``
~~~~~~~~~~~

ID translation in Enstratius API.

``resource_filter.py``
~~~~~~~~~~~~~~~~~~~~~~

Useful when you search particular resources such as servers from a list of resources.
