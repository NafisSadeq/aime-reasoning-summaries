import os
from openai import OpenAI

class ReasoningClient:
    def __init__(self, api_key=None, model="o3"):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_reasoning_tokens = 0

    def get_reasoning_summary_and_output(self, prompt, effort="medium", summary_type="detailed"):
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            reasoning={
                "effort": effort,
                "summary": summary_type
            }
        )

        # Extract summaries
        summaries = [summary.text for summary in response.output[0].summary]

        # Extract final output
        output = response.output[1].content[0].text

        # Track token usage
        usage = response.usage
        self.total_input_tokens += usage.input_tokens
        self.total_output_tokens += usage.output_tokens
        self.total_reasoning_tokens += usage.output_tokens_details.reasoning_tokens

        return {
            "summaries": summaries,
            "output": output,
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "reasoning_tokens": usage.output_tokens_details.reasoning_tokens
        }

    def get_total_usage(self):
        return {
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_reasoning_tokens": self.total_reasoning_tokens
        }
