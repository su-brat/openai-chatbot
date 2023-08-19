import os

from dotenv import load_dotenv

from helpers.conversation import OpenAiConversation
from helpers.terminal_args import parse_arguments


def main():
    args = parse_arguments()
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assistant = OpenAiConversation(api_key=api_key)
    assistant.do_conversation(
        assistant_role=args["role"], use_context=args["use_context"]
    )


if __name__ == "__main__":
    main()
