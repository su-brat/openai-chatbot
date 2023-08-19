import openai

from .styling import Style


class OpenAiConversation:
    def __init__(
        self,
        api_key,
        user_prefix="You",
        assistant_prefix="Assistant",
        prefix_separator=":",
    ) -> None:
        self.openai = openai
        if not api_key:
            raise Exception("Empty API Key")
        self.openai.api_key = api_key
        self._user_prefix_text = f"{user_prefix}{prefix_separator}"
        self._assistant_prefix_test = f"{assistant_prefix}{prefix_separator}"

    def _get_user_prefix(self):
        return Style.red(Style.bold(self._user_prefix_text))

    def _get_assistant_prefix(self):
        return Style.blue(Style.bold(self._assistant_prefix_test))

    def get_single_response(self, messages, max_tokens=100):
        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=max_tokens
        )
        response = response["choices"][0]
        content = response["message"]["content"]
        response_completed = str(response["finish_reason"]).lower() == "stop"
        if response_completed:
            return content
        return f"{content}\n[INCOMPLETE DUE TO TECHNICAL REASONS]"

    def do_conversation(self, assistant_role="helpful assistant", use_context=True):
        system_message = {"role": "system", "content": f"You are {assistant_role}"}
        messages = [system_message]
        while True:
            try:
                user_input = input(f"{self._get_user_prefix()} ")
                messages.append({"role": "user", "content": user_input})
                response = self.get_single_response(messages)
                print(self._get_assistant_prefix(), response)
                if use_context:
                    messages.append({"role": "assistant", "content": response})
                else:
                    messages.pop()
            except KeyboardInterrupt:
                print()
                print(self._get_assistant_prefix(), "Bye, bye, see you later!")
                break
