# Web-Server-Programming
Lab 1 for CSE4344 Computer Network Organization

ASSIGNMENT DESCRIPTION:

In this project, we will develop a multi-thread web server, capable of serving multiple
requests in parallel. You can refer to the textbook for this assignment as well.

Basic Requirements:

The basic functional requirements of the web server are as below:

1) A webpage is stored on your server (assuming it is localhost). We assume it is
index.html but the name is your choice. This index.html shall contain at least one
image.

2) A process will be running on the server and listening to the specified port. We
assume it is 8080 but the port number is your choice.

3) In your web browser, if you type in http://localhost:8080/index.html, your web
server process shall fetch the index.html (or requested objects) from the file
system, compose the http response, and send it back to the browser.

4) If you web browser can display the page correctly, the web server process is
functioning as required for a Status Code 200 response.

5) You are required to implement 301, 404 Status Codes as well. You will need to
study (BY YOURSELF) meanings of these codes and how to implement the
proper additional header fields, if any.
