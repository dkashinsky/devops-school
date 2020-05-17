Tasks and scores:

* (+ 0.3) Install Jenkins on CentOS 7/8 local virtual machine or AWS (be caucious in case of AWS)
* (+ 0.1) Setup Jenkins plugins (manually)
    - Git plugin
    - Pipeline
    - Credentials Binding Plugin
    - Ansible
    - Generic Webhook Trigger Plugin
    - https://www.jenkins.io/doc/pipeline/steps/nexus-artifact-uploader/
    - Any other plugins if you need them
* (+ 0.1) Create non admin user for Jenkins
* (+ 0.1) Create private github repository and upload your project there
    - It should contain `ops-tools` folder containing `Jenkinsfile` and `ansible` scripts
* (+ 0.1) Create pipeline which will build your application and publish it into nexus repository (based on `lesson4`)
* (+ 0.2) Create pipeline which will deploy your application pulling artifacts from nexus (based on `lesson4`)
* (+ 0.1) Create pipeline which will make Quality Checks (run tests and linters). It can be based on webhooks or run on schedule
* (+ 0.4) Find and use Jenkins plugin for Nexus (to avoid using `curl` to push artefacts)
* (+ 0.4) Mark commits as successful or failed based on Quality Checks
* (+ 0.2) Once PR is merged, it should trigger build and deploy.

Scoring: max = 2, min = 1
