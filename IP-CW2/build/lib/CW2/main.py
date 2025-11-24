import argparse
from .DataExtractor import DataExtractor
from .ViewByBrowser import ViewByBrowser
from .ViewByCountry import ViewByCountry
from .AvidReaders import AvidReaders
from .AlsoLikes import AlsoLikes
from .GUI import GUI

def main():
    parser = argparse.ArgumentParser(description="Document Tracking System")

    parser.add_argument("-u", "--user_uuid", help="Visitor UUID", required=False)
    parser.add_argument("-d", "--doc_uuid", help="Document UUID", required=False)
    parser.add_argument("-t", "--task_id", help="Task ID: 2a, 2b, 3a, 3b, 4, 5d, 6, 7", required=False)
    parser.add_argument("-f", "--file_name", help="JSON file path", required=False)

    args = parser.parse_args()

    # when no arguments are given
    if args.task_id is None and args.file_name is None:
        GUI(
            preset_doc=args.doc_uuid,
            preset_user=args.user_uuid,
            preset_file=args.file_name
        )
        return
        print("Error: arguments required.")

    # GUI mode
    if args.task_id == "7":
        GUI(
            preset_doc=args.doc_uuid,
            preset_user=args.user_uuid,
            preset_file=args.file_name
        )
        return

    # the rest of the task need filename
    if not args.file_name:
        print("Error: -f issuu.json required for this task.")
        return

    loader = DataExtractor(args.file_name)
    df = loader.load()

    if args.task_id == "2a":
        v = ViewByCountry(df)
        counts = v.getCountryCounts(args.doc_uuid)
        print(counts)
        v.displayCountries(counts, args.doc_uuid)

    elif args.task_id == "2b":
        v = ViewByCountry(df)
        counts = v.getCountryCounts(args.doc_uuid)
        cont = v.getContinentCounts(counts)
        print(cont)
        v.displayContinents(cont, args.doc_uuid)

    elif args.task_id == "3a":
        vb = ViewByBrowser(df)
        counts = vb.getUserAgentCounts()
        print(counts)
        vb.displayUserAgents(counts)

    elif args.task_id == "3b":
        vb = ViewByBrowser(df)
        counts = vb.getUserAgentCounts()
        simple = vb.getBrowserCounts(counts)
        print(simple)
        vb.displaySimplified(simple)

    elif args.task_id == "4":
        ar = AvidReaders(df)
        table = ar.getTableOfReaders()
        print(table)

    elif args.task_id == "5d":
        al = AlsoLikes(df)
        results = al.sort_alsoLikes(args.doc_uuid)
        print(results)

    elif args.task_id == "6":
        al = AlsoLikes(df)
        try:
            al.displayGraph(args.doc_uuid, args.user_uuid)
        except Exception as e:
            print("Graph Error", f"Could not generate graph:\n{e}")

    else:
        print("Invalid task id")

# if __name__ == "__main__":
#     main()