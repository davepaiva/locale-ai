---


---

<h1 id="locale.ai-interview-task"><strong><a href="http://Locale.ai">Locale.ai</a> interview task:</strong></h1>
<h2 id="back-end-task"><em>1. Back-end Task:</em></h2>
<ul>
<li><em><strong>Task Statement</strong></em>:<br>
XRides, delivers about a 200 rides per minute or 288,000 rides per day. Now, they want to send this data to your system via an API. Your task is to create this API and save the data into PostgreSQL. The API should be designed, keeping in mind the real-time streaming nature of data and the burst of requests at peak times of the day. The user of this API expects an acknowledgment that the data is accepted and a way to track if the request fails.</li>
</ul>
<p>Brownie Points:</p>
<ol>
<li>Write a query DSL of how you would want this data to be queried and how someone would be able to run analytics operations on top of it.</li>
<li>Write up on the ideal system architecture and the design of API given enough time and resources.</li>
</ol>
<p>Ideal Tech Stack : Python/Go.</p>
<ul>
<li><em><strong>Implementation</strong></em>:<br>
Coming across the  terms “Real time , streaming nature and bursts of data”  I decided to implement the API using a micro-service based server less architecture. Some of the great things about the cloud based server less architecture is that one  doesn’t have to  worry about server setup, security, provisioning or even scaling during bursts. For infrequent usage, it is also cost effective as compared to running a server. I prefer working with a micro-service based architecture because it helps modularize code, isolating components of the systems, delivering quicker and safer iterations of code.</li>
</ul>
<p>Some of the providers are : Amazon Web Services &amp; Google Firebase.</p>
<p>I had worked previously on a Geo location based web app using Firebase but realized that Firebase wasn’t optimized for handling Geo coordinates because it only supported shallow queries in Firestore (No SQL database for Firebase).<br>
Also as the solution required a PostgreSQL database, I decided to use AWS.</p>
<p>This was my first project on AWS , but due to the ample documentation and tutorials I was able to come up with a solution without much difficulty.</p>
<p><a href="https://aws.amazon.com/api-gateway/">AWS API Gateway</a> provides a simple way to create API endpoints at any given scale.Using a POST method API , I created an endpoint through which we could pass  data as query string parameters. I chose the POST method because it is more reliable than GET for larger number of parameter, also GET method does not have a post-body.</p>
<p>Example of  API Endpoint:</p>
<p><a href="https://1714r7h89a.execute-api.ap-south-1.amazonaws.com/api/">https://1714r7h89a.execute-api.ap-south-1.amazonaws.com/api/</a></p>
<p>Example of POST request to the API Endpoint:</p>
<pre><code>curl --location --request POST "https://1714r7h89a.execute-api.ap-south-1.amazonaws.com/api/?booking_id=1&amp;vehicle_model_id=3&amp;package_id=4&amp;travel_type_id=5&amp;from_area_id=6&amp;to_area_id=7&amp;from_city_id=8&amp;to_city_id=9&amp;from_date=10&amp;to_date=11&amp;online_booking=12&amp;booking_created=13&amp;from_lat=14&amp;from_long=15&amp;to_lat=16&amp;to_long=17&amp;driver_id=18&amp;user_id=22"
</code></pre>
<p>Next I needed a PostgreSQL database, to store all this incoming data.This was done using <a href="https://aws.amazon.com/rds/postgresql/">AWS RDS for PostgreSQL</a>, which sets us a remote database instance in the cloud.Using pgAdmin 4 I connected to the remote database and implemented a many-one schema containing 4 tables: drivers, riders &amp; rides.</p>
<p>Finally, I needed a way to parse the data in the API query string, into the PostgreSQL database. Keeping in mind that  the preferred language is Python I decided to implement a Python <a href="https://aws.amazon.com/lambda/">AWS Lambda Function</a>.The Lambda function was implemented using AWS CLI and Chalice which is a AWS library for packaging and deploying python lambda functions. <a href="https://github.com/davepaiva/locale-ai/blob/master/locale-api/app.py">Here</a> is the complete Lambda function that parses the query strings to the PostgreSQL database.</p>
<p>Once a user has passed the data through the API, if successful it will return the primary keys of all 3 tables along with a success <a href="http://message.In">message.In</a> the case of any error it will return a error trace-back from the python Lambda function.</p>
<p>AWS API Gateway + Lambda Functions takes care of the stream and burst nature of the data as it only bills when triggered (every 100 milliseconds). So during peak times it will scale dynamically according to the number of times it is invoked.</p>
<p>Given enough time and resources I would :</p>
<ul>
<li>Implement real time data analysis using <a href="https://aws.amazon.com/kinesis/data-analytics/">AWS Kinesis</a>.</li>
<li>Implement <a href="https://postgis.net/features/">POSTGIS</a> for the PostgreSQL.</li>
<li>Experiment with <a href="https://graphql.org/">GraphQL</a> and a NoSQL database for scaling purposes.</li>
</ul>
<h2 id="data-science-task"><em>2. Data Science Task:</em></h2>
<ul>
<li>
<p><em><strong>Task Statement:</strong></em><br>
The biggest challenge for XRides is to increase the utilization rate of their cabs. However, the<br>
demand keeps fluctuating based on the area, time of day, etc. Your task is to device a<br>
geo-surge strategy that would help them incentivize their drivers. Identify what areas and at<br>
what times get most bookings and how would you increase the price in those areas in order to<br>
meet the demand.<br>
More than any other task, it will be critical for you to get a deep understanding of the dataset,<br>
the business and how you can help them.<br>
Brownie points if you share a recommendation or strategy backed by data that helps them<br>
reduce cancellation, increase revenue or reduce costs.</p>
</li>
<li>
<p><strong>Implementation:</strong></p>
</li>
</ul>
<p>Jupyter Notebook showing data analyses can be found <a href="https://github.com/davepaiva/locale-ai/blob/master/Data%20Science.ipynb">here</a> <em>(all maps can be exported as html leaflet.js files)</em> .</p>
<p><em>Dynamic Pricing Model:</em></p>
<ul>
<li>During high demand, prices increase so that drivers are incentivized to that particular location.</li>
<li>As more and more drivers come and demand slowly subsides, prices return to normal.</li>
<li>Other than increasing supply, increased prices will also tend to decrease demand. Make the service run more smoother.</li>
<li>If demand is low , offering promotions to boost up demand (hence pricing) would benefit the company.</li>
</ul>
<p><em>Some points to consider:</em></p>
<ul>
<li>At exact time riders want high supply , drivers do not work at that time.Low supply arises sometimes because Drivers prefer not to drive at current condition (Bad weather, Late nights, weekends etc).</li>
<li>During most peak hours (eg: right after work), other modes of public transport are also jammed. Therefore can use this to our advantage.</li>
<li>Number of cancelled rides could be because of no supply (waiting too long, cabs far away).</li>
</ul>

