# ParallelBehaveAllureFlow
## Description
ParallelBehaveAllureFlow: A GitHub Actions workflow for parallel execution of Behave tests with efficient Allure report generation, streamlining and accelerating BDD testing in CI/CD pipelines. It integrates a retry mechanism within the behave_test_runner.py script, offering default retries up to n times, enhancing test reliability and reducing false negatives. Supported Browser at the moment: Chrome


## Usage of workflow
To use this workflow in your project, add a workflow file in your repository (e.g., `.github/workflows/test.yml`) with the following configuration:

```yaml
first_job:
    ...
    ...
reuse_job:
  needs: first_job
  permissions:
    contents: write
  uses: ggkiokas/ParallelBehaveAllureFlow/.github/workflows/reusable.yml@main
  with:
    ENV_VARS: |
      {
        "YOUR_ENV_VAR1": "${{ needs.first_job.outputs.ENV_VAR1 }}",
        "YOUR_ENV_VAR2": "${{ needs.first_job.outputs.ENV_VAR2 }}",
        "YOUR_ENV_VAR2": "ENV_VAR3"
      }
    PATHS: '["backend/behave","frontend/selenium_wd/behave/app2/myfeaturefile.feature"]'
    PYTHON_VERSION: "3.9"
    DB_PORT: "5430"
    DB_INSTANCE: "project:region:instance"
    
    #optional inputs
    RETRIES_NUM: 3  #  Number of retries for failed tests. Default is 3.
    SCREENSHOTS_PATH: 'screenshots/'  # Path to save screenshots of failed tests. Default is 'screenshots/'.

    secrets:
      CM_PASS_STAGING: ${{ secrets.CM_PASS_STAGING }}
      DB_PASSWORD_STAGING: ${{ secrets.DB_PASSWORD_STAGING }}
      GOOGLE_SERVICE_KEY_STAGING: ${{ secrets.GOOGLE_SERVICE_KEY_STAGING }}
      SF_PASS_STAGING: ${{ secrets.SF_PASS_STAGING }}
      CLOUD_GOOGLE_SERVICE_JSON_STAGING: ${{ secrets.CLOUD_GOOGLE_SERVICE_JSON_STAGING }}
```
ENV_VARS allows you to define environment variables that will be used in your test execution environment.

PATHS specifies the locations of the Behave feature files that you want to run in parallel.
In the example, all feature files in the backend/behave directory and a specific feature file frontend/selenium_wd/behave/app2/myfeaturefile.feature will be executed.

## General Information
- Python 3 is installed and the version can be specified as input
- For UI tests, Chrome and Chromedriver are installed in steps 'Install Chrome' and 'Setup ChromeDriver'.

## Database Connection
Currently, the workflow supports connections to Google Cloud SQL Database in step 'Connect to Google Cloud SQL Database'
To add new method for database connection follow the instructions on CONTRIBUTING.md



