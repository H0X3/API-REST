Dependencies
------------
- click==8.0.3
- colorama==0.4.4
- Flask==2.0.2
- itsdangerous==2.0.1
- Jinja2==3.0.2
- MarkupSafe==2.0.1
- Werkzeug==2.0.2

Steps
-----------
1.  Create virtual environment::

        python3 -m venv ./venv
        source ./venv/bin/activate

2.  Install requirements::

        make requirements

3.  Run project::

        make run

4.  GET API message

        open http://localhost:5000

5.  POST API list send json

        http://localhost:5000/api/get_content
