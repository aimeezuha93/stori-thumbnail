### STORI-THUMBNAIL
-----

First of all, let me tell you the original idea of the project: You have a simple web page where the user will be able to upload an image to get a thumbnail version of it. This web page will upload the image to a S3 bucket which by a trigger will process the image to obtain the desired result.
Now, is the idea complete? No
Why not? Lack of knowledge of web programming, time, call it whatever you want :(

Now, based on the original idea, I will present the strengths and weaknesses of the project.

#### Strengths

1. The user will be able to select any image, this gives us the dynamism to be able to reprocess any image without having to decide ourselves, the owners of the solution.

2. The user will not have any contact with the back of the solution, due to security issues or lack of knowledge, their front end will only be a simple web page.

3. By using AWS lambdas services we can ensure that we will not take up as much processing as, for example, a Glue job because, in part, we are using it with simple tasks in mind.

4. Speaking of saving costs, we can ensure that by using an event trigger, the requests made will not be too high considering the purpose of the solution.


#### Weaknesses

1. Unfortunately the main code that performs the image resizing is very simple, a single function that cannot be expanded to more functionality possibilities.

2. I used predefined libraries that help with image processing, it may be better to create an algorithm that is more adaptable to future needs.

3. Lack of back-end monitoring of the solution.

4. I am combining both the serverless framework and Cloudformation for deploying resources, everything could be done using only one of them.