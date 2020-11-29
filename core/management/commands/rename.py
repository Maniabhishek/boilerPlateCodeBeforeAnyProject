from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self,parser):
        parser.add_argument('new_project_name',type=str,help='the new django project name')

        # parser.add_argument('-p','--prefix') optional argument for prefix
    def handle(self, *args , **kwargs):
        new_project_name = kwargs['new_project_name']

        # logic t replace each older name to newer in tom each file

        files_to_rename = ['demo/settings/base.py','demo/wsgi.py','manage.py']
        folder_to_rename = 'demo'

        for f in files_to_rename:
            with open(f,'r') as file:
                filedata = file.read()
            filedata=filedata.replace('demo',new_project_name)

            with open(f,'w') as file:
                file.write(filedata)


        os.rename(folder_to_rename,new_project_name)
        self.stdout.write(self.style.SUCCESS('project has been renamed to %s' %new_project_name))
