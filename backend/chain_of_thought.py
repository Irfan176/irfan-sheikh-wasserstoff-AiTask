from rag_processor import generate_response

def develop_reasoning_steps(initial_response, previous_context):
    steps = [initial_response]
    for context in previous_context:
        steps.append(generate_response(context))
    return steps

def refine_response_based_on_thought_steps(thought_steps):
    return " ".join(thought_steps)

def process_query_with_chain_of_thought(user_query, previous_context):
    initial_response = generate_response(user_query)
    thought_steps = develop_reasoning_steps(initial_response, previous_context)
    final_response = refine_response_based_on_thought_steps(thought_steps)
    return final_response
