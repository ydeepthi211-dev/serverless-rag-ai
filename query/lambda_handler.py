from rag_pipeline import run_rag
import json


def handler(event, context):
    body = json.loads(event.get("body", "{}"))
    question = body.get("question")

    answer = run_rag(question)

    return {
        "statusCode": 200,
        "body": json.dumps({"answer": answer})
    }
