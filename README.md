# DATA - Admin

David Williamson @ Varilink Computing Ltd

Configuration to enable the use of the Django admin interface to manage the Derby Arts and Theatre Association website's database. This has been put in place as a retro fit for the application's database.

As well as enabling the use of the Django admin interface this also facilitates the use of Django migrations, which I use specifically for the publication of news items on the website.

The steps for publishing a news item are as follows:

1. Add a migration file for the news item in `whatson/migrations/` by copying the previous migration file.
2. Change the file name to something meaningful for the planned news item and increment the prefix number in the file name also.
3. Edit the content of the file, remembering to update the published date, title, image, precis, item text and dependencies.
4. Copy the new migration file to the deployment environment.
6. Run the migration `python3 manage.py migrate whatson`, which you must do with `root` privilege in the Django project's home folder.
