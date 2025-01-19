
<h1>Spy Cat Agency API</h1>
<p>
  This is a Django REST API project for managing spy cats, missions, and targets.
  The project demonstrates CRUD operations, integration with an external API (<em>TheCatAPI</em>), 
  and usage of Django Rest Framework (DRF). It also includes business logic such as 
  mission completion rules, assignment constraints, and more. <a href="https://develops.notion.site/Python-engineer-test-assessment-the-Spy-Cat-Agency-1220fe54b07b80e78dd3c411e1309210#03da2017db7e40688d00bbf0e3dee8a2" target="_blank">
    Task link</a>.
</p>

<hr>

<h2>1. Requirements & <code>requirements.txt</code></h2>

<p>
  Below are the core requirements. You can install them with 
  <code>pip install -r requirements.txt</code>. 
  Make sure you have a <strong>virtual environment</strong> activated if you wish to keep dependencies isolated.
</p>

<pre><code># requirements.txt

Django==4.2.0
djangorestframework==3.14.0
psycopg2-binary==2.9.6
requests==2.31.0

# For API documentation (optional)
drf-yasg==1.21.5
</code></pre>

<p>
  You might have slightly different versions depending on your environment, 
  but these are tested with Python 3.11. 
  If you are using a different Python version (3.9+ recommended), it should also work fine.
</p>

<hr>

<h2>2. Project Setup & Database Configuration</h2>

<ol>
  <li><strong>Clone the repository from GitHub</strong>.
    <br />
    <code>git clone https://github.com/boghtml/spy-cat-agency.git</code>
  </li>
  <li><strong>Create a virtual environment</strong> (optional but recommended):
    <pre><code>python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
</code></pre>
  </li>
  <li><strong>Install dependencies</strong> using:
    <pre><code>pip install -r requirements.txt
</code></pre>
  </li>
  <li>
    <strong>Configure PostgreSQL</strong> (or another DB) in <code>settings.py</code>:
    <pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spycat_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
</code></pre>
    Make sure you have created the database <code>spycat_db</code> (or whichever name) 
    and have a matching user/password.
  </li>
  <li>
    <strong>Run migrations</strong> to create the necessary tables:
    <pre><code>python manage.py makemigrations
python manage.py migrate
</code></pre>
  </li>
  <li>
    <strong>Create a superuser</strong> (optional, for Django Admin):
    <pre><code>python manage.py createsuperuser
</code></pre>
  </li>
  <li>
    <strong>Start the development server</strong>:
    <pre><code>python manage.py runserver
</code></pre>
    Then open <code>http://127.0.0.1:8000</code> in your browser.
  </li>
</ol>

<p>
  You can now access the API endpoints at <code>http://localhost:8000/api/</code>.
  Also, if you have added <code>drf-yasg</code> and configured URLs, you can open:
</p>
<ul>
  <li><strong>Swagger UI</strong>: <code>http://127.0.0.1:8000/swagger/</code></li>
  <li><strong>Redoc UI</strong>: <code>http://127.0.0.1:8000/redoc/</code></li>
</ul>

<hr>

<h2>3. Project Architecture</h2>
<p>
  The project follows a <strong>modular</strong> structure, separating functionality into 
  different Django <em>apps</em>:
</p>

<pre><code>spy_cat_agency/
│   ├── manage.py
│   ├── requirements.txt
│   ├── README.md
│   └── spy_cat_agency/   <-- Main Django settings + URLs
│        ├── __init__.py
│        ├── settings.py
│        ├── urls.py
│        ├── wsgi.py
│        └── asgi.py
│
│   └── apps/
│        ├── cats/
│        │    ├── models.py       (Cat model)
│        │    ├── serializers.py  (CatSerializer)
│        │    ├── views.py        (CatViewSet)
│        │    ├── urls.py         (routes for cats)
│        │    └── ...
│        ├── missions/
│        │    ├── models.py       (Mission model)
│        │    ├── serializers.py  (MissionSerializer)
│        │    ├── views.py        (MissionViewSet)
│        │    ├── urls.py         (routes for missions)
│        │    └── ...
│        └── targets/
│             ├── models.py       (Target model)
│             ├── serializers.py  (TargetSerializer)
│             ├── views.py        (TargetViewSet)
│             ├── urls.py         (routes for targets)
│             └── ...
</code></pre>

<ul>
  <li>
    <code>cats</code>: Manages all logic related to <strong>Cat</strong> objects 
    (creation, update, validation with TheCatAPI).
  </li>
  <li>
    <code>missions</code>: Manages <strong>Missions</strong>, including custom endpoints 
    to <em>mark as complete</em>, <em>assign a cat</em>, etc.
  </li>
  <li>
    <code>targets</code>: Manages <strong>Targets</strong> (the individual spying objectives),
    including rules about notes, completion status, etc.
  </li>
</ul>

<p>
  This separation <strong>makes the code more maintainable</strong> and 
  follows Django's recommended best practices. Each app has its own <em>models</em>, 
  <em>serializers</em>, <em>views</em>, and <em>urls</em>.
</p>

<hr>

<h2>4. Endpoints Overview (17 total)</h2>
<p>
  We have <strong>17 total endpoints</strong> across three resources (Cats, Missions, Targets),
  plus a couple of custom actions. All base paths are prefixed with <code>/api/</code>.
</p>

<h3>Cats (5 endpoints)</h3>
<ol>
  <li><code>GET /api/cats/</code> - List all cats</li>
  <li><code>POST /api/cats/</code> - Create a new cat (with breed validation)</li>
  <li><code>GET /api/cats/{id}/</code> - Retrieve a specific cat by ID</li>
  <li><code>PUT /api/cats/{id}/</code> or <code>PATCH /api/cats/{id}/</code> - Update an existing cat</li>
  <li><code>DELETE /api/cats/{id}/</code> - Remove a cat</li>
</ol>

<h3>Missions (7 endpoints)</h3>
<ol>
  <li><code>GET /api/missions/</code> - List all missions</li>
  <li><code>POST /api/missions/</code> - Create a mission <strong>with</strong> 1–3 targets</li>
  <li><code>GET /api/missions/{id}/</code> - Retrieve a mission + nested targets</li>
  <li><code>PUT /api/missions/{id}/</code> or <code>PATCH /api/missions/{id}/</code> - Update mission details</li>
  <li><code>DELETE /api/missions/{id}/</code> - Remove a mission <strong>only if complete</strong></li>
  <li>
    <code>PATCH /api/missions/{id}/mark-as-complete/</code> - 
    Custom action to force the mission to <em>complete</em>, also completes all targets
  </li>
  <li>
    <code>PATCH /api/missions/{id}/assign-cat/</code> - 
    Custom action to assign a cat to a mission 
    (only if the cat doesn’t have another <em>assigned</em> mission)
  </li>
</ol>

<h3>Targets (5 endpoints)</h3>
<p>
  If separate creation/updates of targets is allowed (in addition to nested creation under missions), 
  we have:
</p>
<ol>
  <li><code>GET /api/targets/</code> - List all targets</li>
  <li><code>POST /api/targets/</code> - Create a target (optional use-case)</li>
  <li><code>GET /api/targets/{id}/</code> - Retrieve a specific target</li>
  <li><code>PUT /api/targets/{id}/</code> or <code>PATCH /api/targets/{id}/</code> - Update target; 
  can mark status = <code>complete</code>, etc.</li>
  <li><code>DELETE /api/targets/{id}/</code> - Remove a target</li>
</ol>

<p>
  <em>Note</em>: In some setups, we might disable <strong>POST /api/targets/</strong> 
  if we only allow creation <em>inside</em> Missions. 
  But conceptually, it's still a potential endpoint.
</p>

<hr>

<h2>5. Postman Collection</h2>
<p>
  You can import the Postman collection from the link:
  <a href="https://educational-platform-7691.postman.co/workspace/Educational-Platform-Workspace~ce1508d2-7c2d-4b4e-8913-47b8a5cec381/collection/37235075-0a503a26-ba3b-40e4-91da-8e0b0902f3f7?action=share&creator=37235075" target="_blank">
    Spy Cat Agency - Postman Collection
  </a>.
</p>


![image](https://github.com/user-attachments/assets/d7afe29a-28c0-4dfa-b2a4-6f099079a17e)


<p>
  This collection contains sample requests for:
  <ul>
    <li>Creating & Updating Cats (with breed validation)</li>
    <li>Creating Missions + nested Targets</li>
    <li>Marking Missions as complete / Assigning cats</li>
    <li>Deleting Missions (only if complete)</li>
    <li>CRUD for Targets</li>
  </ul>
</p>

<hr>

<h2>6. Additional Notes</h2>
<ul>
  <li>
    <strong>TheCatAPI Validation:</strong> 
    When creating or updating a <em>Cat</em>, the <code>breed</code> field is validated against 
    <a href="https://api.thecatapi.com/v1/breeds">TheCatAPI</a>. 
    If the breed is invalid, you get a 400 or 422 error.
  </li>
  <li>
    <strong>Business Logic:</strong> 
    One cat can only have one assigned mission at a time 
    (<code>status='assigned'</code>), 
    and completing a mission automatically blocks any further notes modifications. 
    You can force-complete a mission with <code>/mark-as-complete</code>.
  </li>
  <li>
    <strong>Cleanup / Deletion:</strong> 
    Missions can only be deleted if they are already complete. 
    Deleting a mission cascades to delete its Targets as well.
  </li>
  <li>
    <strong>Swagger & Redoc Documentation</strong>: 
    If drf-yasg is installed and configured, 
    you can view <code>http://127.0.0.1:8000/swagger/</code> or <code>/redoc/</code>.
    This auto-generates an OpenAPI spec for all endpoints.
  </li>
</ul>

<hr>

<h2>7. Contact / Q&A</h2>
<p>
  If you have any questions, feel free to reach me at: 
  <a href="mailto:boghtml@gmail.com">boghtml@gmail.com</a>.
</p>
