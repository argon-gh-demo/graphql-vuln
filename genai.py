from textwrap import dedent

def unsafe(request):
  # ruleid: eval-format-string-in-python-for-langchain
    agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    prompt=data
    )
    repsone = agent.run(event)
    code = """
    print(%s)
    """ % repsone
    eval(code)
