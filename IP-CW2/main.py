import argparse
from DataExtractor import DataExtractor
from ViewByBrowser import ViewByBrowser
from ViewByCountry import ViewByCountry
from AvidReaders import AvidReaders
from AlsoLikes import AlsoLikes
from GUI import GUI

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--user_uuid", help="Visitor UUID", required=False)
    parser.add_argument("-d", "--doc_uuid", help="Document UUID", required=False)
    parser.add_argument("-t", "--task_id", help="Task ID: 2a, 2b, 3a, 3b, 4, 5a, 5b, 6, 7", required=False)
    parser.add_argument("-f", "--file_name", help="JSON file path", required=False)

    args = parser.parse_args()

    # when no arguments are given
    if args.task_id is None and args.file_name is None:
        GUI()
        return

    df = None
    if args.file_name:
        loader = DataExtractor(args.file_name)
        df = loader.load()

    if args.task_id == "2a":
        v = ViewByCountry(df)
        print(v.getCountryCounts(args.doc_uuid))

    elif args.task_id == "2b":
        v = ViewByCountry(df)
        counts = v.getCountryCounts(args.doc_uuid)
        print(v.getContinentCounts(counts))

    elif args.task_id == "3a":
        vb = ViewByBrowser(df)
        print(vb.getUserAgentCounts())

    elif args.task_id == "3b":
        vb = ViewByBrowser(df)
        counts = vb.getUserAgentCounts()
        print(vb.getBrowserCounts(counts))

    elif args.task_id == "4":
        ar = AvidReaders(df)
        print(ar.getAvidReaders())

    elif args.task_id == "5d":
        al = AlsoLikes(df)
        results = al.sort_alsoLikes(args.doc_uuid)
        print(results)

    elif args.task_id == "6":
        al = AlsoLikes(df)
        al.displayGraph(args.doc_uuid, args.user_uuid)


    elif args.task_id == "7" or args.task_id.lower() == "gui":
        GUI(
            preset_doc=args.doc_uuid,
            preset_user=args.user_uuid,
            preset_file=args.file_name
        )

    else:
        print("Invalid task id")

if __name__ == "__main__":
    main()