from cli.parser import build_parser
from cli.commands import handle_command

def main():
    parser = build_parser()
    args = parser.parse_args()
    handle_command(args)

if __name__ == "__main__":
    main()