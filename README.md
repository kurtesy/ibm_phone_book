# IBM Phone Book
## Team Principles
    - TDD.
    - Kanban.
    - Continuous delivery.
    - Continuous integration.
    - Squad service ownership.
    - Frequent delivery to production.

## Problem statement
    We would like you to develop a small piece of code to implement a simple HTTP service to represent a phone book.

## Acceptance criteria.
    - List all entries in the phone book.
    - Create a new entry to the phone book.
    - Remove an existing entry in the phone book.
    - Update an existing entry in the phone book.
    - Search for entries in the phone book by surname.A phone book entry must contain the following details:
        - Surname
        - Firstname
        - Phone number
        - Address (optional)

## Development setup:
    1. clone repo from 'https://github.com/kurtesy/ibm_phone_book/tree/develop'
        `git clone https://github.com/kurtesy/ibm_phone_book/tree/develop`
    2. Install Python 3.x in the system.
    3. Go to the project directory
        `cd ./ibm_phone_book/`
    4. Install python dependencies
        `pip install requirement.txt`
    5. Run `python server.py`
    6. Bravo!! your Phone Book api server is ready to serve you!

## Deployment process: [For ubuntu/linux environment]
    1. Install and setup docker in the production server
    2. Update Dockerfile as:
        `
        COPY ./requirements.txt /var/www/requirements.txt
        RUN pip install -r /var/www/requirements.txt
        `
    3. create start.sh
        #!/bin/bash
        app="docker.ibm_phone_book"
        docker build -t ${app} .
        docker run -d -p 56733:80 \
          --name=${app} \
          -v $PWD:/app ${app}
    4. Run start.sh to start the docker process
    5. Verify that your server is running using `docker ps`

## Sample API calls:
    Endpoint	HTTP Method	Sample Request
    /api/phonebook/	GET	http://127.0.0.1:5000/api/phonebook
    /api/phonebook/add	POST	http://127.0.0.1:5000/api/phonebook/add?sur_name="Suman"&first_name="H"&phone_number=4444444444
    /api/ phonebook/search/:surname	GET	http://127.0.0.1:5000/api/phonebook/search/Patel
    /api/phonebook/update/:surname,:firstname	PUT	http://127.0.0.1:5000/api/phonebook/update/abc/xyz/sur_name=Suman&first_name=H&phone_number=4444444444
    /api/phonebook/remove/:surname,:firstname	DELETE	http://127.0.0.1:5000/api/phonebook/remove/abc/xyz/
