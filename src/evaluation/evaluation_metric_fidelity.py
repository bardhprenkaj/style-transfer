from src.evaluation.evaluation_metric_base import EvaluationMetric
from src.core.oracle_base import Oracle
from src.core.explainer_base import Explainer


class FidelityMetric(EvaluationMetric):
    """As correctness measures if the algorithm is producing counterfactuals, but in Fidelity measures how faithful they are to the original problem,
     not just to the problem learned by the oracle. Requires a ground truth in the dataset
    """

    def __init__(self, config_dict=None) -> None:
        super().__init__(config_dict)
        self._name = 'Fidelity'

    def evaluate(self, instance , explanation , oracle : Oracle=None, explainer : Explainer=None, dataset = None):
        instance_2 = explanation.top
        
        label_instance_1 = oracle.predict(instance)
        label_instance_2 = oracle.predict(instance_2)
        oracle._call_counter -= 2

        prediction_fidelity = 1 if (label_instance_1 == instance.label) else 0
        
        counterfactual_fidelity = 1 if (label_instance_2 == instance.label) else 0

        result = prediction_fidelity - counterfactual_fidelity
        
        return result