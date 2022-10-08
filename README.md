# crontab

I created a virtual machine on microsoft azure
I ensured that required programs were installed and updated by running sudo apt-get update
I check the version of python being run on the system by running python
I created a local folder and wrote a python code that would request an api file as shown in the attached python file 
by running df=requests.get('https://data.cms.gov/data-api/v1/dataset/60ccbf1c-d3f5-4354-86a3-465711d81c5a/data'), among others


while coding, my challenge was establishing the path where the downloaded file will be stored on the virtual machine when the crontab is run

I then logged into the virtual machine and cloned the repo from git into the virtual machine

I encountered several errors while attempting to run crontab. I have attached screenshots from my attempts
