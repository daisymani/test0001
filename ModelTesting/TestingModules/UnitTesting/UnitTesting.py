class RelevanceTester:
    """Class to test the relevance of model outputs to input prompts."""

    def evaluate_relevance(self, prompt, output, expected_keywords):
        """
        Evaluate if the output directly answers the input query.

        Args:
            prompt (str): The input query or prompt.
            output (str): The model's output.
            expected_keywords (list): List of keywords expected in the output.

        Returns:
            bool: True if the output is relevant, False otherwise.
        """
        relevance_score = sum(1 for keyword in expected_keywords if keyword in output)
        is_relevant = relevance_score == len(expected_keywords)
        print(f"Prompt: {prompt}")
        print(f"Output: {output}")
        print(f"Expected Keywords: {expected_keywords}")
        print(f"Relevance Score: {relevance_score}/{len(expected_keywords)}")
        print(f"Is Relevant: {is_relevant}")
        return is_relevant

    def check_response_originality(self, output, reference_texts):
        """
        Check the originality of the response by comparing it with reference texts.

        Args:
            output (str): The model's output.
            reference_texts (list): List of reference texts to compare against.

        Returns:
            bool: True if the response is original, False if it matches any reference text.
        """
        is_original = all(output != reference for reference in reference_texts)
        print(f"Output: {output}")
        print(f"Reference Texts: {reference_texts}")
        print(f"Is Original: {is_original}")
        return is_original

# Example usage
if __name__ == "__main__":
    tester = RelevanceTester()
    prompt = "What is the capital of France?"
    output = "The capital of France is Paris."
    expected_keywords = ["capital", "France", "Paris"]
    tester.evaluate_relevance(prompt, output, expected_keywords)
    reference_texts = ["The capital of France is Paris.", "Paris is the capital of France."]
    output = "The capital of France is Paris."
    tester.check_response_originality(output, reference_texts)
