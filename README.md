<h1>Spy Cat Agency API</h1>

<p>
  This is a Django REST API project for managing spy cats, missions, and targets.
  The project demonstrates CRUD operations, integration with external APIs (TheCatAPI), 
  and usage of Django Rest Framework (DRF).
</p>

<hr>

<h2>1. Project Setup & Requirements</h2>
<ul>
  <li>Python 3.9+ (tested on 3.11)</li>
  <li>Django 3.2+ / 4.0+ (depending on your environment)</li>
  <li>Django Rest Framework</li>
  <li>PostgreSQL (or any other DB) + <code>psycopg2-binary</code></li>
  <li>Optional: <code>drf-yasg</code> for Swagger/Redoc docs</li>
</ul>

<p>Install dependencies:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h2>2. How to Run the Application</h2>
<ol>
  <li>Clone the repository from GitHub.</li>
  <li>Create a virtual environment (optional but recommended).</li>
  <li>Edit <code>settings.py</code> to configure database credentials.</li>
  <li>Run migrations:
    <pre><code>python manage.py makemigrations
python manage.py migrate
    </code></pre>
  </li>
  <li>Start the development server:
    <pre><code>python manage.py runserver
    </code></pre>
  </li>
  <li>Access the API via <code>http://localhost:8000/api/</code>.</li>
</ol>

<h2>3. Endpoints Overview</h2>
<p>
  For details on each endpoint and expected JSON structure, please refer to:
</p>
<ul>
  <li>Swagger UI: <code>http://127.0.0.1:8000/swagger/</code></li>
  <li>Redoc UI: <code>http://127.0.0.1:8000/redoc/</code></li>
  <li>Postman Collection: 
    <a href="https://educational-platform-7691.postman.co/workspace/Educational-Platform-Workspace~ce1508d2-7c2d-4b4e-8913-47b8a5cec381/collection/37235075-0a503a26-ba3b-40e4-91da-8e0b0902f3f7?action=share&creator=37235075">
      Click to Open
    </a>
  </li>
</ul>

<p>Key endpoints (short version):</p>
<ul>
  <li><strong>/api/cats/</strong> - CRUD for spy cats.</li>
  <li><strong>/api/missions/</strong> - CRUD for missions (nested creation of targets).</li>
  <li><strong>/api/targets/</strong> - CRUD for targets (if you allow separate creation).</li>
  <li><strong>/api/missions/{id}/mark-as-complete/</strong> - Force completing a mission, also completes all targets.</li>
  <li><strong>/api/missions/{id}/assign-cat/</strong> - Assign a cat to a mission (if the cat has no ongoing mission).</li>
</ul>

<h2>4. Postman Collection</h2>
<p>
  You can import the Postman collection from the link:
  <a href="https://educational-platform-7691.postman.co/workspace/Educational-Platform-Workspace~ce1508d2-7c2d-4b4e-8913-47b8a5cec381/collection/37235075-0a503a26-ba3b-40e4-91da-8e0b0902f3f7?action=share&creator=37235075" target="_blank">
    Spy Cat Agency - Postman Collection
  </a>.
</p>

<h2>5. Additional Notes</h2>
<ul>
  <li>
    <strong>TheCatAPI Validation:</strong> when creating or updating a <em>Cat</em>, 
    the <code>breed</code> field is validated against 
    <a href="https://api.thecatapi.com/v1/breeds">TheCatAPI</a>. 
    If the breed is invalid, you get a 400/422 error.
  </li>
  <li>
    <strong>Business Logic:</strong> 
    one cat can only have one assigned mission at a time, 
    and completing a mission automatically blocks any further notes modifications.
  </li>
  <li>
    <strong>Cleanup / Deletion:</strong> 
    missions can only be deleted if they are already complete.
  </li>
</ul>

<h2>6. Contact / Q&A</h2>
<p>
  If you have any questions, feel free to reach me at: 
  <a href="mailto:boghtml@gmail.com">boghtml@gmail.com</a>.
</p>

</body>
</html>
