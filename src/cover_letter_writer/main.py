#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from cover_letter_writer.crew import CoverLetterWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'job_posting_url': 'https://www.indeed.com/jobs?q=ai+engineer&from=searchOnDesktopSerp&radius=25&start=120&vjk=7b7674e718f7f2eb',
        'github_url': 'https://github.com/amohseni',
        'personal_writeup': """Adam is AI specialist"""
    }
    
    try:
        CoverLetterWriter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'job_posting_url': 'https://www.indeed.com/jobs?q=ai+engineer&from=searchOnDesktopSerp&radius=25&start=120&vjk=7b7674e718f7f2eb',
        'github_url': 'https://github.com/amohseni',
        'personal_writeup': """Adam is AI specialist"""
    }
    try:
        CoverLetterWriter().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CoverLetterWriter().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'job_posting_url': 'https://www.indeed.com/jobs?q=ai+engineer&from=searchOnDesktopSerp&radius=25&start=120&vjk=7b7674e718f7f2eb',
        'github_url': 'https://github.com/amohseni',
        'personal_writeup': """Adam is AI specialist"""
    }
    try:
        CoverLetterWriter().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
