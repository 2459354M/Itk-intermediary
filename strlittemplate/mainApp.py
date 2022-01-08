from core.MultiApp import App

smalls = {
    'github': "https://github.com/2459354M/Itk-intermediary",
    'gitlab': "https://stgit.dcs.gla.ac.uk/team-project-h/2021/cs34/itk-reporting",
    'docker': "https://hub.docker.com/repository/docker/2459354m/itk-production",
    'other': "otherstuff"
}

myapp = App("multiApp", "Streamlit Multi Theme App", smalls)

myapp.main()
