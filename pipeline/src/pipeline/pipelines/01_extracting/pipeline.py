from kedro.pipeline import Pipeline, node, pipeline
from .nodes import extract_subreddits 

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=extract_subreddits,
                inputs='params:extracted_subreddits.limit_requests',
                outputs="extracted_subreddits",
                name="extract_subreddits_node"
            )
        ]
    )
