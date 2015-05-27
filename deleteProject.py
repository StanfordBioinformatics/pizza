import dxpy
from argparse import ArgumentParser

description = "Given the name or object ID of a DNANexus project, deletes it. If the project is given by name, and a single project of that name is found, it will be deleted; however, if there are multiple projects found by that name, then none will be deleted, unless the --delete-all argument is passed, in which case all will be deleted."
parser = ArgumentParser(description=description)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--name",help="The name of the DNAnexus project. Quotation marks are optional around the name.")
group.add_argument("-dxid",help="The DNANexus object ID of the project.")
parser.add_argument("--delete-all",action="store_true",help="Only useful with the --name option. Add this in order to delete all projects that have the name given to --name.")

args = parser.parse_args()
name = args.name
dxid = args.dxid
deleteAll = args.delete_all

if name:
	name = name.strip("'").strip('"')
	res = list(dxpy.find_projects(name=name))
	if len(res) == 1 and deleteAllButMostRecent:
		pass
	elif len(res) > 1 and deleteAllButMostRecent:
		#blabla

	else:
		for i in res:
			dxpy.api.project_destroy(object_id=i['id'])
      #Could also delete a project this way:
      #  >project = dxpy.DXProject("project-BYz27380Z0fGVqP38v396Zx0")
      #  >project.destroy()
elif dxid:
	dxpy.abi.project_destroy(object_id=dxid)
		
			
			
	

