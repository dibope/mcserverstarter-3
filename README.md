## Runs entirely on github no need to download 
#### (only thing u need to do is add email and password)
### Table of contents:
- [Setup](https://github.com/dibope/mcserverstarter-3/blob/main/README.md#to-use-it-for-ur-seedloaf-server)
- [Prevent friends from changing code](https://github.com/dibope/mcserverstarter-3/blob/main/README.md#to-prevent-them-from-changing-the-code) (Make sure u do this too!)

### To use it for ur seedloaf server:

1)Fork this and create 2 repository secrets named USERNAME, PASSWORD.(ur email and seddloaf password)

  To add repository secret:(Settings > Secrets and variables > Actions > repository secrets)

( No one can see them after u set so it's really a secret)
![repo_secrets1](https://github.com/dibope/mcserverstarter-3/blob/main/.github/workflows/Images/repo_secrets1.jpg)

2)Click Start the mc Server then Run workflow. Refresh page to view the run.
![start_mc](https://github.com/dibope/mcserverstarter-3/blob/main/.github/workflows/Images/startmc.jpg)

3)Add your friends as collaborators.
![collaboraters](https://github.com/dibope/mcserverstarter-3/blob/main/.github/workflows/Images/collaboraters.jpg)

### To prevent them from changing the code:

1)Go to settings>branchs>branch protection rule>Require status check>select "fail-job" or type if not appearred.
![fail_job1](https://github.com/dibope/mcserverstarter-3/blob/main/.github/workflows/Images/fail_job1.jpg)
![fail_job2](https://github.com/dibope/mcserverstarter-3/blob/main/.github/workflows/Images/fail_job2.jpg)

2)Set ur friends with read only access

