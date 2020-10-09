QMark : A Question Bank
--------------------------------------------------------------------------------
Course Project for Software Lab, CS699, Autumn 2019.

================================================================================
Team Name: TTFKAH
(formerly known as: The Team Formerly Known as Honorificabilitudinitatibus)
--------------------------------------------------------------------------------
Members:
    19305R003 : Sourab Jha
    193050024 : Devesh Ratna Singh
    193050076 : Zahid Wakeel

================================================================================
Repository link: https://github.com/hundredrab/QuestionBank
--------------------------------------------------------------------------------

INSTALLATION:

Requires virtualenv, python3.

    # Create a virtualenv
    sudo apt install virtualenv

    # Clone the repository from github
    git clone git@github.com:hundredrab/QuestionBank.git
    # Alternatively:
    # git clone https://github.com/hundredrab/QuestionBank

    cd QuestionBank/source

    # Create and source a new virtualenv
    virtualenv -p python3 env
    source env/bin/activate

    # Set up the environment
    pip install -r requirements.txt

    # Apply the migrations and start the development server
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

More details in the manual in docs folder.

================================================================================
MOTIVATION:

Tests are conducted to assess student's knowledge in a subject, grading them,
to give admission to higher education, placements, scholarships, etc. Hence, a
question paper must be set in a way that can measure the change in the level of
students' knowledge in a particular subject. Therefore, a good amount of care
and caution is necessary for setting question papers. The types of question
papers differ with the objective of the examination.

The process of setting a new question paper for an examination could be
cumbersome and tedious when one has to dig through old archives and comply with
the guidelines at the same time. A centralized, one-size-fits-all approach to
collaborative setting of papers either do not exist or are not intuitive
enough to be popular.

One has to keep in mind the difficulty level of each question, check questions
against previous papers, and still cover the various topics or skills that need
to be assessed. This mental overhead hampers setting up quality papers.

An aspirant usually covers her syllabi in a topic-wise fashion, wherein
applications of multiple topics or skills come in later than application of
individual topics. However, question banks usually do not account for this
distinction between topics covered and not covered. Thus, a practice session
tailored for individual needs is not trivially set up.

================================================================================
CONTRIBUTIONS:

Sourab: Schema design, User Interfaces
Devesh: Views, and internal logic
Zahid Wakeel: Documentation and Landing page

================================================================================
