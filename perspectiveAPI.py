from googleapiclient import discovery
from googleapiclient.errors import HttpError
from enum import Enum
import time
from datetime import datetime


class EvaluationMode(Enum):
    SPAM = "SPAM"
    TOXIC = "TOXICITY"
    BOTH = "BOTH"


class PerspectiveAPI:
    API_KEY = None
    CLIENT = None
    DELAY = 1

    def __init__(self) -> None:
        with open("api-key.txt", 'r+') as keyfile:
            for line in keyfile.readlines():
                self.API_KEY = line.strip()
                break

        self.CLIENT = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=self.API_KEY,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
        )

    def getScore(self, sample, mode: EvaluationMode):
        if mode == EvaluationMode.BOTH:
            attr = {EvaluationMode.SPAM.value: {}, EvaluationMode.TOXIC.value: {}}
        else:
            attr = {mode.value: {}}

        analyze_request, score = {
            'comment': {'text': sample},
            'requestedAttributes': attr,
            "languages": ["en"],
            "doNotStore": True,
        }, 0

        try:
            response = self.CLIENT.comments().analyze(body=analyze_request).execute()

            if mode == EvaluationMode.BOTH:
                score = [
                    response['attributeScores'][EvaluationMode.SPAM.value]['summaryScore']['value'],
                    response['attributeScores'][EvaluationMode.TOXIC.value]['summaryScore']['value'],
                ]
            else:
                score = [
                    response['attributeScores'][mode.value]['summaryScore']['value']
                ]
                if mode == EvaluationMode.SPAM:
                    score.append(None)
                else:
                    score.insert(0, None)

            self.DELAY = 1

        except Exception as e:
            if type(e) == HttpError:
                self.DELAY = min(self.DELAY * 2, 60)
                print(f"API Time Limit Exception. Sleeping for {self.DELAY} at {datetime.utcnow()}")
                time.sleep(self.DELAY)

                return self.getScore(sample, mode)
            else:
                print(str(e))

        return score
