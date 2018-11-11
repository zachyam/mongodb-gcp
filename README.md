# mongodb-gcp

This is a playground project to get my feet wet with 3 main technologies:

1. MongoDB Atlas
2. Kubernetes on GCP
3. Golang

MongoDB Atlas is a fully-automated cloud database built by MongoDB. Atlas handles the complexities of handling/deploying your cloud database.

With a few clicks, I was able to sign up for a free tier on Atlas and deploy a basic database cluster

Setting up a Kubernetes cluster was by far the hardest component of this project. I had to create a project, then create a cluster, and learn about deploying an application using manifest files.

For this project, I had a python script make a GET call to my webserver. The script and webserver were deployed as separate nodes within the same Kubernetes cluster.

With every GET call, the script would save details about the api call to my Mongo database: timestamp, request code and the response text. It is a very simple script to get up and running with a Mongo DB.

Lastly, the webserver was written in Go. I had not used Golang before and I wanted to try it out as I heard that it is more performant than Python when it comes to handling concurrent requests
