import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Chatbot program using OpenAI Chat Completion API"
    )
    parser.add_argument(
        "--role", default="helpful assistant", help="assign a role to chatbot"
    )
    parser.add_argument(
        "--use-context",
        nargs="?",
        const=True,
        default=False,
        help="use this flag to retain context between conversations",
    )
    return parser.parse_args().__dict__
