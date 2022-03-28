import pandas as pd

from webApp.models import Project, Client

df = pd.read_excel("PROJECTS.xlsx")
df = df.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    client = Client.objects.create(name=row['CLIENT'])
    project = Project.objects.create(
        year=row['YEAR'],
        description=row['PROJECT'],
        location=row['LOCATION'],
        role=row['ROLE'],
        client=client
    )
    print(project.description)
