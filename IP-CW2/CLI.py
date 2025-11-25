import argparse
from helpers.DataExtractor import DataExtractor
from helpers.TaskManager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Document Tracking System")

    parser.add_argument("-u", "--user_uuid", help="Visitor UUID", required=True)
    parser.add_argument("-d", "--doc_uuid", help="Document UUID", required=True)
    parser.add_argument("-t", "--task_id", help="Task ID: 2a, 2b, 3a, 3b, 4, 5d, 6, 7", required=True)
    parser.add_argument("-f", "--file_name", help="JSON file path", required=True)

    args = parser.parse_args()

    # when no arguments are given
    if args.task_id is None or args.file_name is None:
        print("Error: arguments required.")
        return

    df = DataExtractor().load(args.file_name)

    tm = TaskManager()
    output = tm.run_task(args.user_uuid, args.doc_uuid, args.task_id, df)
    print(output)

if __name__ == "__main__":
    main()
