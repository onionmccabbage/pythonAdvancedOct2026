### Review 3 

##### 1hr 15mins

if you wish, use microservices, DB, API, i/o context etc. within your work

#### Client Server (Microservices):

* Write a new server (a microservice) as a front-end to your database from yesterday.
(Or copy my code if you like)
* The client should send requests to the server, for specific creatures, (or posts or todos if you have them)
* The server responds by querying the database (or API) and returning 
a nicely formatted response about that creature, post or todo
* Remember to use .encode() and .decode()
* Find a way for the client to ask the proxy server to add or update members of the database. 
(Work on one data-type first, such as creatures, then generalize for the others)
* **Optionally**, the client can persist server responses as bytefiles. 
(Write to a byte file every time something happens, maybe use redirection)

#### Alternative (instead of the above)
* In a server, check if the buffer is one of 'users', 'posts', 'todos', 'photos' or 'albums'
* If so, fetch the relevant data set from the jsonplaceholder REST API and return it to the client.
(either import your existing 'requests' code or write a module for this)
* Find a way for the client to specify a category AND an id.
(If a valid category is not passed, choose sensible defaults)
* Adapt the client so it checks to see if a valid category and id have been injected as system argument variables
* If not, ask for a category and an id number from the user, then pass these to the server
* The server then requests 'https://jsonplaceholder.typicode.com/<category>/<id>'
and sends the response back to the client
* e.g. requests.get( f'{apiURL}/{cat}/{id}' )
* Make the server write a nicely formatted byte log file of every request it receives

Further Options
===============
* Provide a means of context-switching the output from the server
* For example the default could be printing to the console,
but context options could write to a text file or a byte file
* Send context options in the client request to control how the server streams its output

Around tea break there will be a chance to show you code