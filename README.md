# ParallelBehaveAllureFlow
## Description
ParallelBehaveAllureFlow: A GitHub Actions workflow for parallel execution of Behave tests with efficient Allure report generation. Streamlines and accelerates BDD testing in CI/CD pipelines.

## General Information
- Python is installed and the version can be specified as input
- For UI tests, Chrome and Chromedriver are installed in steps 'Install Chrome' and 'Setup ChromeDriver'.
## Database Connection
Currently, the workflow supports connections to Google Cloud SQL Database. To configure this connection, you need to set up the necessary secrets and specify the appropriate inputs in your workflow file. To add new method for database connection follow the instructions on CONTRIBUTING.md

### Example Configuration for Google Cloud SQL:

```yaml
    steps:
    - name: Connect to Google Cloud SQL Database
      continue-on-error: true 
      uses: mattes/gce-cloudsql-proxy-action@v1
      with:
        creds: ${{ secrets.CLOUD_GOOGLE_SERVICE_JSON_STAGING }}
        instance: calypso-staging-werc:europe-west3:calypso-staging-2fvg
        port: ${{ inputs.DB_PORT }}

```

## Usage of workflow
To use this workflow in your project, add a workflow file in your repository (e.g., `.github/workflows/test.yml`) with the following configuration:

```yaml
reuse_job:
  needs: first_job
  permissions:
    contents: write
  uses: ggkiokas/ParallelBehaveAllureFlow/.github/workflows/reusable.yml@main
  with:
    ENV_VARS: |
      {
        "DEVICE_VIEW": "${{ needs.first_job.outputs.DEVICE_VIEW }}",
        "ENV": "${{ needs.first_job.outputs.ENV }}",
        "MACHINE": "${{ needs.first_job.outputs.MACHINE }}",
        "SF_EMAIL": "${{ needs.first_job.outputs.SF_EMAIL }}",
        "TIMEOUT_UI": "${{ needs.first_job.outputs.TIMEOUT_UI }}"
      }
    PATHS: '["backend/behave/sf_app", "frontend/selenium_wd/behave/sf_app","frontend/selenium_wd/behave/cm_app"]'
    PYTHON_VERSION: "3.9"
    DB_PORT: "5430"