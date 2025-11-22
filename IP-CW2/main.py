import argparse
from DataExtractor import DataExtractor
from ViewByBrowser import ViewByBrowser
from ViewByCountry import ViewByCountry
from AvidReaders import AvidReaders
from AlsoLikes import AlsoLikes
from GUI import GUI

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--user_uuid")
    parser.add_argument("-d", "--doc_uuid")
    parser.add_argument("-t", "--task_id")
    parser.add_argument("-f", "--file_name", required=True)

    args = parser.parse_args()

    loader = DataExtractor(args.file_name)
    df = loader.load()

    if args.task_id == "2a":
        v = ViewByCountry(df)
        c = v.getCountryCounts(args.doc_uuid)
        print(c)

    elif args.task_id == "2b":
        v = ViewByCountry(df)
        c = v.getCountryCounts(args.doc_uuid)
        cont = v.getContinentCounts(c)
        print(cont)

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
        func = lambda x: -x[1]
        print(al.alsoLikes(args.doc_uuid, func)[:10])

    elif args.task_id == "6":
        al = AlsoLikes(df)
        al.displayGraph(args.doc_uuid, args.user_uuid)


    elif args.task_id == "7" or args.task_id.lower() == "gui":
        GUI(
            preset_doc=args.doc_uuid,
            preset_user=args.user_uuid,
            preset_task=(
                "2a - Views by Country" if args.task_id == "2a" else
                "2b - Views by Continent" if args.task_id == "2b" else
                "3a - Browser Histogram" if args.task_id == "3a" else
                "3b - Simplified Browser Histogram" if args.task_id == "3b" else
                "4 - Top 10 Avid Readers" if args.task_id == "4" else
                "5d - Also Likes Top 10" if args.task_id == "5d" else
                "6 - Generate Also-Likes Graph" if args.task_id == "6" else
                None
            ),
            preset_file=args.file_name
        )

    else:
        print("Invalid task id")

if __name__ == "__main__":
    main()