from CW2.core import run_gui
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # CLI mode
        # Example:
        #   myapp.exe -u ... -d ... -t ...
        from CW2.CLI import main as cli_main
        cli_main()
    else:
        run_gui()
