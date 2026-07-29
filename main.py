from graph.workflow import graph

def main():
    initial_state = {
        "user_request": "Please analyze the Titanic dataset and provide insights.",
        "dataset_path": "datasets/titanic.csv",
        "messages": [],
    }

    result = graph.invoke(initial_state)

    for m in result["messages"]:
        m.pretty_print()
        
    print(result["report_generator_report"].report_path)
    
if __name__ == "__main__":
    main()