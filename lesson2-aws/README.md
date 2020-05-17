* Task: Create cloudformation template which should create the following infrastructure:
    - All the infrastructure should be created automatically
    - Load Balancer
    - 2 E2C instances
    - Should install apache/nginx
    - When load balancer link is opened it should display "Hello World" html-page
    - Switching off any of the two instances should not affect html-page accessibility

* Scores:
    - (1x*)  html page should display "Hello from `server ip address`"
    - (2x*)  html page should display image from S3 bucket
    - (6х*)  Use AWS Lambda for tasks listed above
    - (10х*) Use Terraform for all the tasks listed above

Solution should be present as a single file - Cloudformation template (or Terraform)