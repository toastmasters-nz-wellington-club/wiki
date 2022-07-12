import mkdocs_gen_files

with mkdocs_gen_files.open("next_meeting_agenda_redirect.html", "w") as dst:
    with open('extras/next_meeting_agenda_redirect.html', 'r') as src:
        dst.writelines(src.readlines())