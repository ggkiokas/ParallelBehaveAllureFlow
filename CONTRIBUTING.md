### CONTRIBUTING.md

# Contributing to ParallelBehaveAllureFlow

## Adding Secrets
To contribute to the repository, especially for enhancements like database access, you may need to add new secrets:

# Example
Add a new secret to the existing ones
```yaml
    secrets:
      ...
      ...
      NEW_SECRET:
        required: false
```

## Adding new Database connection methods
To contribute to the repository, especially for enhancements like database access, you may need to add a new method for
database connection.
IMPORTANT: you must add continue-on-error: true  otherwise the workflow will timeout

# Example
Add a new secret to the existing ones
```yaml
    steps:
    - name: Connect to PostgreSQL Database
      continue-on-error: true 
      run: |
        PGPASSWORD=${{ secrets.POSTGRES_PASSWORD }} psql -h ${{ secrets.POSTGRES_HOST }} -U ${{ secrets.POSTGRES_USER }} -d ${{ secrets.POSTGRES_DB }} -c "SELECT version();"
```

# General steps
1. **Create a Pull Request:**
   - Fork the repository.
   - Add or modify the workflow file in your fork to include the steps for your specific database or other services.
   - Commit the changes to your fork.

2. **Add Secrets for Testing:**
   - In your forked repository, go to settings.
   - Navigate to 'Secrets', then 'Actions'.
   - Add the required secrets for your changes.

3. **Submit the Pull Request:**
   - Once you've tested your changes and added necessary documentation, submit a pull request to the main repository.

## Guidelines
- If adding new features, consider updating the README.md with usage instructions.

## Testing
- Test your changes thoroughly before submitting a pull request.
- Ensure that existing functionality is not adversely affected.

## Review
- All contributions will be reviewed for compatibility and adherence to project goals.
- Please be responsive to feedback if changes are requested.