class EvaluationMetrics:
    """Class to calculate evaluation metrics for GENAI models."""

    def calculate_accuracy(self, predictions, ground_truth):
        """
        Calculate accuracy based on predictions and ground truth.

        Args:
            predictions (list): List of model predictions.
            ground_truth (list): List of ground truth labels.

        Returns:
            float: Accuracy as a percentage.
        """
        if len(predictions) != len(ground_truth):
            raise ValueError("Predictions and ground truth lists must have the same length.")

        correct_count = sum(1 for pred, truth in zip(predictions, ground_truth) if pred == truth)
        accuracy = (correct_count / len(ground_truth)) * 100
        print(f"Accuracy: {accuracy:.2f}%")
        return accuracy

# Example usage
if __name__ == "__main__":
    eval_metrics = EvaluationMetrics()
    predictions = ["cat", "dog", "bird", "cat"]
    ground_truth = ["cat", "man", "bird", "dog"]
    eval_metrics.calculate_accuracy(predictions, ground_truth)
