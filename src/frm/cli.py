import argparse

class InitAction(argparse.Action):
    supported_projects = ["java", "python", "php"]

    def __call__(self, parser, namespace, values, option_string=None):
        project_type = values[0]
        if project_type.lower() not in self.supported_projects:
            parser.error("Project Type not supported yet!")
        namespace.project_type = project_type.lower()

def create_parser():
    parser = argparse.ArgumentParser(
        description="""
            CLI framework to quickly setup CD workflow for your project.
        """
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--init", help="Initialize continuous-delivery workflow for a specific project type (java, php...).",
                        nargs=1,
                        metavar="PROJECT_TYPE",
                        action=InitAction
                        )

    group.add_argument("--clean", help="Reset continuous-delivery workflow state to default.", action="store_true")
    group.add_argument("--destroy", help="Remove continuous-delivery workflow.", action="store_true")
    group.add_argument("--info", help="Get quick info about the continuous delivery workdlow.", action="store_true")

    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = vars(parser.parse_args())
    if "project_type" in args:
        print("Init Workflow")
    elif args["clean"]:
        print("Clean Workflow")
    elif args["destroy"]:
        print("Destroy Workflow")
    elif args["info"]:
        print("Info Workflow")

def main():
    pass